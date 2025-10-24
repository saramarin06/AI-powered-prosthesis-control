import pandas as pd

def window_slicing_time(df, window_time, overlap, time_col="tiempo"):
    """
    Divide señales en ventanas de tamaño fijo en segundos.
    
    df: DataFrame con una columna de tiempo y señales.
    window_time: duración de la ventana en segundos.
    overlap: fracción de solapamiento (0 = sin solape, 0.5 = 50%, etc.)
    time_col: nombre de la columna de tiempo.
    """
    if not 0 <= overlap < 1:
        raise ValueError("El overlap debe estar entre 0 y <1")

    # Paso temporal (asumimos uniforme)
    dt = df[time_col].diff().mean()
    samples_per_window = int(window_time / dt)

    step = int(samples_per_window * (1 - overlap))
    if step <= 0:
        raise ValueError("El overlap es demasiado alto")

    # Extraer solo las señales
    signal_cols = [c for c in df.columns if c != time_col]
    signals = df[signal_cols].values  # (N, n_canales)

    ventanas = []
    for start in range(0, len(signals) - samples_per_window + 1, step):
        ventana = signals[start : start + samples_per_window]  # (200, canales)
        ventanas.append(ventana.T.flatten()) # aplano Pipe(la T es para que los valores si queden [b1, b2, b3, t1, t2, t3])

    # Nombres de columnas dinámicos
    col_names = []
    for col in signal_cols:
        for i in range(samples_per_window):
            col_names.append(f"{col}_{i}")

    return pd.DataFrame(ventanas, columns=col_names)

def Corte30s(lista_de_Ventanas):
    import pandas as pd
    # Recortar todas las señales a máximo 30 segundos
    lista_de_Ventanas_30s = []

    for idx, df_emg in enumerate(lista_de_Ventanas):
        print(f'Procesando señal {idx+1}/{len(lista_de_Ventanas)}')
        
        # Obtener duración actual
        tiempo_max = df_emg['tiempo'].max()
        tiempo_min = df_emg['tiempo'].min()
        duracion = tiempo_max - tiempo_min
        
        print(f'  Duración original: {duracion:.3f}s (de {tiempo_min:.3f}s a {tiempo_max:.3f}s)')
        
        # Filtrar solo hasta 30 segundos desde el inicio
        tiempo_inicio = df_emg['tiempo'].min()
        tiempo_limite = tiempo_inicio + 30.0
        
        df_recortado = df_emg[df_emg['tiempo'] <= tiempo_limite].copy()
        
        # Verificar
        nueva_duracion = df_recortado['tiempo'].max() - df_recortado['tiempo'].min()
        filas_eliminadas = len(df_emg) - len(df_recortado)
        
        print(f'  Duración final: {nueva_duracion:.3f}s')
        print(f'  Filas originales: {len(df_emg)}, Filas finales: {len(df_recortado)}')
        print(f'  Filas eliminadas: {filas_eliminadas}\n')
        
        lista_de_Ventanas_30s.append(df_recortado)

    print(f'Todas las señales ahora duran máximo 30 segundos')
    print(f'Nueva lista con {len(lista_de_Ventanas_30s)} señales')
    return lista_de_Ventanas_30s


def Etiquetador(lista_de_Ventanas_30s,df_times): # Entra una lista con las señales de 30s y los onset y offset en dataframe
    import pandas as pd
    Vent_eti = []

    # Para cada señal EMG en la lista
    for idx, df_emg in enumerate(lista_de_Ventanas_30s):
        print(f'Procesando señal {idx+1}/{len(lista_de_Ventanas_30s)}')
        
        # Determinar qué sujeto corresponde (cada sujeto tiene 3 muestras)
        sujeto_idx = idx // 3  # División entera: 0,1,2->0, 3,4,5->1, etc.
        muestra_num = (idx % 3) + 1  # Número de muestra: 1, 2, o 3
        
        print(f'  Sujeto {sujeto_idx+1}, Muestra {muestra_num}')
        
        # Obtener los tiempos de onset y offset de esta fila (convertir a float)
        # Reemplazar coma por punto para formato decimal
        onset1 = float(str(df_times.iloc[sujeto_idx, 0]).replace(',', '.'))
        offset1 = float(str(df_times.iloc[sujeto_idx, 1]).replace(',', '.'))
        onset2 = float(str(df_times.iloc[sujeto_idx, 2]).replace(',', '.'))
        offset2 = float(str(df_times.iloc[sujeto_idx, 3]).replace(',', '.'))
        onset3 = float(str(df_times.iloc[sujeto_idx, 4]).replace(',', '.'))
        offset3 = float(str(df_times.iloc[sujeto_idx, 5]).replace(',', '.'))
        
        
        print(f'  Rangos: [{onset1}-{offset1}], [{onset2}-{offset2}], [{onset3}-{offset3}]')

        onsets  = [onset1, onset2, onset3]
        offsets = [offset1, offset2, offset3]

        # Antes del primer onset → reposo
        Vent_eti.append([df_emg[df_emg['tiempo'] < onsets[0]].copy(), 0])

        # Recorre todos los pares onset/offset
        for i in range(len(offsets)):
            # Intervalo activo
            Vent_eti.append([
                df_emg[(df_emg['tiempo'] >= onsets[i]) & (df_emg['tiempo'] < offsets[i])].copy(),
                1
            ])
            
            # Intervalo de reposo entre este offset y el siguiente onset
            if i < len(onsets) - 1:
                Vent_eti.append([
                    df_emg[(df_emg['tiempo'] >= offsets[i]) & (df_emg['tiempo'] < onsets[i+1])].copy(),
                    0
                ])

    print(f'\nTotal de labels generados: {len(Vent_eti)}')
    return Vent_eti




import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

import os

def listar_archivos_mat(ruta_principal):
    """
    Recorre todas las carpetas y subcarpetas en 'ruta_principal'
    y devuelve una lista con las rutas completas de los archivos .mat
    """
    lista_paths = []
    for carpeta, _, archivos in os.walk(ruta_principal):
        for archivo in archivos:
            if archivo.lower().endswith(".mat"):  # Filtrar solo .mat
                lista_paths.append(os.path.join(carpeta, archivo))
    return lista_paths

def load_emg(file_path):
    """
    Carga un archivo .mat de LabChart y extrae los canales de Biceps y Triceps.

    Parámetros
    ----------
    file_path : str o Path
        Ruta relativa o absoluta al archivo .mat

    Retorna
    -------
    dict con claves 'Biceps' y 'Triceps' que contienen los arrays de señal
    """
    data = scipy.io.loadmat(file_path)

    # Extraemos la señal principal
    signals = data["data"].squeeze()

    # Extraemos títulos de los canales
    titles = data["titles"].squeeze()

    # Creamos un diccionario con las señales que necesitamos
    result = {}
    for i, title in enumerate(titles):
        if "Biceps" in title or "Triceps" in title:
            start = int(data["datastart"][i, 0]) - 1
            end = int(data["dataend"][i, 0])
            result[title.strip()] = signals[start:end]

##Debido a que le vamos a dar de entrada un dataframe a window slicing hay que anadir un vector de tiempo (Pipe)
    samplerate =  2000 #float(data['tickrate'].squeeze()[2]) 

    # Calcular el vector de tiempo
    # Tomamos la longitud de cualquiera de las señales (ambas tienen misma duración)
    if "Biceps" in result:
        n_samples = len(result["Biceps"])
    else:
        # Si no hay Biceps, usamos Triceps
        n_samples = len(result["Triceps"])

    duration = n_samples / samplerate
    # Vector de 0 a duración, con paso 1/samplerate
    time_vector = np.arange(0, duration, 1.0 / samplerate)

    # Aseguramos que la longitud coincida exactamente
    time_vector = time_vector[:n_samples]

    result["tiempo"] = time_vector
    db=pd.DataFrame(data=result)

    return db
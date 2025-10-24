import pandas as pd
import numpy as np # Librería para manejo de vectores y matrices
import matplotlib.pyplot as plt # Librería para graficar
from scipy.signal import butter, filtfilt # Librería para filtrar las señales
from scipy.fft import fft, fftfreq # Librería para la transformada de Fourier

def butter_filter(data, lowcut=None, highcut=None, fs=1000, btype='low', order=4):
    nyq = 0.5 * fs
    if btype == 'low':
        normal_cutoff = highcut / nyq # Se hallan las frecuencias de corte
        b, a = butter(order, normal_cutoff, btype='low') # Se estiman los coeficientes para del filtro para aplicarlos a la señal
    elif btype == 'high':
        normal_cutoff = lowcut / nyq # Se hallan las frecuencias de corte
        b, a = butter(order, normal_cutoff, btype='high')# Se estiman los coeficientes para del filtro para aplicarlos a la señal
    elif btype == 'band':
        low = lowcut / nyq # Se hallan las frecuencias de corte
        high = highcut / nyq # Se hallan las frecuencias de corte
        b, a = butter(order, [low, high], btype='band')# Se estiman los coeficientes para del filtro para aplicarlos a la señal
    elif btype == 'bandstop':
        low = lowcut / nyq # Se hallan las frecuencias de corte
        high = highcut / nyq # Se hallan las frecuencias de corte
        b, a = butter(order, [low, high], btype='bandstop')# Se estiman los coeficientes para del filtro para aplicarlos a la señal
    else:
        raise ValueError("Tipo de filtro no válido")
    return filtfilt(b, a, data)

def plot_fft(signal, fs):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1/fs)

    magnitude = 2.0 / N * np.abs(yf[:N//2]) # su transformada tiene simetría conjugada: la segunda mitad de yf es redundante.
    #El factor 2.0 / N es una normalización para que la amplitud refleje correctamente la escala de la señal original.
    #// es el operador de división entera.

    plt.plot(xf[:N//2], magnitude)
    plt.title("Espectro de Frecuencia (FFT) - Amplitud Real")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud")
    #plt.xlim([0,120])
    plt.grid()
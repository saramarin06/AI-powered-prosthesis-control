# AI-powered-prosthesis-control

# Clasificación de Contracción Muscular a partir de Señales EMG

Este repositorio contiene el código y experimentos para la clasificación de contracción vs. relajación muscular usando señales EMG de bíceps y tríceps.  
Se emplean características temporales y espectrales, reducción de dimensionalidad mediante PCA y varios modelos de machine learning y deep learning, destacando un SVM con kernel RBF en machine learning.


## 1. Propósito del proyecto
Diseñar y desarrollar un sistema inteligente basado en aprendizaje de máquina que analice señales electromiográficas del bíceps y tríceps braquial para detectar su activación permitiendo traducir dicha información en comandos precisos y naturales de control por una prótesis mioeléctrica trans radial.

Proceso objetivo: 
  - Cargar y preprocesar señales EMG.
  - Extraer características (RMS, MAV, VAR, ZC, IMEG, MEANF, MDF, SPECTRAL_ENT).
  - Estandarizar y reducir la dimensionalidad mediante PCA.
  - Entrenar y evaluar modelos de clasificación (DNN, Random Forest, SVM RBF).
- Seleccionar el modelo con mejor equilibrio entre rendimiento global y falsos negativos, pensando en una futura aplicación de control de prótesis.
- Documentar el proceso para que pueda ser reproducido y extendido en trabajos futuros.


## 2. Dependencias

El proyecto está desarrollado en **Python**.

Dependencias principales:

- Python 3.9 / 3.10  
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `tensorflow` (para los modelos DNN)
- `jupyter` o `jupyterlab` (si se usan notebooks)

Para instalar todo con:

```bash
pip install -r requirements.txt














Toda la información relacionada al proyecto la puedes encontrar en la [Wiki](https://github.com/saramarin06/AI-powered-prosthesis-control/wiki/1.-Introducción)

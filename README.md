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


##  Resultados esperados

Dado el diseño del pipeline, el tipo de características extraídas y los modelos seleccionados, se proyectan los siguientes resultados esperados para el sistema de clasificación EMG. Estos representan el comportamiento previsto del modelo una vez ejecutado el entrenamiento, validación y pruebas sobre datos reales o artificiales.


###  1. Separabilidad entre contracción y relajación

Se espera que las características extraídas (RMS, MAV, VAR, IMEG, ZC, MEANF, MDF y entropía espectral) generen una separación detectable entre los estados musculares de **contracción** y **relajación**, especialmente:

- Las características de **amplitud** (RMS, MAV, VAR) deberían mostrar valores significativamente más altos durante la contracción.
- Las características **frecuenciales** y de **complejidad** deberían aportar información complementaria para mejorar la discriminación.

Esto debería reflejarse en histogramas bimodales, dispersión diferenciada y correlaciones coherentes con la fisiología muscular.

---

###  2. Reducción eficiente de dimensionalidad mediante PCA

El Análisis de Componentes Principales (PCA) debería:

- Capturar **80–95%** de la varianza en las primeras 8–15 componentes principales.
- Reducir la redundancia entre características de amplitud, que suelen estar altamente correlacionadas.
- Generar un espacio de características más compacto y estable para los modelos de clasificación.

Se espera observar una clara tendencia en la varianza acumulada, confirmando la utilidad del PCA.

---

###  3. Rendimiento competitivo de los modelos de Machine Learning

Aunque los resultados exactos dependen de los datos finales, se prevé que:

- **SVM con kernel RBF** obtenga el mejor rendimiento general  
  gracias a su habilidad para separar clases no lineales.
- **Random Forest** alcance un desempeño cercano pero con mayor variabilidad.
- **DNN simple (32-16-1)** presente buen rendimiento, pero dependiendo del tamaño del dataset podría requerir más regularización o datos.
  
En términos generales, se proyectan métricas en los siguientes rangos:

- **Accuracy Test:** 0.90 – 0.97  
- **Recall (Clase Contracción):** 0.88 – 0.95  
- **AUC:** 0.95 – 0.99  

Estos rangos representan el comportamiento esperado en datasets EMG de dos clases bien diferenciadas.

---

###  4. Matrices de confusión coherentes con la fisiología EMG

Se espera que el sistema:

- Identifique correctamente la mayoría de las contracciones (TP altos).  
- Mantenga falsos negativos en niveles bajos.  
- Genere pocos falsos positivos, aunque estos pueden ser aceptables en aplicaciones protésicas.

###  5. Curvas ROC con buena separación

Las curvas ROC deberían mostrar:

- Alta sensibilidad a bajas tasas de falso positivo.  
- AUC superior a 0.95 en la mayoría de modelos.  
- Comportamiento similar entre Train, Validación y Test (sin sobreajuste extremo).

---

###  6. Correcta clasificación de muestras artificiales

Dado que las muestras artificiales se generan respetando la distribución estadística real del dataset, se espera que:

- Una muestra artificial de **contracción** sea clasificada como 1 con probabilidad > 0.90  
- Una muestra artificial de **relajación** sea clasificada como 0 con probabilidad < 0.10

Esto confirmaría que el pipeline generaliza adecuadamente incluso con valores simulados.



###  7. Robustez del pipeline para integrar nuevos datos

Debido a la modularidad del preprocesamiento (escalado + PCA + modelo), se espera que el sistema:

- Permita añadir datos nuevos sin reentrenar desde cero.  
- Mantenga coherencia estadística en predicciones de streaming o señales externas.  
- Escale hacia un futuro sistema de control protésico en tiempo real.

---

###  Conclusión proyectada

Basado en la literatura EMG y en la estructura del pipeline, se espera que el proyecto produzca un sistema de clasificación estable, con alto rendimiento general, baja tasa de falsos negativos y capacidad de generalización suficiente para su uso en entornos protésicos reales.





Toda la información relacionada al proyecto la puedes encontrar en la [Wiki](https://github.com/saramarin06/AI-powered-prosthesis-control/wiki/1.-Introducción)

Para instalar todo con:

```bash
pip install -r requirements.txt



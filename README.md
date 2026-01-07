# Exploratory Data Analysis – Adult Census Income

## 📌 Descripción del proyecto
Este proyecto consiste en un **Análisis Exploratorio de Datos (EDA)** realizado sobre el **Adult Census Income Dataset**, disponible en Kaggle. El objetivo del análisis es estudiar cómo distintas características **demográficas, educativas y laborales** se relacionan con el nivel de ingresos de los individuos.

El estudio diferencia entre personas que ganan **≤50K** y **>50K** dólares anuales, centrándose en la identificación de patrones y relaciones entre variables, sin desarrollar modelos predictivos.

---

## ❓ Hipótesis planteadas
Antes de realizar el análisis exploratorio, se formularon las siguientes hipótesis:

- Un mayor nivel educativo aumenta la probabilidad de obtener ingresos superiores a 50K.
- La edad y las horas trabajadas influyen en los ingresos, pero no de forma independiente.
- Existen diferencias de ingresos según sexo, estado civil y ocupación.
- Entre los individuos que presentan *capital gain*, mayores niveles educativos y de ingresos se asocian con mayores ganancias.

---

## 🛠️ Tecnologías utilizadas
- **Lenguaje:** Python  
- **Librerías:**
  - pandas
  - numpy
  - matplotlib
  - seaborn
- **Entorno:** Visual Studio Code

---

## 📁 Estructura del repositorio
├── src/
│   ├── data/
│   │   ├── adult.csv
│   │   └── adult_clean.csv
│   ├── img/
│   │   └── img-01.png
│   ├── notebooks/
│   │   ├── notebook-eda-inicial_limpieza_datos.ipynb
│   │   ├── notebook-eda-analisis-univariante.ipynb
│   │   ├── notebook-eda-analisis-bivariante.ipynb
│   │   └── notebook-eda-analisis-multivariante.ipynb
│   └── utils/
│       ├── bootcampviztools.py
│       └── funciones.py
├── venv/
├── .gitignore
├── main.ipynb
├── Memoria.pdf
├── Presentacion.pdf
└── README.md

---

## ▶️ Instrucciones de reproducción

Para reproducir el análisis exploratorio de datos (EDA), es suficiente con ejecutar el notebook principal del proyecto.

**Instalar las dependencias necesarias:**
pip install pandas numpy matplotlib seaborn

**Ejecutar el análisis:**
- Abrir el archivo main.ipynb
- Ejecutar las celdas en orden

---

## 📊 Principales conclusiones

- El **nivel educativo** es el factor más fuertemente asociado al nivel de ingresos.
- Existen diferencias significativas de ingresos según **sexo** y **estado civil**.
- La **edad** y las **horas trabajadas** muestran una relación positiva con los ingresos, aunque de menor magnitud.
- El **capital gain** se concentra principalmente en individuos con ingresos superiores a 50K, siendo el nivel de ingresos el principal determinante de mayores ganancias.

---

## 📄 Documentación del proyecto

- **Memoria técnica:** `Memoria.pdf`  
- **Presentación:** `Presentacion.pdf`

La memoria técnica documenta de forma detallada el proceso completo de análisis exploratorio, mientras que la presentación resume los principales hallazgos y conclusiones.

---

## 👤 Autor

**Nick Brown**

- GitHub: https://github.com/Nick-Brown-Git 
- LinkedIn: https://www.linkedin.com/in/nick-brown-bb218a3a3/ 

---

## 🎯 Objetivo del proyecto

Este proyecto forma parte de un **portfolio de Data Science**, con el objetivo de demostrar la capacidad para realizar análisis exploratorios rigurosos, interpretar relaciones entre variables socioeconómicas y comunicar resultados de forma clara y estructurada.

# NBA-Scrapping

## Team Members
- [Fabricio Juarez](https://github.com/fabricio63)
- [Steven Wilson](https://github.com/StevenWilson121)

## Descripción
Este proyecto tiene como objetivo crear una herramienta la cual nos permita utilizar la información de equipos de la NBA para realizar análisis estadísticos. 

Con el uso de la librería de Python Beautiful Soup realizamos el *webscrapping* de los [NBA Standings](https://www.basketball-reference.com/leagues/NBA_2020_standings.html). A partir de los datos recopilados se implementó la estructura de datos de un **binary search tree** para encontrar los equipos con los punteos máximos y mínimos de cada categoría, adiconalmente se implementaron tres algoritmos de sorting: **selection sort, bubble sort, quick sort** y dos algoritmos de searching: **linear search y binary search**. Por medio del API creada con Flask un *micro web framework* par Python se desplegaron los datos correspondientes y se utilizó la librería Matplotlib para visualizar algunos datos. 

## Overview
[**Video of API**](images\2020-04-15-05-42-14.mp4)
- Crear un web scraper que extraiga los datos de la página.
- Implementar una estructura de datos para ordenar y acceder los datos de forma eficiente.
- Desarrollar un API en el que se puedan acceder los datos obtenidos.
- Analizar los datos obtenidos.

## Metrics and Reports 
- Baseline: Hacer un baseline del funcionamiento sin la aplicación de conceptos de estructuras de datos y comparar performance luego de implementar estructuras de datos

### Profiling
#### Memory Profiler
Se monitoreó el consumo de memoria utilizando el modulo de python memory_profiler. 
![Imagen Memory Profiler](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfiling.PNG)
![Imagen Memory Profiler Binary Search Tree](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfiling2BstScrapper.jpeg)
![Imagen Memory Profiler Calc](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfilingCalc.jpeg)

### Testing
#### Unittest
Por medio del framework unittest se realizarón los tests a el web scrapper y la lista generada por el mismo. Archivo:[unites.py](https://github.com/fabricio63/NBA-scrapping/blob/API/unites.py)
![Imagen de unit testing](https://github.com/fabricio63/NBA-scrapping/blob/master/images/unit.png)
![Imagen de unit testing Calc](https://github.com/fabricio63/NBA-scrapping/blob/API/images/unitTesting2.jpeg)


#### Jmeter
Utilizando Jmeter se realizó Test HTTP Request con 500 usuarios. Archivo:[JmeterTest.jmx](https://github.com/fabricio63/NBA-scrapping/blob/API/JmeterTest.jmx)


#### **Results Tree**

![Imagen Results Tree](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterResultsTree.PNG)
![Imagen Results Tree 2](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterResultsTree2.jpeg)

#### **Graph Results**

![Imagen Graph Results](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterGraphResults.PNG)
![Imagen Graph Results 2](https://github.com/fabricio63/NBA-scrapping/blob/API/images/JmeterGraphResult2.jpeg)

#### **Summary Report**

![Imagen Summary Results](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterSummaryReport.PNG)

#### Pytest
![Imagen Pytest Sorting](https://github.com/fabricio63/NBA-scrapping/blob/API/images/searchingtest.PNG)
![Imagen Pytest Searching](https://github.com/fabricio63/NBA-scrapping/blob/API/images/sortingTest.PNG)



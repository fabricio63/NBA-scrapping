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

En la primera imágen se evidencia que se utilizaron 88.3 MiB al realizarse sobre el main() del archivo NBA-scrapping/bst.py, donde se realizaba el import de la informacion recopilada y la construcción del Binary Search Tree. 
![Imagen Memory Profiler](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfiling.PNG)

En la segunda imágen se realizó el memory profiling del nuevo archivo que ahora integra la parte de scrapping, construcción del Binary Search Tree y Sorting. Este utiliza 43.3 MiB. 
![Imagen Memory Profiler Binary Search Tree](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfiling2BstScrapper.jpeg)

En la tercera imágen, se realiza el memory profiling de la funcion calculadora('average') la cual es utilizada en la ruta de Data Statistics para encontrar medidas de tendencia central de la información recopilada. 
![Imagen Memory Profiler Calc](https://github.com/fabricio63/NBA-scrapping/blob/API/images/memoryProfilingCalc.jpeg)

### Testing
#### Unittest
Por medio del framework unittest se realizarón los tests a el web scrapper y la lista generada por el mismo. Archivo: [unites.py](https://github.com/fabricio63/NBA-scrapping/blob/API/unites.py)

En el primer test realizado se hizo un assert para comprobar el funcionamiento adecuado del scrapper, para asegurarnos que los datos recopilados fueran iguales a los de la pagina web [NBA Standings](https://www.basketball-reference.com/leagues/NBA_2020_standings.html). En ese mismo test se comprobó el funcionamiento del Binary Search Tree, probando especificamente los máximos y mínimos generados.  
![Imagen de unit testing](https://github.com/fabricio63/NBA-scrapping/blob/master/images/unit.png)

En el segundo grupo de tests se comprobó el funcionamiento de los algoritmos de sorting, selection sort, bubble sort, y quick sort.  
![Imagen de unit testing Calc](https://github.com/fabricio63/NBA-scrapping/blob/API/images/unitTesting2.jpeg)


#### Jmeter
Utilizando Jmeter se realizó Test HTTP Request con 500 usuarios. Archivo: [JmeterTest.jmx](https://github.com/fabricio63/NBA-scrapping/blob/API/JmeterTest.jmx)

#### **Results Tree**

El primer test realizado con Jmeter son HTTP Requests del Home Page del API de webscrapping, este no incluye datos de forma dinámica.
![Imagen Results Tree](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterResultsTree.PNG)

En el segundo test sí se hace el testing de forma dinámica incluyendo tres diferentes archivos CSV para probar el funcionamiento de la pagina en la que se reciben parámetros, Data Statistics. Los errores que ocurrieron durante la prueba son causados por un  end-of-file <EOF>. 
![Imagen Results Tree 2](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterResultsTree2.jpeg)

#### **Graph Results**
Los tests realizados para la primera gráfica no fue de forma dinámica y en promedio el tiempo de respuesta fue menor a 958 ms, se realizaron dos loops de 500 usuarios. 
![Imagen Graph Results](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterGraphResults.PNG)

Los tests realizados para la segunda gráfica fueron de forma dinámica, se realizaron pruebas con 64 usuarios y los teimpos de respuesta fueron menores a 1136 ms.
![Imagen Graph Results 2](https://github.com/fabricio63/NBA-scrapping/blob/API/images/JmeterGraphResult2.jpeg)

#### **Summary Report**

Reporte para el primer conjunto de tests no dinámicos. 
![Imagen Summary Results](https://github.com/fabricio63/NBA-scrapping/blob/API/images/jmeterSummaryReport.PNG)

#### Pytest

Se utilizó el testing *framework* de Pytest para el sorting y searching. 
El algoritmo que tuvo un desempeño superiror fue el quick sort, el cual tienen un Time complexity de (n log(n)), seguido por selection sort con un Time Complexity de O(n^2) y ultimo el bubble sort. 
![Imagen Pytest Searching](https://github.com/fabricio63/NBA-scrapping/blob/API/images/sortingTest.PNG)

En el test realizado para el searching, el algoritmo que tuvo un desempeño superior fue el binary search, el cual tiene un Time Complexity O(log n) a comparación de un O(n) que posee el linear search. 
![Imagen Pytest Sorting](https://github.com/fabricio63/NBA-scrapping/blob/API/images/searchingtest.PNG)




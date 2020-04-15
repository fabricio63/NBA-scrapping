# NBA-scrapping

#Web Scraper para Análisis de Estadísticas del NBA
Autores: Fabricio Juárez 20190361, Steven Wilson 20190361

Este proyecto tiene como objetivo crear una herramienta la cual nos permite utilizar la información de equipos de la NBA para realizar análisis estadísticos. 

Overview
Problem
Difícil de analizar múltiples años de información: Toma mucho tiempo revisar toda la información ya que no está sintetizada. 
Solo se presentan los datos en forma de tabla: En múltiples páginas tales como nba.com o espn.com no hay otra forma de ver los datos más que listados como tabla
Goals
Crear un web scraper que saque los datos de la página.
Implementar una estructura de datos para ordenar y acceder los datos de forma eficiente.
Desarrollar un API en el que se pueda acceder los datos obtenidos.
Analizar los datos obtenidos.
Out of Scope
UI: El enfoque del proyecto no es presentar la data al usuario sino analizar la data.
Tipo de Información: La información que se va a recopilar es únicamente de los equipos y sus resultados.
Fuente de Información: Se realizará web scraping de una página web. 


People and Roles
Fabricio Juárez (Developer)
Steven Wilson (Developer)
Luis Angel Tórtola (Asesor Técnico)



Context

Use Cases 
Queremos lograr:
Acceder a la información: Poder hacerlo pero de una forma más eficiente utilizando una estructura de datos adecuada
Filtrar la información: Que por medio de parámetros se pueda filtrar dependiendo de lo que se quiera encontrar
Imprimir Información: Si se encuentra una información útil que se pueda guardar en un archivo para tenerla almacenada

Assumptions
Desplegar datos: basándose en los datos recopilados se buscará crear graficas relevantes y se auto generarán.
Múltiples usuarios: El API podrá ser accedido por varios usuarios al mismo tiempo. 
Análisis generado: Proveerán una idea general del suceso. 



Proposal 
Web Scraper 
Decidimos que para la parte de web scraping vamos a utilizar beautifulsoup una librería en python que brinda las herramientas necesarias. Nota: dependiendo de resultados de performance puede que decidamos utilizar otras herramientas
User Experience
URL: por medio del URL se podrá acceder información especifica
UI: El UI busca hacer referencia de la data de una forma ordenada y grafica de forma simple. 
Acceso: el acceso será por medio de un URL

API Functionalities
La idea de este API es poder tener un medio por el cual poder interactuar con la información de varias formas entre las cuales las ideas principales que se tienen son:

Pedir la información completa
Pedir información filtrada por parámetros
Pedir que se imprima la información
Que pueda predecir resultados a futuro con la información obtenida (no estamos seguros)
Que por medio de herramientas visuales se pueda graficar o representar la información. (no estamos seguros)
Knobs for Running the Test
Test de optimización de web scraping: crearemos un test para probar las diferentes estructuras de datos y medir cuáles son las más rápidas.
Recopilación de Datos Automatizada: cada cierto tiempo actualizar los datos, y ver si van al día.


Metrics and Reports 
Baseline: Hacer un baseline del funcionamiento sin la aplicación de conceptos de estructuras de datos y comparar performance luego de implementar estructuras de datos
Reportar y documentar: Después de cualquier cambio realizado se documente y se haga un test para ir paso a paso viendo si el cambio representa una mejora o no.
Future Work
Crear predicciones acerca de los partidos: Utilizando la información recopilada generar predicciones acerca de los ganadores/perdedores y el punteo. 
Optimizar UI: crear una página web que le permita al usuario navegar y filtrar la información a su gusto de forma user friendly.
Tasks and Timeline 
Fechas pueden variar dependiendo de tareas o fechas asignadas por catedrático
Feb 25: revisión de PRD
Marzo 20: Web Scraper extraiga la información correcta
Abril 01: API con las funcionalidades básicas para testing
Abril 05: entrega segundo parcial
Abril 25: Implementación del resto de funcionalidades o mejora de las anteriores y la estructura de datos.
Mayo 5: Entrega del proyecto terminado.

Criterios de aceptación del proyecto
El proyecto en general consiste en entregar un programa que haga web scraping de una página que contenga información de partidos pasados y exista una forma de interactuar con ellos por medio de un API.

Especificamente estos criterios son:
Que el web scraper de la página funcione correctamente.
Implementación de la estructura de datos correcta para eficientizar el proceso de filtrado vrs otro tipo de estructuras.
Un API que contenga los endpoints adecuados en los que se pueda imprimir toda la información, que se pueda filtrar y que se pueda guardar la información que se encontró en un archivo.

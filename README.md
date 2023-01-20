
![Asset_1](/srv/MiawTV/1x/Asset_1.png)

# API ETL 
### para Análisis de Datos en Películas y Series


## Descripción:

Esta API permite a los analistas de datos acceder fácilmente a un conjunto de datos limpio y transformado de información de películas y series. La API proporciona varios **Endpoints** para filtrar y recuperar información del conjunto de datos, como *obtener el número de ocurrencias de una palabra específica en los títulos de películas o series en una plataforma determinada*, o *obtener el título y la puntuación de la película o serie con la segunda mejor puntuación en una plataforma determinada*.

El conjunto de datos utilizado para esta API se obtuvo del conjunto de datos de **IMDb** y se limpió y transformó utilizando la libreria **Python** *pandas*. La API está construida utilizando el framework **FastAPI** y se realiza su deploy en la plataforma **Deta**.

### ENDPOINTS
La API tiene los siguientes endpoints:

-  **/**: *un endpoints sencillo que devuelve un mensaje de saludo*
-  **/items/{item_id}**: *un endpoints que devuelve el ID del elemento pasado como parámetro*
-  **/word_count/{platform}/{word}**: *un endpoints que devuelve el número de ocurrencias de la palabra pasada como parámetro en los títulos de películas y series en la plataforma pasada como parámetro*
-  **/score_count/{platform}/{score}/{year}**: *un endpoints que devuelve el número de películas o series en la plataforma pasada como parámetro que tienen una puntuación mayor que la puntuación pasada como parámetro y fueron lanzadas en el año pasado como parámetro*
-  **/second_score/{platform}**: *un endpoints que devuelve el título y la puntuación de la película o serie con la segunda mejor puntuación en la plataforma pasada como parámetro*
-  **/get_longest/{plataform}/{duration_type}/{year}**: *un endpoints que devuelve el título, la duración en minutos y el tipo de duración de la película o serie más larga en la plataforma pasada como parámetro, con el tipo de duración pasado como parámetro y que fue lanzada en el año pasado como parámetro*
-  **/rating/{platform}/{year}**: *un endpoint que devuelve el título, la puntuación y el género de las películas o series con una puntuación mayor a 8 en la plataforma pasada como parámetro y que fueron lanzadas en el año pasado como parámetro*

### Deployment
La API se despliega en la plataforma **Deta**, una plataforma sin servidor para construir y desplegar aplicaciones de aprendizaje automático y procesamiento de datos.

### Tecnologías y Frameworks
- Python 3.9
- FastAPI
- pandas
- Deta (para despliegue)

### Uso
Para usar la API, envía una solicitud GET al endpoint deseado con los parámetros adecuados. Por ejemplo, para obtener el número de ocurrencias de la palabra "love" en los títulos de películas y series en Netflix, envía una solicitud GET a /word_count/netflix/love.

## Comenzando:
1. **Clonar el repositorio**: git clone https://github.com/YOUR_USERNAME/ETL_API.git
2. **Instalar las dependencias**: pip install -r requirements.txt
3. **Ejecutar la API: uvicorn main**:app --reload
4. **Probar la API**: enviando una solicitud **GET** a uno de los endpoints con los parámetros adecuados. Por ejemplo, para obtener el número de ocurrencias de la palabra *"amor"* en los títulos de películas y series en Netflix, enviar una solicitud **GET** a http://localhost:8000/word_count/netflix/amor.
5. **Desplegar la API**: en la plataforma **Deta** siguiendo las instrucciones de la *documentación de **Deta***.

**Nota**: *El archivo clean_data.csv debe estar en la misma carpeta que el archivo main.py*

## Prerequisitos:
- Una cuenta en Deta (https://deta.sh/)
- Git (https://git-scm.com/)
- Python 3.9+
- Administrador de paquetes pip

Antes de comenzar, asegúrate de tener una cuenta en **Deta** y tener **Git** e **instalado Python** en tu computadora. También necesitarás tener el **administrador de paquetes pip** instalado para instalar las dependencias necesarias para la API.

## Instalación:
- **Clona el repositorio**: git clone https://github.com/TU_USUARIO/ETL_API.git
- **Navega al directorio del proyecto**: *'cd ETL_API'*
- **Instala las dependencias necesarias**: *'pip install -r requirements.txt'*
- **Asegúrate de que el archivo**: *clean_data.csv* esté en la misma carpeta que el archivo *main.py*
- **Ejecuta la API**: *'uvicorn main:app --reload'*
- **Prueba la API**: enviando una solicitud **GET** a uno de los endpoints con los parámetros apropiados. Por ejemplo, para obtener el número de ocurrencias de la palabra *"love"* en los títulos de películas y series de Netflix, envía una solicitud **GET** a http://localhost:8000/word_count/netflix/love.
- **Para desplegar la API**: en la plataforma **Deta**, sigue las instrucciones en la *documentación de Deta*.

**Nota**: Se recomienda usar un *entorno virtual* para la instalación y ejecución de la API.

## Deployment:
###Para desplegar esta API en la plataforma Deta, siga los siguientes pasos###:

1. Asegúrese de tener una cuenta en **Deta** (https://deta.sh/) y de haber seguido las instrucciones de configuración en su sitio web.
2. Clone este repositorio en su máquina local: git clone https://github.com/TU_USUARIO/ETL_API.git
3. Navegue hasta el directorio del proyecto: *cd ETL_API*
4. Instale las dependencias necesarias: *pip install -r requirements.txt*
5. Asegúrese de que el archivo *clean_data.csv* esté en la misma carpeta que el archivo *main.py.*
6. Inicie sesión en **Deta** desde la línea de comandos: *deta login*
7. Cree un nuevo proyecto en **Deta**: *deta new*
8. Despliegue la API en el proyecto creado: *deta deploy*
9. Pruebe la API enviando una solicitud **GET** a uno de los endpoints con los parámetros apropiados usando una herramienta como *Postman* o *cURL*. Por ejemplo, para probar el endpoint */word_count/{platform}/{word}*, envíe una solicitud **GET** a la **URL** del endpoint proporcionada por **Deta** y verifique que la respuesta sea correcta.
10. Repita los pasos anteriores para cada endpoint para asegurarse de que todos estén funcionando correctamente.

**Nota**: es recomendable utilizar un *entorno virtual* para el despliegue de esta API.

## Corriendo los tests:
### Pruebas con uvicorn:
- **Ejecuta la API localmente utilizando uvicorn**: *uvicorn main:app --reload*
- **Prueba la API**: enviando una solicitud **GET** a uno de los puntos finales con los parámetros apropiados utilizando una herramienta como *Postman* o con *cURL*. Por ejemplo, para probar el endpoint */word_count/{platform}/{word}*, envía una solicitud **GET** a http://localhost:8000/word_count/netflix/love y verifica que la respuesta sea correcta.
- **Pruebas**: de los endpoints con **uvicorn**:

- **Repite**: los pasos del paso anterior para cada punto final para asegurarte de que todos estén funcionando correctamente.
- **Presta atención**: a los parámetros y a la respuesta.

### Pruebas con Deta:
- **Despliega la API**: en la plataforma **Deta** siguiendo las instrucciones de la documentación de **Deta**.
- **Prueba la API**: enviando una solicitud **GET** a uno de los endpoints con los parámetros apropiados utilizando una herramienta como Postman o cURL. Por ejemplo, para probar el punto final /word_count/{platform}/{word}, envía una solicitud GET a la URL del punto final proporcionada por Deta y verifica que la respuesta sea correcta.
- **Pruebas**: de los endpoints con **Deta**:

- **Repite**: los pasos del paso anterior para cada punto final para asegurarte de que todos estén funcionando correctamente.
- **Presta atención**: a los parámetros y a la respuesta.

**Nota**: Se recomienda utilizar herramientas de prueba automatizadas como *Pytest* para hacer que el proceso de prueba sea más eficiente."

## Proceso ETL:
El archivo *clean_data.csv* utilizado por esta API se creó a través de un proceso ETL (Extract, Transform, Load) utilizando la biblioteca de **Python** *pandas*.

1. **Extracción**: El primer paso fue obtener los datos de la base de datos IMDb.

2. **Transformación**: Una vez obtenidos los datos, se limpian y transforman para que sean más fáciles de analizar. Esto incluye eliminar columnas innecesarias, reemplazar valores faltantes y crear nuevas columnas a partir de los datos existentes.

3. **Carga**: Finalmente, los datos limpios y transformados se cargan en un archivo CSV para su fácil acceso a través de la API.

Durante este proceso, se eliminan los datos que no cumplen ciertos criterios. Esto incluye entradas duplicadas y entradas que no contienen cierta información, como un título o un año de lanzamiento. Los datos restantes luego se organizan y reorganizan para facilitar la recuperación y filtrado de información. Esto incluye cambiar el nombre de las columnas a nombres más descriptivos y crear nuevas columnas para albergar valores calculados como la calificación promedio.

Una vez que se crea el archivo clean_data.csv, se puede usar como fuente de datos para la API. Se puede almacenar en una base de datos u otro sistema de almacenamiento de datos para su uso en producción, o se puede mantener en el sistema de archivos del proyecto para su uso en desarrollo y pruebas.

## Creación de las Queries:
Para crear las queries para los endpoints de la API, se utiliza la biblioteca *pandas* de **Python**. Esta biblioteca proporciona herramientas para filtrar, organizar y analizar datos en un DataFrame.

Para crear una query, se carga el archivo *clean_data.csv* en un DataFrame y se utilizan las funciones de filtrado de pandas para seleccionar solo las filas que cumplen con los criterios específicos de cada endpoint. Por ejemplo, para el endpoint */score_count/{platform}/{score}/{year}*, se filtran las filas donde la columna "platform" es igual al parámetro "platform", la columna "score" es mayor que el parámetro "score" y la columna "release_year" es igual al parámetro "year".

Una vez seleccionadas las filas apropiadas, se utilizan las funciones de agregación de pandas para contar el número de filas en el DataFrame filtrado. En este caso, para el endpoint */score_count/{platform}/{score}/{year}*, se cuenta el número de filas en el DataFrame filtrado.

Las queries se utilizan en los endpoints para devolver la información solicitada al usuario. Es importante asegurarse de que las queries sean eficientes y estén correctamente construidas para garantizar que los endpoints respondan rápidamente y devuelvan los resultados correctos.

## Autores: 
- Fernando Blas De Olano para 'Proyecto Individual 1' *cohorte_6* **HENRY** 

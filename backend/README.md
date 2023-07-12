![image](https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/assets/129927386/fabc1388-3526-4da0-ae0e-daa84722d136)<div align="center">
  <img src=https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Logo2.png?raw=true?alt="texto alternativo">
</div>

## Integrantes:
- Fabryzzio Jossue Meza Torres
- Fernando Alonso Usurin Arias 
- Josue Nehemias Velo Poma

## Introduccion
<p align="justify">El proyecto en cuestión es un servicio web diseñado para satisfacer la creciente demanda en el mercado educativo de cursos y asesorías en programación. Con el fin de garantizar la calidad de la capacitación, se cuenta con un equipo altamente calificado de instructores profesionales que imparten cursos de una amplia gama de temas, desde conceptos fundamentales hasta técnicas especializadas. Además, la plataforma ofrece una experiencia de usuario atractiva, con una interfaz amigable y fácil de usar, y garantiza una compra segura y fiable a través de múltiples opciones de pago. El servicio también proporciona información detallada sobre los cursos y las asesorías para que los usuarios puedan tomar decisiones informadas.La plataforma cuenta con un formulario seguro de registro y un sistema de compra confiable para garantizar la seguridad de los datos personales y financieros de los usuarios. Además, la empresa emplea una base de datos Postgres altamente segura para almacenar y proteger la información de sus clientes.</p>

## Objetivos Principales:
- Desarrollar un servicio web de alta calidad, atractivo, efectivo y facil de usar.
- Obtener y almacenar correctamente los datos de interes para nuestra empresa
- Segmentar nuestro servicio web de forma estrategica para estructurar de manera correcta nuestro contenido, para que sea altamente entendible y relevante para nuestros clientes.
- Tener un diseño llamativo, con la inclusión estratégica de videos e imágenes, lo cual permita atraer y mejorar la experiencia del usuario en nuestro servicio.
- Implementar un modelo de negocio rentable y sostenible para maximizar los ingresos y garantizar la rentabilidad de la empresa.

## Misión: 
<p align="justify">Ofrecer una plataforma web de alta calidad, segura y confiable, con cursos y asesorías en programación impartidos por instructores profesionales, para satisfacer las necesidades educativas de nuestros usuarios.</p>

## Visión: 
<p align="justify">Ser líderes en el mercado educativo de programación, innovando constantemente nuestra plataforma para brindar la mejor experiencia de usuario y ser reconocidos por nuestra calidad y rentabilidad sostenible.</p>

## Información acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos:

### __Vue__:
<p align="justify">Vue es un framework de JavaScript de código abierto utilizado para construir interfaces de usuario interactivas y de una sola página (SPA, por sus siglas en inglés). Fue creado por Evan You y lanzado por primera vez en 2014. Vue se centra en ser simple, flexible y escalable, lo que lo hace muy popular entre los desarrolladores web.</p>

### __Flask__:
<p align="justify">Es un micro-framework de Python utilizado para desarrollar aplicaciones web. Es ligero y tiene una amplia gama de extensiones disponibles. En el proyecto de TechTribe, Flask se emplea para crear el servidor web que aloja la plataforma de cursos y asesorías en programación. Permite a los usuarios interactuar con la plataforma, realizar compras seguras, registrarse y acceder a los cursos y asesorías. Flask es importante porque facilita la creación de aplicaciones web eficientes y escalables.</p>

### __Flask-SQLAlchemy__:
<p align="justify">Es una extensión de Flask que proporciona una capa de abstracción sobre SQLAlchemy, una biblioteca de mapeo objeto-relacional para Python. Permite a los desarrolladores crear y administrar fácilmente bases de datos en sus aplicaciones web de Flask. En el proyecto de TechTribe, Flask-SQLAlchemy se emplea para almacenar y proteger de manera segura la información de los clientes,sus tarjetas de credito,los trabajadores, los cursos ofrecidos en la plataforma. También ayuda a estructurar y acceder de manera más eficiente a los datos en la aplicación. En resumen, Flask-SQLAlchemy es una herramienta clave para garantizar la calidad y seguridad de la información en el servicio web de TechTribe.</p>

### __UUID__:
<p align="justify">Universally Unique Identifier es una biblioteca de Python que se utiliza para generar identificadores únicos para objetos. En el proyecto de TechTribe, se utiliza UUID para generar identificadores únicos para cada objeto que se almacena en la base de datos a través de Flask-SQLAlchemy. Esto garantiza la unicidad de los registros y evita problemas de duplicidad en la base de datos.</p>

### __Datetime__:
<p align="justify">Es un módulo de Python que permite trabajar con fechas y tiempos. En Flask se puede utilizar para registrar la fecha y hora de creación y modificación de una entrada en una base de datos. En el proyecto de TechTribe, datetime se emplea en combinación con SQLAlchemy para mantener un registro de la fecha de creación y modificación de las clases que se emplean en el servidor web.</p>

### __HTML__:
<p align="justify">Hypertext Markup Language es el lenguaje de etiquetas estándar utilizado para crear páginas web. Flask utiliza HTML para crear la estructura de las páginas web que se muestran al usuario. En el proyecto de TechTribe, HTML se utiliza para diseñar las plantillas de las páginas web y para renderizar la información dinámica que se obtiene de la base de datos.</p>

### __CSS__:
<p align="justify">Cascading Style Sheets es un lenguaje de diseño utilizado para dar estilo y formato a páginas web. Su empleo es importante para mejorar la apariencia visual y la experiencia del usuario en el sitio web. En el proyecto TechTribe, CSS se emplea para personalizar el aspecto y la estructura de la plataforma, asegurando la consistencia y la legibilidad de la información en todo momento.</p>

### __JavaScript__:
<p align="justify">Es un lenguaje de programación de alto nivel utilizado en aplicaciones web para agregar interactividad y mejorar la experiencia del usuario. En el proyecto TechTribe, se emplea para implementar funcionalidades dinámicas en la interfaz del usuario y para realizar validaciones en formularios. Su importancia radica en permitir la creación de aplicaciones web más interactivas y ricas en funcionalidades para el usuario.</p>

### __werkzeug.security__:
<p align="justify">proporciona funciones para la generación segura de contraseñas y tokens, así como para la verificación de contraseñas y tokens en aplicaciones web desarrolladas con Flask. Esto ayuda a fortalecer la seguridad y proteger la información confidencial.</p>

### __hashlib__:
<p align="justify">La librería "hashlib" en Python proporciona funciones para calcular funciones hash criptográficas.</p>

### __random__:
<p align="justify">Es una librería estándar de Python que proporciona funciones relacionadas con la generación de números aleatorios</p>

### __psycopg2__:
<p align="justify">Es un adaptador de base de datos PostgreSQL para el lenguaje de programación Python.</p>

### __traceback__:
<p align="justify">Es una librería estándar de Python que proporciona funciones para obtener y manipular información de seguimiento de excepciones. </p>

### __sys__:
<p align="justify">Es una librería estándar de Python que proporciona acceso a variables y funciones específicas del intérprete de Python.</p>

### __json__:
<p align="justify">Es una librería estándar que proporciona funciones para trabajar con datos en formato JSON (JavaScript Object Notation). </p>

## Componentes:
### ContentBox.vue:
<p align="justify">Es responsable de mostrar y organizar el contenido principal de la página web. Proporciona una caja de contenido que se utiliza para mostrar información relevante sobre los cursos de programación en línea. Contiene texto, imágenes, enlaces y otros elementos multimedia para proporcionar una experiencia interactiva al usuario. Este componente generalmente se utiliza en varias secciones de la página web para presentar diferentes tipos de contenido.</p>

### Inicio.vue:
<p align="justify">Representa la página de inicio de la página web. Este componente contiene una introducción a la plataforma de cursos de programación en línea, destacando sus características clave y beneficios.Incluye texto descriptivo, imágenes atractivas, llamadas a la acción y enlaces a secciones importantes de la página web. El componente 'Inicio' es esencial para captar la atención de los visitantes y proporcionarles una visión general del contenido y las oportunidades que ofrece el sitio web.</p>



### Menu.vue:
<p align="justify">Es responsable de mostrar y manejar el menú de navegación de la página web. Proporciona una estructura visual para los diferentes enlaces y secciones del sitio. El menú usa una lista de elementos o botones que permiten al usuario acceder a diferentes partes de la página web. El componente Menu.vue facilita la navegación del usuario y mejora la usabilidad del sitio web.</p>

### NewUser.vue:
<p align="justify">Es una sección o formulario que permite a los usuarios nuevos registrarse en la página web para acceder a los cursos de programación en línea. Este componente incluye campos para que el usuario ingrese su nombre, apellido, correo electrónico y su contraseña. También contiene botones para enviar el formulario de registro y proporcionar mensajes de confirmación o error. El componente 'NewUser.vue' es fundamental para permitir que nuevos usuarios se unan a la plataforma y accedan a los cursos.</p>

### TextMenu.vue:
<p align="justify">Es un elemento de texto utilizado en el menú de navegación de la página web. Proporciona etiquetas o descripciones breves para cada enlace o sección del menú. Estos textos suelen ser concisos y descriptivos, permitiendo al usuario identificar rápidamente la función o el contenido asociado con cada enlace. El componente 'TextMenu.vue' se utiliza para mejorar la legibilidad y la comprensión del menú de navegación.</p>

### TextSec.vue:
<p align="justify">Se utiliza para mostrar texto descriptivo en secciones específicas de la página web.Contiene párrafos de texto, títulos, subtítulos u otros elementos relacionados con la información que se muestra en esa sección en particular. Este componente se utiliza para proporcionar contexto y detalles adicionales sobre el contenido presentado en la página web. El componente 'TextSec.vue' mejora la comprensión y la comunicación de la información al usuario.</p>


## Vistas:
### FormRegis.vue:
<p align="justify">Representa la vista de registro en TechTribe. Esta vista contiene un formulario en el que los usuarios pueden ingresar la información requerida para crear una cuenta en el sitio web. El formulario incluye campos como nombre, apellido, email y contraseña. También puede contener botones para enviar el formulario y cancelar el proceso de registro. La vista FormRegis.vue permite a los usuarios registrarse y acceder a los cursos y funcionalidades de la página web.</p>

### HomeView.vue:
<p align="justify">Representa a la página de inicio de TechTribe. Esta vista contiene una presentación general del sitio web, destacando sus características, beneficios y cursos disponibles.Incluye imágenes, texto descriptivo, animaciones, llamadas a la acción y secciones destacadas. La vista 'HomeView.vue' tiene como objetivo principal captar el interés de los visitantes y brindarles una visión general del contenido y las oportunidades que ofrece el sitio web.</p>

### Signln.vue:
<p align="justify">Representa a la página de inicio de sesión de TechTribe. Esta vista contiene un formulario en el que los usuarios pueden ingresar sus credenciales de inicio de sesión. También incluye registrarse si el usuario no tiene una cuenta. La vista 'Signln.vue' permite a los usuarios autenticarse en el sitio web y acceder a su perfil y cursos.</p>

### VistaAses.vue:
<p align="justify">Es la sección en donde los usuarios pueden acceder a servicios de asesoría. Esta vista proporciona información detallada sobre los servicios de asesoría disponibles. También proporciona información sobre los costos o tarifas asociadas. La vista 'VistaAsesoria.vue' permite a los usuarios obtener apoyo adicional y orientación personalizada para su aprendizaje.</p>

### VistaContend.vue:
<p align="justify">Es la sección en donde se muestra el contenido detallado de cada curso en específico. Esta vista proporciona información detallada sobre cada curso. La vista 'VistaContend.vue' permite a los usuarios explorar y sumergirse en el contenido específico de un curso en particular.</p>

### VistaCursos.vue:
<p align="justify">Representa a una sección que muestra una lista de los cursos disponibles. En esta vista se presentan los cursos de forma organizada, mostrando detalles como el título, descripción, nivel de dificultad, precio, duración y un video introductorio de cada curso. La vista 'VistaCursos.vue' brinda a los usuarios una visión general de los cursos disponibles y les permite acceder a la información detallada de cada uno.</p>

### VistaProfs.vue:
<p align="justify">Representa a una sección que muestra información y perfiles de los profesores o instructores de la empresa TechTribe. Esta vista proporciona detalles sobre la experiencia, áreas de especialización, logros y tal vez testimonios de los profesores. También puede incluye opciones para contactar o enviar consultas a los profesores. La vista 'VistaProfs.vue' permite a los usuarios conocer y familiarizarse con los profesores y obtener información sobre sus credenciales y competencias en la enseñanza de los cursos de programación.</p>


## El nombre del script a ejecutar para iniciar la base de datos con datos:
serverproject.py

## Host:
localhost

## Puerto:
5432

## Manejo de errores HTTP:
### __Errores en el Servidor__:
<p align="justify">Cuando un sitio web devuelve un código de estado 500, generalmente se muestra una página de error genérica al usuario para indicar que ha ocurrido un problema técnico y que el servidor no pudo procesar la solicitud.</p>
#### __Errores de Exitoso en nuestro sitio web__:
 ***Ejemplo 1:***
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error1_500_ejemplo1.png?raw=true" alt="texto alternativo" width="400">
<div align="left">


### __Errores en el Cliente__:
<p align="justify">El código de estado 400 generalmente indica un problema con la sintaxis de la solicitud realizada.</p>

#### __Errores de Cliente en nuestro sitio web__:
***Ejemplo 1:***
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error1_400_ejemplo1.png?raw=true" width="400">

 ***Ejemplo 2:***
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error2_400_ejemplo2.png?raw=true" width="400">
  
 ***Ejemplo 3:***
 <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error3_400_ejemplo3.png?raw=true" alt="texto alternativo" width="400">

   
 ***Ejemplo 4:***
 <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error4_400_ejemplo4.png?raw=true" alt="texto alternativo" width="400">

  ***Ejemplo 5:***
 <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/backend/static/images/Error5_400_ejemplo5.png?raw=true" alt="texto alternativo" width="400">


### __Redirección__:
<p align="justify">El código de estado 300 se utiliza principalmente para casos en los que un recurso ha cambiado de ubicación de forma permanente o temporalmente.</p>

### __Exitoso__:
<p align="justify">Cuando un servidor devuelve un código de estado 200, significa que la solicitud del cliente ha sido recibida, entendida y procesada correctamente, y el resultado se incluye en la respuesta.</p>
  
 #### __Errores de Exitoso en nuestro sitio web__:
  ***Ejemplo 1:***
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error2_200_ejemplo1.png?raw=true" alt="texto alternativo" width="400">
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_200.png?raw=true" alt="texto alternativo" width="400">
   <p align="justify">En estas líneas de código, se genera un hash de la contraseña del usuario, se crea un nuevo usuario en la base de datos con los datos proporcionados y se devuelve un objeto JSON con el ID del nuevo usuario, un estado de éxito y un mensaje indicando que el usuario se creó exitosamente, con un código de estado HTTP 200.</p>
  
  ***Ejemplo 2:***
  <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error2_200_ejemplo2.png?raw=true" alt="texto alternativo" width="400">
  <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error2_400.png?raw=true" alt="texto alternativo" width="400">
   <p align="justify">La función "login" gestiona el inicio de sesión en una aplicación web. Verifica si la solicitud es de tipo "POST", obtiene el correo electrónico y la contraseña proporcionados y consulta la base de datos en busca del usuario. Si se encuentra y las contraseñas coinciden y cumplen los requisitos, devuelve un objeto JSON con un mensaje de inicio de sesión exitoso y código HTTP 200.</p>

***Ejemplo 3:***
  <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error3_200.png?raw=true" alt="texto alternativo" width="400">
   <p align="justify">Este código intenta crear una nueva tarjeta en la base de datos con la información proporcionada, confirma la transacción y devuelve una respuesta JSON indicando que la transacción se ha realizado correctamente.</p>
    
### __Informacional__:
<p align="justify">El código de estado 100, específicamente, se utiliza para indicar al cliente que el servidor ha recibido la solicitud inicial y está esperando que el cliente envíe datos adicionales antes de continuar con el proceso.</p>
    
## Cómo ejecutar el sistema (Deployment scripts):
1. git clone git@github.com:Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP.git 
2. Correr en el terminal para instalar todas las dependencias:
pip install -r requirements.txt
3. Correr el codigo python principal
python serverproject.py

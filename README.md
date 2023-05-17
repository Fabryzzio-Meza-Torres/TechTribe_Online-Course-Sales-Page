<div align="center">
  <img src=https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Logo2.png?raw=true alt="texto alternativo">
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

### __Flask__:
<p align="justify">Es un micro-framework de Python utilizado para desarrollar aplicaciones web. Es ligero y tiene una amplia gama de extensiones disponibles. En el proyecto de TechTribe, Flask se emplea para crear el servidor web que aloja la plataforma de cursos y asesorías en programación. Permite a los usuarios interactuar con la plataforma, realizar compras seguras, registrarse y acceder a los cursos y asesorías. Flask es importante porque facilita la creación de aplicaciones web eficientes y escalables.</p>

### __Flask-SQLAlchemy__:
<p align="justify">Es una extensión de Flask que proporciona una capa de abstracción sobre SQLAlchemy, una biblioteca de mapeo objeto-relacional para Python. Permite a los desarrolladores crear y administrar fácilmente bases de datos en sus aplicaciones web de Flask. En el proyecto de TechTribe, Flask-SQLAlchemy se emplea para almacenar y proteger de manera segura la información de los clientes,sus tarjetas de credito,los trabajadores, los cursos ofrecidos en la plataforma. También ayuda a estructurar y acceder de manera más eficiente a los datos en la aplicación. En resumen, Flask-SQLAlchemy es una herramienta clave para garantizar la calidad y seguridad de la información en el servicio web de TechTribe.</p>

### __Flask-Migrate__:
<p align="justify">Es un plugin para Flask que proporciona herramientas para facilitar la gestión de las migraciones de la base de datos en aplicaciones web Flask que utilizan SQLAlchemy. Es importante porque permite la actualización y modificación de los modelos de la base de datos sin tener que eliminar y crearla nuevamente, lo cual puede ser costoso en términos de tiempo y recursos. En el proyecto TechTribe, Flask-Migrate se utiliza para realizar migraciones en la base de datos PostgreSQL de la empresa.</p>

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
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_500_ejemplo1.png?raw=true" alt="texto alternativo" width="400">
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_500.png?raw=true" alt="texto alternativo" width="400">
   <p align="justify">En caso de que ocurra una excepción, se imprime la información de la excepción y se realiza un rollback en la sesión de la base de datos. Se devuelve un objeto JSON indicando el fallo en la creación del usuario, con un mensaje de error y un código de estado HTTP 500.</p>
  
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error2_500.png?raw=true" alt="texto alternativo" width="400">
   <p align="justify">El código devuelve un código de estado HTTP 500, que es un código de error interno del servidor. Esto indica que ha ocurrido un error interno en el servidor al procesar la transacción.</p>

### __Errores en el Cliente__:
<p align="justify">El código de estado 400 generalmente indica un problema con la sintaxis de la solicitud realizada.</p>

#### __Errores de Cliente en nuestro sitio web__:
***Ejemplo 1:***
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_400_ejemplo1.png?raw=true" alt="texto alternativo" width="400">
  
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_400.png?raw=true" alt="texto alternativo" width="400">
</div>
<p align="justify">La función "register" valida y procesa el registro de usuarios en una aplicación web. Retorna un objeto JSON con el estado de éxito o fallo del registro, así como los mensajes de error, si los hay, en un código de estado HTTP 400 en caso de errores.</p>
  
 ***Ejemplo 2:***
<p align="justify"></p>
  
  
 ***Ejemplo 3:***
  
 <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_400_ejemplo1.png?raw=true" alt="texto alternativo" width="400">
  
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error1_400.png?raw=true" alt="texto alternativo" width="400">
</div>
<p align="justify">La función "register" valida y procesa el registro de usuarios en una aplicación web. Retorna un objeto JSON con el estado de éxito o fallo del registro, así como los mensajes de error, si los hay, en un código de estado HTTP 400 en caso de errores.</p>

  
  
  
<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error3_400.png?raw=true" alt="texto alternativo" width="400">
</div>
<p align="justify">La salida de este código es una respuesta JSON con dos elementos: "success" y "message". El valor de "success" es "False", lo que indica que el inicio de sesión no fue exitoso debido a que las credenciales proporcionadas son inválidas.</p>

<div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error4_400.png?raw=true" alt="texto alternativo" width="400">
</div>
<p align="justify">La salida de este código es una respuesta JSON con dos elementos: "success" y "message". El valor de "success" es "False", lo que indica que el inicio de sesión no fue exitoso porque el usuario no fue encontrado en el sistema.</p>
  
 <div align="left">
  <img src="https://github.com/Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP/blob/TechTribe/static/images/Error5_400.png?raw=true" alt="texto alternativo" width="400">
</div>
<p align="justify">La salida de este código es una respuesta JSON con dos elementos: "success" y "message".Si alguna de las variables "creditcard_number", "expiration_date" o "password" es nula o está vacía, significa que uno o más campos requeridos no se proporcionaron en la solicitud.</p>


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

### __Informacional__:
<p align="justify">El código de estado 100, específicamente, se utiliza para indicar al cliente que el servidor ha recibido la solicitud inicial y está esperando que el cliente envíe datos adicionales antes de continuar con el proceso.</p>

## Cómo ejecutar el sistema (Deployment scripts):
1. git clone git@github.com:Fabryzzio-Meza-Torres/TechTribe_ProyectoDBP.git 
2. Correr en el terminal para instalar todas las dependencias:
pip install -r requirements.txt
3. Correr el codigo python principal
python serverproject.py            

# Mi Proyecto de Django/Python "ProyectoWeb"

Este es un proyecto de Django y Python que tiene como función core la de ser una "tienda" de un local de hamburguesas del cual soy uno de los titulares. Puedes utilizar este README como punto de partida para documentar tu proyecto.

Esta compuesto por un proyecto principal y aplplicaciones con funcionalidades diferentes

Project:ProyectoWeb
  |_App:Autenticacion. Es donde se hace el majejo de usuarios y sesiones. 
  |_App:Blog. Es un Blog para que los usuarios posteen su experiencia. 
  |_App:Carrito. Es el Carrito de compras de la Web.
  |_App:Contacto. Maneja la mensajeria para que el usuario pueda contactar a la empresa.
  |_App:Pedidos. Es la App que administra los pedidos generados por los usuarios. 
  |_App:ProyectoWebApp. Es la App que administra al resto de las Apps.
  |_App:Servicios. Acá es donde se administran los servicios que se ofrecen. 
  |_App:Tienda. Es la app que administra los productos que se comercializan.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu entorno de desarrollo:

asgiref==3.7.2
beautifulsoup4==4.12.2
blinker==1.6.2
cachetools==5.3.1
certifi==2023.7.22
channels==4.0.0
charset-normalizer==3.2.0
click==8.1.6
colorama==0.4.6
contourpy==1.1.1
cycler==0.11.0
distlib==0.3.7
Django==4.2.7
django-ckeditor==6.3.2
django-cors-headers==3.13.0
django-crispy-forms==2.0
django-environ==0.9.0
django-js-asset==2.1.0
django-restframework==0.0.1
django-storages==1.13.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.0
et-xmlfile==1.1.0
filelock==3.12.2
Flask==2.3.2
Flask-MySQL==1.5.2
fonttools==4.42.1
google-api-core==2.11.1
google-api-python-client==2.99.0
google-auth==2.23.0
google-auth-httplib2==0.1.1
googleapis-common-protos==1.60.0
httplib2==0.22.0
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
kiwisolver==1.4.5
lxml==4.9.3
MarkupSafe==2.1.3
matplotlib==3.8.0
numpy==1.25.2
oauth2client==4.1.3
openpyxl==3.1.2
packaging==23.1
pandas==2.0.3
persona==0.0.1
Pillow==9.3.0
platformdirs==3.10.0
plotly==5.15.0
protobuf==4.24.3
psycopg2==2.9.5
pyasn1==0.5.0
pyasn1-modules==0.3.0
pydata==1.0.0
PyDrive==1.3.1
pygame==2.5.1
PyJWT==2.8.0
PyMySQL==1.1.0
pyparsing==3.1.1
python-dateutil==2.8.2
python-dotenv==1.0.0
pytz==2023.3
PyYAML==6.0.1
requests==2.31.0
rsa==4.9
six==1.16.0
soupsieve==2.4.1
sqlparse==0.4.4
tenacity==8.2.2
tzdata==2023.3
uritemplate==4.1.1
urllib3==1.26.16
virtualenv==20.24.2
Werkzeug==2.3.6


Nota: Revisar documento "requirements.txt" para mayor información. 


# Configuración del Entorno

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/tuproyecto.git
   cd tuproyecto

2. Crea un entorno virtual (se recomienda virtualenv):
   
    python -m venv venv

3. Activa el entorno virtual:

     En Windows:
     venv\Scripts\activate

     En macOS y Linux:
     source venv/bin/activate

4. Instala las dependencias del proyecto:

    pip install -r requirements.txt

5. Realiza las migraciones de la base de datos:

     python manage.py migrate

6.  Carga datos iniciales (opcional):

    python manage.py loaddata data.json

## Ejecución del Proyecto

Para ejecutar el proyecto, utiliza el siguiente comando:

  python manage.py runserver

## El proyecto estará disponible en http://localhost:8080/.


## Uso   

    Esta aplicación web te permite realizar compras en línea de una manera sencilla y segura. A continuación, te proporcionamos un paso a paso sobre cómo utilizarla:

    1. Registro o Inicio de Sesión

    Si eres un usuario nuevo, debes registrarte en la plataforma. Si ya tienes una cuenta, simplemente inicia sesión.

    - Haz clic en "Registro" si eres un nuevo usuario.
    - Proporciona la información requerida, como tu nombre, dirección de correo electrónico y una contraseña segura.
    - Haz clic en "Iniciar Sesión" si ya tienes una cuenta y proporciona tu correo electrónico y contraseña.

    2. Navegación por la Tienda

    Una vez que hayas iniciado sesión, puedes navegar por la tienda en busca de productos. Utiliza las siguientes funciones:

    - Barra de navegación: Encuentra diferentes categorías de productos.
    - Barra de búsqueda: Busca productos específicos por nombre o palabra clave.
    - Filtros: Refina tus búsquedas por precio, marca, tamaño, etc.

    3. Agregar Productos al Carrito

    Cuando encuentres un producto que desees comprar:

    - Haz clic en el producto para ver los detalles.
    - Selecciona la cantidad que deseas comprar.
    - Haz clic en el botón "Agregar al Carrito".

    4. Revisar el Carrito

    Para revisar los productos que has agregado al carrito:

    - Haz clic en el icono del carrito en la esquina superior derecha.
    - Verás una lista de los productos en tu carrito.
    - Puedes ajustar las cantidades, eliminar productos o aplicar cupones de descuento si los tienes.

    5. Proceso de Compra

    Cuando estés listo para comprar:

    - Haz clic en el botón "Proceder al Pago" en el carrito.
    - Proporciona la información de envío y método de pago.
    - Revisa tu pedido y confirma la compra.

    6. Confirmación de Compra

    Después de completar la compra, recibirás una confirmación de pedido en tu correo electrónico. También podrás ver los detalles del pedido en tu cuenta.

    7. Seguimiento de Pedidos

    Puedes hacer un seguimiento de tus pedidos en tu cuenta, donde encontrarás información sobre el estado de entrega.

    ¡Listo! Ahora estás listo para comenzar a utilizar la aplicación web de compras en línea. 
    
    ¡Disfruta de tus compras en línea!



## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

  1. Crea un fork del proyecto en GitHub.
  2. Clona tu fork localmente.
  3. Crea una nueva rama para tu contribución.
  4. Realiza tus cambios y asegúrate de seguir las guías de estilo.
  5. Haz un pull request a este repositorio.


## Licencia

Este proyecto está bajo la licencia LICENSE.txt. Consulta el archivo LICENSE para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, puedes contactarme en moroni_sebastian@yahoo.com.ar
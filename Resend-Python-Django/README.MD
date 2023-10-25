### Enviar email con Resend usando Python & Django

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar Djando desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        python -m pip install Django
        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Crear el proyecto con Djando

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

5.  Crear mi primera aplicación en Django

        python manage.py startapp enviar_email

6.  Instalar nuestra aplicación (enviar_email) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'enviar_email',
        ]

7.  Crear una clase en models.py la cual reprtesentara mi tabla en BD, preferiblemente los modelos
    se declaran en singular

        class Contacto(models.Model):
            nombre_cliente = models.CharField(max_length=100)
            email_cliente = models.EmailField()
            mensaje_cliente = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
            updated = models.DateTimeField(auto_now_add=False, auto_now=True)

            class Meta:
                db_table = "contactos"
                ordering = ['-created_at']

8.  Crear y correr las migraciones

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

9.  Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

10. Crear el archivo urls.py en la aplicación (envia_email)

        from django.urls import path
        from . import views

                urlpatterns = [
                    path('', views.inicio, name='inicio'),
                    path('recibe-formulario-para-enviar-email/', views.procesar_envio_email,
                        name='procesar_envio_email'),
                ]

11. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('envia_email.urls')),
        ]

12. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

13. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

14. Correr archivo requirement.txt

        pip install -r requirements.txt

#### Resultado final

#####Formulario para registrar Empleado
![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/registrar-empleado-con-django-crud-urian-viera.png)

##### Lista de Empleados

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/lista-de-empleados-crud-django-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍

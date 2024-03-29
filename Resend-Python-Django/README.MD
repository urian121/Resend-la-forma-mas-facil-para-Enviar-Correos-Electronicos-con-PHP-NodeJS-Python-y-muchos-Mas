### Enviar email con Resend desde Python & Django

#### Crear mi entorno virtual

        python -m venv env

#### Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

#### Instalar Django ya dentro del entorno virtual.

        pip install Django

#### Crear el proyecto con Django

        `django-admin startproject project_core .`

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

#### Crear mi primera aplicación en Django

        python manage.py startapp enviar_email

#### Instalar nuestra aplicación (enviar_email) ya creada en el proyecto, en el archivo settings.py

        INSTALLED_APPS = [
    		----,
    		'enviar_email',
        ]

#### Opcional, Crear una clase en models.py

        class Contacto(models.Model):
            nombre_cliente = models.CharField(max_length=100)
            email_cliente = models.EmailField()
            mensaje_cliente = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
            updated = models.DateTimeField(auto_now_add=False, auto_now=True)

            class Meta:
                db_table = "contactos"
                ordering = ['-created_at']

#### Crear el archivo urls.py en la aplicación (envia_email)

        from django.urls import path
        from . import views

                urlpatterns = [
                    path('', views.inicio, name='inicio'),
                    path('recibe-formulario-para-enviar-email/', views.procesar_envio_email,
                        name='procesar_envio_email'),
                ]

#### Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto

    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('envia_email.urls')),
        ]

#### Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

#### Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos

    estaticos (css, js, imagenes, etc..)

#### Crear y correr las migraciones

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

#### Correr el proyecto existente 😊 😉

        pip install -r requirements.txt    ->Instalar todas las dependecias del proyecto
        python manage.py migrate         -> Correr migraciones
        python3 manage.py runserver ->En Mac
    	python manage.py runserver ->En Windows
        Revisar la consola y visitar la URL http://127.0.0.1:8000

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/enviar-email-desde-Resend-con-Node-y-Express-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍

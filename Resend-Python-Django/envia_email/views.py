from django.shortcuts import render, redirect
from . models import Contacto
from django.contrib import messages  # Para usar mensajes flash

# Importante importando Resend
import resend

resend.api_key = ""


def inicio(request):
    return render(request, 'index.html')


def procesar_envio_email(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        email_cliente = request.POST.get('email_cliente')
        mensaje_cliente = request.POST.get('mensaje_cliente')

        contact = Contacto(
            nombre_cliente=nombre_cliente,
            email_cliente=email_cliente,
            mensaje_cliente=mensaje_cliente,
        )
        contact.save()

        parametrosdeEnvio = {
            "from": "Python & Django <pythondjango@resend.dev>",
            "to": ["urian1213viera@gmail.com"],
            "subject": "Python & Django",
            "html": f"""<p>Recibiendo email desde Python y Django 😲</p>
                    <p style="color:#24cf5f; font-size:22px; font-weight: bold;">Datos del Cliente:<p>
                    <p>Cliente: {nombre_cliente}</p>
                    <p>Email: {email_cliente}</p>
                    <p>Asunto: {mensaje_cliente}</p>
                """,
        }

        r = resend.Emails.send(parametrosdeEnvio)
        print(r)

        messages.success(
            request, f"Felicitaciones el correo fue enviado correctamente  😉")
        return redirect('inicio')

    return redirect('inicio')

# Importando  flask y algunos paquetes
from flask import Flask, render_template, request, redirect, url_for
# Importando Resend
import resend


resend.api_key = "re_gQYDfsg9_DY6dVbrbi1yM6nTHSyuSKNkc"

# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

app.secret_key = '97110c78ae51a45afcb3380af008f90b23a5d1616bf19bc29098105da20fe'


@app.route('/', methods=['GET'])
def inicio():
    return render_template('public/index.html')


# Buscar empleado
@app.route('/enviar-email-resend-phyton-flask', methods=['POST'])
def formulario_contacto():
    if request.method == "POST":
        nombre_cliente = request.form["nombre_cliente"]
        email_cliente = request.form["email_cliente"]
        mensaje_cliente = request.form["mensaje_cliente"]

        params = {
            "from": "Python  & Fask <pythonflaskg@resend.dev>",
            "to": ["urian1213viera@gmail.com"],
            "subject": "Python & Flask",
            "html": f"""Recibeindo email desde Python y Flask 😲
                    Datos del formulario:
                    <p>Cliente: {nombre_cliente}</p>
                    <p>Email: {email_cliente}</p>
                    <p>Asunto: {mensaje_cliente}</p>
                """,
        }

        r = resend.Emails.send(params)
        print(r)

    return redirect(url_for('inicio'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)

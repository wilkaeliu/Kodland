from flask import Flask, request
import random


app = Flask (__name__)

facts_list = [
    "La dependencia tecnológica puede llevar a la pérdida de habilidades básicas.",
    "El uso excesivo de la tecnología puede afectar la salud mental y física.",
    "La tecnología puede crear una brecha entre generaciones.",
    "La dependencia tecnológica puede afectar la productividad y la concentración.",
    "El uso constante de dispositivos electrónicos puede afectar la calidad del sueño."]

@app.route('/', methods=['GET', 'POST'])
def index():
    texto = request.form.get("address")
    if texto == "sixseven":
        return "", 302, {'Location': '/ADRESS'}
    return "<h1>Bienvenido a la página de hechos sobre la dependencia tecnológica</h1><a href='/facts'>Ver hechos</a><form method='POST'><input type='text' name='address' placeholder='Ingrese su dirección'><input type='submit' value='Enviar'></form>"

@app.route("/facts")
def get_facts():
    return f"<h1>Hecho sobre la dependencia tecnológica</h1><p>{random.choice(facts_list)}</p><a href='/'>volver a la pagina principal</a>"

@app.route("/ADRESS")
def function():
    return "<h1>SEIS SIETEEEEEEEEEEEEEEEEE</h1>"
app.run(debug=True)
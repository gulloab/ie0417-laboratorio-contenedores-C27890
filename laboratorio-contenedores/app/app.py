from flask import Flask
import os

app = Flask(**name**)

@app.route("/")
def home():
mensaje = os.environ.get("MENSAJE", "Hola desde Flask en Docker")
return f""" <h1>{mensaje}</h1> <p>Esta aplicación se está ejecutando dentro de un contenedor.</p>
"""

@app.route("/info")
def info():
return {
"app": "Laboratorio de contenedores",
"curso": "IE0417",
"tema": "Docker"
}

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)

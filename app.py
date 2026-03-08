import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    fecha = datetime.now().strftime("%d/%m/%Y")
    mensaje = os.environ.get('MENSAJE', '¡Hola desde Azure App Servicee yuju!')
    return f"""
    <h1>{mensaje}</h1>
    <p>Esta es mi primera aplicación en PaaS con Python en Azure</p>
    <p>Fecha: {fecha}</p>
    """

if __name__ == '__main__':
    app.run()

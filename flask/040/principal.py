# Ejemplo de publicación en flask de una gráfica generada siguiendo el 
# mismo proceso que se seguiríamos para crearla en un jupyter notebook 

# Paquetes requeridos
# sudo apt install python3-tk
# python3 -m venv venv
# source venv/bin/activate
#    pip3 install matplotlib
#    pip3 install pandas
#    pip3 install numpy
#    pip3 install flask

# python3 main.py
# http://localhost:5000/plot.png

import io

from flask import Flask, Response, request, render_template
from flask.helpers import url_for
from werkzeug.utils import secure_filename

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('carga.html')

@app.route('/uploader', methods = ['POST'])
def cargar():
    if request.method == 'POST':
        archivo = request.files['file']
        nuevo_nombre = secure_filename('/static/'+archivo.filename)
        archivo.save(nuevo_nombre)
        df = pd.read_csv(nuevo_nombre)

        df = df.groupby('provincias')['edades','hijos','mascotas'].median().reset_index()
        df.plot(figsize=(20, 20), title='Gráfico de ejemplo', kind='bar', stacked=False)
        output = io.BytesIO()
        plt.legend()
        plt.savefig(output, format='png')
        output.seek(0)
        plot_url = base64.b64encode(output.getvalue()).decode()
        return render_template('resultados.html', 
                                tables=[df.head().to_html(classes='data')], 
                                titles=df.columns.values, 
                                shape=df.shape,
                                figura = plot_url)



if __name__ == '__main__':
   app.run(debug = True)
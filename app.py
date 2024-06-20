from flask import flash, Flask, send_file,session, render_template, request,Response ,jsonify, redirect, url_for
from bson import json_util
from controllers.database import Conexion as dbase
from datetime import datetime,timedelta #* Importacion de manejo de tiempo
from flask import jsonify
from reportlab.pdfgen import canvas # *pip install reportlab este es para imprimir reportes
from reportlab.lib.pagesizes import letter #* pip install reportlab 
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer ,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet ,ParagraphStyle
from routes.empleados import empleados
from routes.herramientas import  herramientas
from routes.prestamo import prestamo
from routes.reporte import reporte

# ! Puntos para instalar pip install flask-paginate flask pymongo reportlab pip install babel
# ! Codigo para que se ejecute 

db = dbase()
app = Flask(__name__)
app.secret_key = 'herramientas14526'
app.config['UPLOAD_FOLDER'] = 'E:/Joshua Benites Construccion/Herramientas/static/img'

# * Vista de Ingreso al sistema 
@app.route('/',methods=['GET','POST'])
def run():
    return render_template('index.html')


#* Este es para cerrar la sesion 
@app.route('/logout')
def logout():
    # Elimina el usuario de la sesión si está presente
    session.pop('username', None)
    return redirect(url_for('index'))


#* Vista Ingreso de admin y usuarios
@app.route('/index',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        usuario = request.form['user']
        password = request.form['contraseña']
        usuario_fo = db.admin.find_one({'user':usuario,'contraseña':password})
        if usuario_fo:
            session["username"]= usuario
            return redirect(url_for('reporte.v_reporte'))
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for('index'))
    else:
        return render_template('index.html')
    

# *Codigo de ingreso de empleados
app.register_blueprint(empleados)

# * Codigo de ingreso de herramientas
app.register_blueprint(herramientas)

# * Codigo de ingreso de prestamos
app.register_blueprint(prestamo)

# * Codigo de ingreso de reportes

app.register_blueprint(reporte)

# *  Este es para manejo de errores
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    return render_template('404.html', message=message), 404


if __name__ == '__main__':
    app.run(debug=True, port=4000)

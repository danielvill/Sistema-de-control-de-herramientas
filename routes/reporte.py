from flask import Blueprint, render_template, request, flash, session, redirect, url_for,send_file
from controllers.database import Conexion as dbase
from modules.reporte import Reporte
from pymongo import MongoClient
from reportlab.pdfgen import canvas # *pip install reportlab este es para imprimir reportes
from reportlab.lib.pagesizes import letter #* pip install reportlab 
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer ,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet ,ParagraphStyle


db = dbase()

reporte = Blueprint('reporte', __name__)





# *Visualizar reporte
@reporte.route("/admin/reporte")
def v_reporte():
    if 'username' not in session:
        flash("Inicia sesion con tu usuario y contraseña")
        return redirect(url_for('reporte.index'))
    reporte = db['reporte'].find()
    return render_template('admin/reporte.html', reporte=reporte)


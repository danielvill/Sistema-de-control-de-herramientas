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


# Para visualizar reportes 
def generar_pdf_vistacompleta(datos):
    doc = SimpleDocTemplate("reporte.pdf", pagesize=letter)
    story = []

    # Define un estilo con texto centrado
    styles = getSampleStyleSheet()
    left_aligned_style = styles['Heading3']
    left_aligned_style.alignment = 0  # 0 = TA_LEFT

    # Agrega la imagen
    imagen = Image('static/img/logo.jpg', width=100, height=100)
    imagen.hAlign = 'CENTER'
    story.append(imagen)
    #story.append(Spacer(1, 12))

    from datetime import datetime
    fecha_hora = datetime.now().strftime("Documento generado %H:%M")
    fecha_hora_parrafo = Paragraph(fecha_hora , left_aligned_style)
    fecha_hora_parrafo.alignment = 1  # 2 = TA_RIGHT
    story.append(fecha_hora_parrafo)
    # Agrega un salto de línea
    #story.append(Spacer(1, 12))
    
    # Agrega el título
    title = Paragraph("<h3>JC</h3>", left_aligned_style)
    story.append(title)

    # Agrega un salto de línea
    #story.append(Spacer(1, 12))

    title2 = Paragraph("<h1>Reporte de prestamos</h1>", left_aligned_style)
    story.append(title2)

    title3 = Paragraph("<h3>El Oro Machala</h3>", left_aligned_style)
    story.append(title3)
    story.append(Spacer(1, 12))
    
    contenido_style = ParagraphStyle(
    'contenido',
    fontName='Helvetica',
    fontSize=12,
    alignment=0  # Alineación izquierda
    )

    # Prepara los datos para la tabla
    data = [["Empleado","Cedula","Codigo","Herramienta","Prestamo","Entrega", "Comentario"]]  # Encabezados

    # Dentro del bucle para preparar los datos de la tabla
    for dato in datos:
        row = [
            Paragraph(dato['empleado_p'], contenido_style),  # Usa el estilo personalizado
            Paragraph(str(dato.get('cedula_p', 0)), contenido_style),
            Paragraph(str(dato.get('codigo_p', 0)), contenido_style),
            Paragraph(str(dato.get('nombreh_p', 0)), contenido_style),
            Paragraph(str(dato.get('fecha_p', 0)), contenido_style),
            Paragraph(str(dato.get('fecha_pf', 0)), contenido_style),
            Paragraph(str(dato.get('comentario', 0)), contenido_style)
        ]
        data.append(row)
    
    ancho_celda=100

    longitud_empleado = pdfmetrics.stringWidth("empleado_p", "Helvetica", 17)
    longitud_cedula = pdfmetrics.stringWidth("cedula_p", "Helvetica", 17)
    longitud_codigo = pdfmetrics.stringWidth("codigo_p", "Helvetica", 17)
    longitud_herramienta = pdfmetrics.stringWidth("nombreh_p", "Helvetica", 17)
    longitud_prestamo = pdfmetrics.stringWidth("fecha_p", "Helvetica", 17)
    longitud_entrega = pdfmetrics.stringWidth("fecha_pf", "Helvetica", 17)
    longitud_comentario = pdfmetrics.stringWidth("comentario", "Helvetica", 17)
    
    # Ajusta el tamaño de fuente según el ancho de la celda
    tamaño_fuente = 12
    if longitud_empleado > ancho_celda:
        tamaño_fuente = 10
        contenido_style.fontSize = tamaño_fuente  #
    

    # Ajusta el ancho de las columnas según las longitudes máximas
    colWidths = [longitud_empleado, longitud_cedula, longitud_codigo, longitud_herramienta, longitud_prestamo, longitud_entrega, longitud_comentario]
    
    # Crea la tabla con el tamaño de fuente actualizado
    table = Table(data, colWidths=colWidths,hAlign='LEFT')
    # Formatea la tabla
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), tamaño_fuente),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))

    # Agrega la tabla al documento
    story.append(table)

    doc.build(story)


@reporte.route('/admin/reporte/re_vistacompleta', methods=['GET'])
def re_vistacompleta():
    doc = SimpleDocTemplate("reporte.pdf", pagesize=letter)
    story = []

    # Define un estilo con texto centrado
    styles = getSampleStyleSheet()
    left_aligned_style = styles['Heading3']
    left_aligned_style.alignment = 0  # 1 = TA_CENTER

    # Agrega la imagen
    imagen = Image('static/img/logo.jpg', width=100, height=100)
    imagen.hAlign = 'CENTER'
    story.append(imagen)
    story.append(Spacer(1, 12))

    from datetime import datetime
    fecha_hora = datetime.now().strftime("Documento generado %H:%M")
    fecha_hora_parrafo = Paragraph(fecha_hora , left_aligned_style)
    fecha_hora_parrafo.alignment = 1  # 2 = TA_RIGHT
    story.append(fecha_hora_parrafo)
    # Agrega un salto de línea
    
    # Agrega el título
    title = Paragraph("<h3>JC</h3>", left_aligned_style)
    story.append(title)

    # Agrega un salto de línea
    

    title2 = Paragraph("<h1>Reporte de prestamos</h1>", left_aligned_style)
    #story.append(title2)

    # Agrega otro salto de línea
    
    title3 = Paragraph("<h3>El Oro Machala</h3>", left_aligned_style)
    story.append(title3)
    story.append(Spacer(1, 12))

    # Prepara los datos no como tabla
    client = request.args.get('cedula_p', default=None, type=str)

    if client is not None:
        clie = db['reporte'].find({'cedula_p': client})
    else:
        clie = db['reporte'].find()
    
    generar_pdf_vistacompleta(clie)
    
    return send_file('reporte.pdf', as_attachment=True)

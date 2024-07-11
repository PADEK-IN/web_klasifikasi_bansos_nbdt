from flask import Blueprint, render_template, session, redirect
from app.server.routes.index import index_controller
# import pdfkit
# import os

Index = Blueprint('index', __name__)

# Tambahkan jalur eksekutor wkhtmltopdf
# path_to_wkhtmlpdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmlpdf)

@Index.route('/')
def index():
    if 'login' in session:
        result = index_controller.count()
        return render_template("pages/index/index.jinja", name=session['name'], count=result)
    else:
        return redirect('/login')

@Index.route('/preview')
def profile():
    return render_template("pages/index/template_pdf.jinja")
        
    
# @Index.route('/download', methods=['GET', "POST"])
# def profile():
#     if request.method == "GET":
#         return render_template("pages/index/template_pdf.jinja")
#     if request.method == "POST":
#         # Menerima HTML dari permintaan POST
#         html_content = request.get_data(as_text=True)
        
#         # Memasukkan HTML ke dalam template dan merendernya
#         rendered_html = render_template("pages/index/template_pdf.html", data=html_content)
        
#         # PDF options
#         options = {
#             "orientation": "landscape",
#             "page-size": "A4",
#             "margin-top": "1.0cm",
#             "margin-right": "1.0cm",
#             "margin-bottom": "1.0cm",
#             "margin-left": "1.0cm",
#             "encoding": "UTF-8",
#         }
        
#         # Build PDF from rendered HTML 
#         pdf = pdfkit.from_string(rendered_html, False, configuration=pdfkit_config, options=options)
        
#         # Mendapatkan nama file untuk menyimpan PDF
#         filename = "output.pdf"

#         # Menyimpan PDF ke direktori sementara
#         with open(filename, 'wb') as f:
#             f.write(pdf)
        
#         # Mengembalikan file PDF sebagai respon
#         return send_file(os.path.abspath(filename), as_attachment=True)

# @Index.route('/profile')
# def profile():
#     return render_template("pages/index/profile.jinja", name="Admin")
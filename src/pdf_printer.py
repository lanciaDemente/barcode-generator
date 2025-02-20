import os, pdfkit, base64
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

pdf_lib_path = os.environ['PDF_LIB_PATH']

def print_pdf(dir_content):
    pdf_content = '<h1>Barcode generati</h1><br>'

    for filename in dir_content:
        f = os.path.join('barcodes', filename)
        
        if os.path.isfile(f) and filename[-3:] == 'png':
            with open(f, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                image_value = 'data:image/png;base64,' + encoded_string
                
                data = filename.replace('.png', '').split('_')

                pdf_content += f"""
                    <h2>{data[0]}</h2>
                    <p>Taglia: {data[1]}</p>
                    <p>Lotto: {data[2]}</p>
                    <br>
                    <img src='{image_value}'>
                    <br>
                    <br>
                    <br>
                    <br>
                    <br>
                """
    
    fname = datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
    config = pdfkit.configuration(wkhtmltopdf=pdf_lib_path)
    pdfkit.from_string(pdf_content, 'outputs\{0}.pdf'.format(fname), configuration=config)
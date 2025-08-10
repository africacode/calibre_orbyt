import os
import time
import requests
from email.message import EmailMessage
import smtplib
import subprocess

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')

ORBYT_USER = os.getenv('ORBYT_USER')
ORBYT_PASS = os.getenv('ORBYT_PASS')

def download_pdf_orbyt(publication, date_str):
    """ Descarga el PDF completo de Orbyt dado el periódico y la fecha """
    session = requests.Session()
    login_url = 'http://quiosco.orbyt.es/'  # URL real puede variar
    # Aquí debes añadir el código exacto para hacer login, esto es ejemplo
    login_data = {
        'username': ORBYT_USER,
        'password': ORBYT_PASS,
    }
    resp = session.post(login_url, data=login_data)
    resp.raise_for_status()

    pdf_url = f"https://quiosco.{publication}.orbyt.es/epaper/pdf/{date_str}.pdf"
    r = session.get(pdf_url)
    if r.status_code == 200:
        filename = f"{publication}_{date_str}.pdf"
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f"Descargado {filename}")
        return filename
    else:
        print(f"No se pudo descargar PDF {pdf_url}, status {r.status_code}")
        return None

def convert_recipe_to_epub(name, recipe_path):
    epub_file = f"{name}.epub"
    subprocess.run(['ebook-convert', recipe_path, epub_file], check=True)
    return epub_file

def send_email(files):
    msg = EmailMessage()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "Tus periódicos del día"

    for file in files:
        with open(file, 'rb') as f:
            if file.endswith('.pdf'):
                subtype = 'pdf'
                maintype = 'application'
            elif file.endswith('.epub'):
                subtype = 'epub+zip'
                maintype = 'application'
            else:
                maintype = 'application'
                subtype = 'octet-stream'
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Correo enviado!")

def main():
    today = time.strftime('%Y_%m_%d')

    files_to_send = []

    # Descarga PDFs Orbyt
    for pub in ['elmundo', 'expansion']:
        pdf_file = download_pdf_orbyt(pub, today)
        if pdf_file:
            files_to_send.append(pdf_file)

    # Convierte los otros periódicos a EPUB (modifica según tengas recetas)
    recipes = {
        'elpais': 'recipes/elpais.recipe',
        'financialtimes': 'recipes/financial_times.recipe',
        # añade aquí otras recetas que quieras
    }

    for name, path in recipes.items():
        try:
            epub_file = convert_recipe_to_epub(name, path)
            files_to_send.append(epub_file)
        except subprocess.CalledProcessError:
            print(f"Error convirtiendo {name}")

    # Envía correo con todos los archivos
    send_email(files_to_send)

if __name__ == '__main__':
    main()

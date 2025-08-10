import os
import subprocess
import smtplib
from email.message import EmailMessage

# Variables de entorno
ORBYT_USER = os.getenv('ORBYT_USER')
ORBYT_PASS = os.getenv('ORBYT_PASS')
FROM_EMAIL = os.getenv('FROM_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

# Recetas para epub (web)
recipes_epub = {
    'El_Pais': 'recipes/elpais.recipe',
    'FT': 'recipes/financial_times.recipe',
    'WSJ': 'recipes/wsj_news.recipe',
}

# Recetas pdf directo orbyt
pdfs_orbyt = {
    'El_Mundo': 'recipes/elmundo_orbyt.recipe',
    'Expansion': 'recipes/expansion_orbyt.recipe',
}

def download_epubs():
    epubs = []
    for name, recipe_path in recipes_epub.items():
        epub_filename = f"{name}.epub"
        print(f"Generando EPUB {epub_filename} desde {recipe_path}...")
        subprocess.run(['ebook-convert', recipe_path, epub_filename], check=True)
        epubs.append(epub_filename)
    return epubs

def download_pdfs_orbyt():
    pdfs = []
    for name, recipe_path in pdfs_orbyt.items():
        pdf_filename = f"{name}.pdf"
        print(f"Generando PDF {pdf_filename} desde {recipe_path} (Orbyt)...")
        # Aquí asumimos que el recipe sabe sacar el pdf directo (o usar wget/curl)
        # Por simplicidad llamamos ebook-convert, pero puede ser otra cosa
        subprocess.run(['ebook-convert', recipe_path, pdf_filename], check=True)
        pdfs.append(pdf_filename)
    return pdfs

def send_email(attachments):
    msg = EmailMessage()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = 'Tus periódicos del día'

    for filename in attachments:
        with open(filename, 'rb') as f:
            if filename.endswith('.pdf'):
                maintype, subtype = 'application', 'pdf'
            elif filename.endswith('.epub'):
                maintype, subtype = 'application', 'epub+zip'
            else:
                maintype, subtype = 'application', 'octet-stream'
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Correo enviado.")

def main():
    attachments = []
    attachments += download_epubs()
    attachments += download_pdfs_orbyt()
    send_email(attachments)

if __name__ == '__main__':
    main()

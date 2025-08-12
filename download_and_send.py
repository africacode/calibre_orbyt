import os
import smtplib
from email.message import EmailMessage

def send_to_kindle(email_kindle, email_sender, password, file_path):
    print(f"Enviando {file_path} a {email_kindle}...")
    msg = EmailMessage()
    msg["Subject"] = "News Update"
    msg["From"] = email_sender
    msg["To"] = email_kindle
    msg.set_content("Adjunto tienes el último número.")

    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)

    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_sender, password)
        smtp.send_message(msg)

    print("Enviado.")

if __name__ == "__main__":
    # Variables de entorno Railway
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_KINDLE = os.getenv("EMAIL_KINDLE")

    # Enviar todos los PDFs y ePubs generados en /app/output
    output_dir = "/app/output"
    for filename in os.listdir(output_dir):
        if filename.endswith(".pdf") or filename.endswith(".epub") or filename.endswith(".mobi"):
            file_path = os.path.join(output_dir, filename)
            send_to_kindle(EMAIL_KINDLE, EMAIL_SENDER, EMAIL_PASSWORD, file_path)

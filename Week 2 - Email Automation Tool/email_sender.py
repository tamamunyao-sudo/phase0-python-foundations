import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config

def send_email(client, pdf_path):
    message = MIMEMultipart()

    message["From"] = config.config["EMAIL"]
    message["To"] = client["Email"]
    message["Subject"] = "INVOICE"

    html = """
    <html>
    <body>
    <p>Hello {client_name},</p>
    <p>Your invoice for {service} is attached.</p>
    <p>Thank you for choosing Tama Automation Agency.</p>
    <p>Regards,</p>
    <p>Collins Tama Munyao,</p>
    </body>
    </html>
    """

    html = html.format(
        client_name=client["Client"],
        service=client["Service"],
    )

    message.attach(MIMEText(html, "html"))

    attachment = MIMEBase("application", "octet-stream")
    with open(pdf_path, "rb") as pdf_file:
        attachment.set_payload(pdf_file.read())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=pdf_path)
    message.attach(attachment)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(config.config["EMAIL"], config.config["APP_PASSWORD"])
            smtp.sendmail(config.config["EMAIL"], client["Email"], message.as_string())
            return True
    except Exception as e:
        print(e)
        return False
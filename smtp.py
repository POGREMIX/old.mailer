import smtplib
import config
from email.mime.multipart import MIMEMultipart


def sendEMail(smtp_auth_key, mailFrom, mailTo, title, message):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = mailFrom
    msg['To'] = mailTo
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message)

    server = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
    server.ehlo()
    server.starttls()

    try:
        server.login(mailFrom, smtp_auth_key)
    except Exception as e:
        raise Exception("Ошибка логирования", e)

    try:
        server.sendmail(mailFrom, mailTo, msg.as_string().encode('utf-8'))
    except Exception as e:
        raise Exception("Ошибка отправки", e)
    finally:
        server.quit()

import os
import smtplib
from email.message import EmailMessage
from senhas import password_hide

EMAIL_ADRESS = "Insira o e-mail que fará o envio aqui"
EMAIL_PASSWORD = password_hide

msg = EmailMessage()
msg['Subject'] = "Titúlo do e-mail aqui"
msg['From'] = "Insira o e-mail que fará o envio aqui"
msg['To'] = "Insira o endereço de e-mail que irá receber a mensagem aqui"
msg.set_content('Insira a mensagem a ser enviada aqui')


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

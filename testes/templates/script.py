import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_destino = 'guilhermedec6@gmail.com'
senha = 'guilher1254322111'

msg = MIMEMultipart()
msg['From'] = email_destino
msg['To'] = email_destino
msg['Subject'] = 'Feedback de usuário'

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
email = input('Digite o e-mail: ')
feedback = input('Digite o feedback: ')

body = f"""
Nome: {nome}
Idade: {idade}
E-mail: {email}
Feedback: {feedback}
"""

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_destino, senha)
text = msg.as_string()
server.sendmail(email_destino, email_destino, text)
server.quit()

print('E-mail enviado com sucesso!')

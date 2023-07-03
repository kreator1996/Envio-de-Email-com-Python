# bibliotecas utilizadas
from email.message import EmailMessage
import smtplib
import re
import csv

# Variáveis para o email e senha
EMAIL = 'seu_email'
SENHA = 'sua_senha' 

# Função que extrai os endereços e email e salva em um lista (pode ser um .csv por exemplo)
def extrai_emails():
    emails_extraidos = []
    with open(file=r'caminho\do\arquivo.csv', mode='r', encoding='utf8') as arquivo:
        csv.reader(arquivo)
        texto = arquivo.read()
        emails = re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', texto)
        for email in emails:
            emails_extraidos.append(email)
        return emails_extraidos

# função para enviar o email (chama a lib smtplib)
def enviar_email(destino):
    msg = EmailMessage()
    msg['Subject'] = 'Envio de Email com smtplib'
    msg['From'] = EMAIL
    msg['To'] = destino
    msg.set_content('1...2...3... Testando...')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, SENHA)
        smtp.send_message(msg)
    print('Email enviado com sucesso!')
        
# Chamada das funções
emails = extrai_emails()
enviar_email(emails)
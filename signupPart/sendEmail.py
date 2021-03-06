import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import time
import random


def Send_Email(receiver_address):
    start = time()
    confirm_key = random.randint(10e5, 10e6)
    mail_content = f'''Hello,
    This is  simple mail form AP MediaPlayer. Verification code is: {confirm_key}.
    Thank You'''

    #The mail addresses and password
    sender_address = 'agha.mehdi2020@gmail.com'
    sender_pass = '0021639450@'
    # receiver_address = 'mahdi.sabour@aut.ac.ir'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'AP MediaPlayer Confirmation Code.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        end = time()
        print('Mail Sent: ', end - start)
        return confirm_key

    except:
        return 0





if __name__ == "__main__":
    Send_Email('mahdi.sabour@aut.ac.ir')
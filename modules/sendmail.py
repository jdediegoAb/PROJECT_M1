import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
useremail=''
def send_email(email_recipient, email_subject, email_message, attachment_location = ''):
   
    email_sender = "j.dediego.abad@gmail.com"
    msg = MIMEMultipart()
    msg["From"] = email_sender
    msg["To"] = useremail
    msg["Subject"] = 'Monuments'
    msg.attach(MIMEText(email_message, "plain"))
    
    if attachment_location != '':
        files = ['./monuments_list.csv',
                './monuments_map.html']
        for a_file in files:
            attachment = open(a_file, 'rb')
            filename = os.path.basename(a_file)
            part = MIMEBase('application','octet-stream')
            part.set_payload(attachment.read())
            part.add_header('Content-Disposition',
                            'attachment',filename=a_file[2:20])
            encoders.encode_base64(part)
            msg.attach(part)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('j.dediego.abad@gmail.com', 'jflrrgbeswffddyw')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True
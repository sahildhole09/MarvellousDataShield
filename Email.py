############################################################
#
# Importing Required Libraries
#
############################################################
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

############################################################
#
# Function Name : SendEmail
# Description   : Send backup report through email
#
############################################################

def SendEmail(SenderEmail,SenderPassword,ReceiverEmail,Subject,Message,ZipFilePath):

    try:
        EmailMessage = MIMEMultipart()

        EmailMessage["Subject"] = Subject
        EmailMessage["From"] = SenderEmail
        EmailMessage["To"] = ReceiverEmail

        Body = MIMEText(Message)
        EmailMessage.attach(Body)

        with open(ZipFilePath, "rb") as fobj:

            Attachment = MIMEBase("application","octet-stream")

            Attachment.set_payload(fobj.read())

        encoders.encode_base64(Attachment)

        FileName = os.path.basename(ZipFilePath)

        Attachment.add_header("Content-Disposition","attachment",filename=FileName)

        EmailMessage.attach(Attachment)

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(SenderEmail,SenderPassword)

        Server.sendmail(SenderEmail,ReceiverEmail,EmailMessage.as_string())

        Server.quit()

        print("Email sent successfully")

        return True

    except Exception as e:
        print("Unable to send email :", e)
        return False


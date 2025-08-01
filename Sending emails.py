from email.message import EmailMessage
import mimetypes
import smtplib
import pandas as pd
import getpass


customer_data_csv = r"/customer_data_50.csv"
customer_email_column= 'email'

def email_from_file(csv_file,email_column):
    """ Takes a csv file path and column containing the emails as an argument and returns the email parsed from the file"""
    customer_dataframe = pd.read_csv(csv_file)
    return customer_dataframe[email_column]


#Create message object from EmailMessage class
message = EmailMessage()
#Google no longer allows "less secure apps" to access Gmail with just your normal password if 2FA is activated. Instead, you must use an App Password, which is a one-time password generated for third-party apps like your Python script.
#This won't work in pycharm
password = getpass.getpass('Enter your gmail password :')

#Setting the image path as a variable
birkenstock = r"image attachment.png"


sender_email =  input("Enter sender's email address: ")
email_recipients = []
for email in email_from_file(customer_data_csv,customer_email_column).head():
    email_recipients.append(email)



message['From'] = sender_email
message['To'] = sender_email
message['Bcc'] = email_recipients


#Setting the content
message['Subject'] = "Sending this email using python"
body = """" Sending this email to test my python skills
            Hire me for jobs that require automation
            Thank you in advance
        """
message.set_content(body)

#Determining the MIME type and MIME subtype and returns a tuple like (mime_type, encoding)
encryption_of_image = mimetypes.guess_type(birkenstock)
#Seperating it into MIME type and MIME subtype
picture_MIME_type, picture_MIME_subtype = encryption_of_image[0].split('/',1)


#Reading the file in Binary and Attaching it to the message to be sent
with open(birkenstock , 'rb') as bk:
    message.add_attachment(bk.read(),
                           maintype = picture_MIME_type,subtype = picture_MIME_subtype,
                           filename = birkenstock)


#Opening the server, the "with" clause will close it immediately once done
with smtplib.SMTP_SSL('smtp.gmail.com',port=465) as my_gmail_server:
    # Getting email password
    my_gmail_server.login(sender_email , password)
    for recipient in email_recipients:
        my_gmail_server.send_message(message,recipient)

print("All emails have been sent my liege")



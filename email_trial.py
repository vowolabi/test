import pandas as pd
import smtplib
import os
from email.message import EmailMessage
from time import sleep


# assumes log in credentials are stored in the environment variable
def send_email(recipient, subject, body, env_add, env_pass, attachment_path=None):
    print(os.getcwd())
    # get login credentials from environment variable
    email_addr = os.getenv(env_add)
    email_pass = os.environ.get(env_pass)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_addr
    msg["To"] = recipient
    msg.set_content(body)

    if attachment_path is not None:  # assert attachment file is included
        path_list = []
        if os.path.isdir(attachment_path):
            attachment_files = os.listdir(attachment_path)
            for file in attachment_files:
                path_list.append(os.path.join(attachment_path, file))
        elif os.path.isfile(attachment_path):
            path_list.append(attachment_path)
        for files in path_list:
            with open(files, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data, maintype='application', subtype='octet-steam', filename=file_name)

    # send email using smpt connection
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_addr, email_pass)
        smtp.send_message(msg)


e = pd.read_csv("C:/Users/Alome/PycharmProjects/Emails/maillist.csv")
mail_list = e["Emails"].values
print(mail_list)
for recipients in mail_list:
    send_email(recipients, 'my world', 'its big', 'EMAIL_ADD', 'EMAIL_PASS', attachment_path="C:/Users/Alome"
                                                                                             "/PycharmProjects/Emails"
                                                                                             "/dagegen.PNG")
    sleep(30)

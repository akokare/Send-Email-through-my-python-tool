#The first step is to create an SMTP object, each object is used for connection with one server
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#importing the necessary classes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#composing email headers
fromaddr = "ashishkokare11@gmail.com"
toaddr = "target@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"


# body of the email to the MIME message
body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

#For sending the mail, we have to convert the object to a string
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("youremailusername", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

#Next, log in to the server
server.login("youremailusername", "password")

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("ashishkokare11@gmail.com", "swapnilon@gmail.com", "Hello Swapnil!- This email is sent from Ashish Email Sender!")














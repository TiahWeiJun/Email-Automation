import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

#Details
sender_email = config("SENDER_EMAIL")
password = config("PASSWORD")

# Set up
server = smtplib.SMTP("smtp.office365.com", 587)
server.ehlo()
context = ssl.create_default_context()
server.starttls(context=context)
server.login(sender_email, password)

# Send Email Function
def send_emails(receiver_email):
    #Email Content
    message = MIMEMultipart()
    message["Subject"] = "NTU Tamarind Hall Sponsorship Request"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
        <head>
            <style type="text/css">
                body {font-family: "Calibri"}
            </style>
        </head>
        <body>
            <p>Dear Sir/Madam,<br><br>
                I am Wei Jun, representing the Business Managers of Nanyang Technological University (NTU)’s newest undergraduate Hall of Residence - Tamarind Hall.<br><br>
                In lieu of the freshmen orientation program in 2021, our Hall Council would like to request for a sponsorship for our freshmen welfare dinner goodie bag 
                which will be distributed on the 25th of August. This distribution of these goodie bags takes place once a year, with an estimate of 300 goodie bags 
                given out each session.<br><br>
                These goodie bags aim to welcome the incoming freshmen to our Hall, allowing our residents to understand that their well-being is taken care of.<br><br>
                If you are keen in providing us with sponsorship, here are some examples of the items we are looking out for to be included in the welfare package:<br>
                <ul>
                    <li>Snacks and Beverages</li>
                    <li>Product Samples</li>
                    <li>Vouchers/Coupons</li>
                    <li>Other items you are willing to sponsor</li>
                </ul>
                <br>
                We hope this platform helps to promote brand awareness of our sponsors through utilising our numbers to your advantage, providing opportunities for 
                greater exposure and publicity to our residents. Acknowledgement and appreciation to our sponsors will also be publicised on Tamarind Hall’s Facebook and 
                Instagram pages. Furthermore, we will be able to show support through likes, shares and positive comments on your social media pages to expand your reach 
                to a wider target audience.<br><br>
                We are also open to any other suggestions or requests our sponsors might have for us to promote their brand. Terms and conditions of the sponsorships 
                can be discussed. <br><br>
                Your contributions will make our freshmen orientation program a more pleasant experience for the residents in our hall. <br><br>
                Thank you and we hope to hear from you soon!<br><br>
                Yours sincerely,<br><br>
                Tiah Wei Jun <br>
                Business Manager Sub-Committee | 4th Tamarind Hall Council<br>
                HP: (+65) 9856 4618<br>
                Email: <a href="mailto:tamarind-bizmag@e.ntu.edu.sg">tamarind-bizmag@e.ntu.edu.sg</a><br>
            </p>
        </body>
    </html>
    """

    part = MIMEText(html, "html")
    message.attach(part)

    server.sendmail(sender_email, receiver_email, message.as_string())

list_of_emails = ["tiahweijun1999@gmail.com"]

for email in list_of_emails:
    send_emails(email)

print("Emails sent!")

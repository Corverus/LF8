import smtplib

class EMailDienst():
    def __init__(self, host, adress, password):
        self.host = host
        self.adress = adress
        self.password = password
    
    def sendEMail(self, receiver, message):
        try:
            smtpObj = smtplib.SMTP_SSL(self.host, 465) 
            smtpObj.ehlo()
            smtpObj.login(self.adress, self.password)
            smtpObj.sendmail(self.adress, receiver, message)
            print ("Success")
        except smtplib.SMTPException:
            print ("Failure")


client = EMailDienst('smtp.gmail.com', 'lf8warningtool@gmail.com', 'LF8!Gruppe4')
client.sendEMail('ben.zimmerhh@gmail.com', 'hallo')
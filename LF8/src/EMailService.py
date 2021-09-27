import smtplib


class EMailDienst:
    def __init__(self, host, adress, password):
        self.host = host
        self.adress = adress
        self.password = password

    def sendEMail(self, receiver, message):
        try:
            smtpObj = smtplib.SMTP(self.host, 587)
            smtpObj.starttls(keyfile=None, certfile=None, context=None)
            # smtpObj.ehlo()
            smtpObj.login(self.adress, self.password)
            smtpObj.sendmail(self.adress, receiver, message)
            print("Success")
        except smtplib.SMTPException:
            print("Failure")

    def buildBody(self, percent):
        body = """Warning \n\nThe harddrive of the system is %d%% filled.""" % (percent)
        return (body)

    def buildMessage(self, sent_from, to, subject, body):

        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (sent_from, ", ".join(to), subject, body)

        return (message)


def sendMail(value):
    client = EMailDienst('smtp-mail.outlook.com', 'lf8warningtool@outlook.de', 'LF8!Gruppe4')
    body = client.buildBody(value)
    message = client.buildMessage('lf8warningtool@outlook.de', ['lf8warningtool@gmail.com'], 'Warning', body)
    client.sendEMail('lf8warningtool@gmail.com', message)

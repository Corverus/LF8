import os

class LogInService():
    def __init__(self):
        self.filename = os.path.join('../src/output', 'LF8Users.txt')
        rfile = open(self.filename, 'r')
        tlines = rfile.readlines()
        tlines = [line.rstrip() for line in tlines]
        self.users = list(tlines[0].split('|'))
        self.passwords = list(tlines[1].split('|'))
        self.emails = list(tlines[2].split('|'))
        rfile.close
        if self.logIn():
            print('Herzlich Willkommen ' + self.users[self.index]) 
        else:
            exit()

    def logIn(self):
        user = input('Bitte geben Sie den Username an, in den sie sich einloggen wollen. ->')
        password = input('Bitte geben Sie das Password Ihres Users ein. ->')
        self.index = self.users.index(user)
        if password == self.passwords[self.index]:
            return(True)
        else:
            return(False)

    def adduser(self, user, password, email):
        if user in self.users:
            print('Es existiert bereits ein User mit dem Namen:' + user)
        else:
            self.users.append(user)
            userString = createString(self.users)
            self.passwords.append(password)
            passwordString = createString(self.passwords)
            self.emails.append(email)
            emailString = createString(self.emails)
            wfile = open(self.filename, 'w')
            strings = [userString, passwordString, emailString]
            wfile.writelines(strings)
            wfile.close

    def createString(strList):
        for element in strList:
            output = output + '|' + element
        return(strList[1:])


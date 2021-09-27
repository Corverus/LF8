import os
import base64

filename = os.path.join('../src/output', 'LF8Users.txt')
rfile = open(filename, 'r')
tlines = rfile.readlines()
tlines = [line.rstrip() for line in tlines]
users = list(tlines[0])
passwords = list(tlines[1])
emails = list(tlines[2])
rfile.close

wfile = open(filename, 'w')

base64.b64encode(users)
base64.b64encode(passwords)
base64.b64encode(emails)
wfile = open(filename, 'w')
strings = [users, passwords, emails]
wfile.writelines(strings)
wfile.close
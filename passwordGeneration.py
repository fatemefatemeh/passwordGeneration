import secrets
import string

letter = string.ascii_letters
digits = string.digits
special_chars = string.ascii_letters

alphabet = letter + digits + special_chars

psw_lenght = 12
psw = ''
for i in range(psw_lenght):
    psw += ''.join(secrets.choice(alphabet))
print(psw)

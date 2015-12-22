#AT&T (formerly Cingular) [10-digit phone number]@txt.att.net
#Sprint PCS (now Sprint Nextel) [10-digit phone number]@messaging.sprintpcs.com
#T-Mobile [10-digit phone number]@tmomail.net
#Verizon [10-digit phone number]@vtext.com


import smtplib, random, string, datetime
from config import *

def random_word(length):
   return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(length))


sms_text=""
log=""
numbers = [line.rstrip('\n') for line in open('numbers.txt')]
facts = [line.rstrip('\n') for line in open('facts.txt', encoding='utf8')]
for number in numbers:
    sms_text=number + "\n" + random.choice(facts) + "\n<To cancel Daily Cat Facts, reply 'Cancel " + random_word(20) + "'>"
    log = number + " sent on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( gmail_username, gmail_password)
    server.sendmail( gmail_username, number, sms_text)
    server.quit()
    f = open('log_file.txt', 'w')
    f.write(log)
    f.close()
    print("Ran script on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")




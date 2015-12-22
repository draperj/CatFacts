import smtplib, random, string
from config import *

def random_word(length):
   return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(length))

sms_text=""
numbers = [line.rstrip('\n') for line in open('numbers.txt')]
facts = [line.rstrip('\n') for line in open('facts.txt')]
for number in numbers:
    sms_text=number + "\n" + random.choice(facts) + "\n<To cancel Daily Cat Facts, reply 'Cancel " + random_word(20) + "'>"
    # server = smtplib.SMTP( "smtp.gmail.com", 587 )
    # server.starttls()
    # server.login( gmail_username, gmail_password)
    # server.sendmail( gmail_username, number, sms_text)
    # server.quit()
    print(sms_text);




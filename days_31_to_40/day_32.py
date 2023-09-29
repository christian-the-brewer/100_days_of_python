# day 32
# pythontest553@gmail.com

import smtplib
import secret

my_email = "pythontest553@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=secret.app_pw)

connection.sendmail(from_addr=my_email,
                    to_addrs="brewer.christiang@gmail.com", msg="hello")
connection.close()

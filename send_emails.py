
import pandas as pd

#importing csv file
data = pd.read_csv("Automated_emails/PEC ACM Chess Tournament 1- Contact Info (Responses).csv")

#converting to list
li = data.iloc[:,1].values

#sending emails
import smtplib
#logging into gmail
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("xyz@gmail.com", "your password")
message = "Message_you_need_to_send"
subject = "Subject you need to send"

for destination in li:    
    s.sendmail("xyz@gmail.com", destination, subject, message) 

s.quit()



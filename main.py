import smtplib
domainName = input("Enter SMTP Domain name: ")
portCode = int(input("Enter Port: "))
connector = smtplib.SMTP_SSL(domainName,portCode)
#Commented region can be run to check if the connection was successfull
# print(type(connector))
#print(connector.ehlo())


sender = input("Enter Sender's Email : ")
password = input("Enter Password : ")
gettingIn = connector.login(sender, password)
#print(gettingIn)
receiver = input("Enter Receiver's Email address: ")
mailBody = input("Enter Mail Body: ")
sendingMail = connector.sendmail(sender, receiver, f'Subject: \n {mailBody}')
print("Mail Successfully Sent!!")
quittingServer = connector.quit()
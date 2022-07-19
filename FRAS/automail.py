import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("500075195@stu.upes.ac.in", "opnlnxrltxqhkpgk")

# sent the mail
yag.send(
    to="500075195@stu.upes.ac.in",
    subject="Attendance Reort", # email subject
    contents="Attendance Report",  # email body
    attachments= filename  # file attached
)
print("Email Sent!")


# try:
#     #initializing the server connection
#     yag = yagmail.SMTP(user='aviralmehra08@gmail.com', password='aviral008')
#     #sending the email
#     yag.send(to='aviralmehra08@gmail.com', subject='Testing Yagmail', contents='Hurray, it worked!')
#     print("Email sent successfully")
# except:
#     print("Error, email was not sent")


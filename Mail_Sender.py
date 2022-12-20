
from datetime import *
from email import message
import time
import schedule
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Mail_Sender(dir=argv[1]):
    listToAddr=list()
    fromaddr = "prajwalpatil2193@gmail.com"
    listToAddr = ['geetapatil8872@gmail.com'] 
    
    msg = MIMEMultipart()
    for toaddr in listToAddr:
        msg['From'] = fromaddr
        msg['To'] = toaddr

        msg['Subject'] = "Mail send using automation"

        body = """Hi 
            I am Prajwal Patil
            Very Good Morning
                                
            yours
            %s"""%fromaddr

        msg.attach(MIMEText(body,'plain'))

        attach = open(dir,'rb')

        p = MIMEBase('application','octet-stream')
        p.set_payload((attach).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % dir)                 
        msg.attach(p)
    
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("prajwalpatil2193@gmail.com","bpaiuernpcbxewve")
        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()
        
        print(" Mail sent Successfully...")


def main():
    print("--------------------------------------------")
    print("****{Automation Script By Prajwal Patil}****")
    
    print()
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName Directory_name Email_address_want_to_send")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to send the mail attach with log file")
            exit()

    if (len(argv)==2):
        try:
            
            schedule.every(3).seconds.do(Mail_Sender)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError:
            print("Value Error")

        except Exception as e: 
            print("Error : ",e)
            
if __name__ == "__main__":
    main()               
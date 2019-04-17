from tkinter import *
from tkinter import messagebox
import smtplib
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.image import MIMEImage
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

f=Tk()

send_email=StringVar()
send_pass=StringVar()
recv_email=StringVar()
attch_email=StringVar()
file_email=StringVar()
subject=StringVar()
msg_body=None


def layout():
    f.title(" Gmail Gui ")
    menuBar=Menu(f)
    f.config(menu=menuBar)
    
    sender_email=Label(f,text="Sender's Gmail ID: ")
    sender_entry=Entry(f,textvariable=send_email,bd=3)
    sender_pass=Label(f,text="Sender's Gmail Pass: ")
    sender_passentry=Entry(f,show='*',textvariable=send_pass,bd=3)

    receiver_email=Label(f,text="Receiver's Email: ")
    receiver_entry=Entry(f,textvariable=recv_email,bd=3)

    sub_email=Label(f,text="Subject: ")
    sub_entry=Entry(f,textvariable=subject,bd=3)
    
    msg_label=Label(f,text='Message')
    global msg_body
    msg_body=Text(f,height=5,width=15,bd=3)
    
    email_attachments=Label(f,text="Attachment Path: ")
    attachment_entry=Entry(f,textvariable=attch_email,bd=3)

    email_file=Label(f,text="File name: ")
    file_entry=Entry(f,textvariable=file_email,bd=3)

   
    send=Button(f,text='Send',width=15,command=mail,bd=3)
    cancel=Button(f,text='Cancel',width=15,command=destroy,bd=3)

    sender_email.grid(row=0,column=0,padx=5,pady=3)
    sender_entry.grid(row=0,column=1,padx=5,pady=3)
    sender_pass.grid(row=1,column=0,padx=5,pady=3)
    sender_passentry.grid(row=1,column=1,padx=5,pady=3)
    receiver_email.grid(row=2,column=0,padx=5,pady=3)
    receiver_entry.grid(row=2,column=1,padx=5,pady=3)
    sub_email.grid(row=3,column=0,padx=5,pady=3)
    sub_entry.grid(row=3,column=1,padx=5,pady=3)

    msg_label.grid(row=4,column=0,padx=5,pady=3)
    msg_body.grid(row=4,column=1,padx=5,pady=3)
    email_attachments.grid(row=5,column=0,padx=5,pady=3)
    attachment_entry.grid(row=5,column=1,padx=5,pady=3)
    email_file.grid(row=6,column=0,padx=5,pady=3)
    file_entry.grid(row=6,column=1,padx=5,pady=3)

    send.grid(row=7,column=0,padx=5,pady=3)
    cancel.grid(row=7,column=1,padx=5,pady=3)
    f.mainloop()

def destroy():
    f.destroy()
    
def msg_box():
    messagebox.showinfo("Email Info","Mail Sent")
    

def mail():
    try:
        if send_email.get()=="" or send_pass.get()=="" or recv_email.get()=="":
            messagebox.showerror("Error","Please enter the complete details.")
        else:
            d=recv_email.get().split(",")
            i=len(d)
            
            #can be send to many users at a time . give emails with "," separator.
            for j in range(0,i):
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                msg = MIMEMultipart()
                
                a=send_email.get()
                b=send_pass.get()
                c=msg_body.get('1.0',END)
                
                msg['Subject'] = subject.get()
                msg.attach(MIMEText(c, 'plain'))
                filename = attch_email.get().split(",")
                k=len(filename)
                x=file_email.get().split(",")
                #many files can be attached at a time . give files separated with ",".
                for l in range(0,k):
                    if filename[l] !="*":
                        attachment=open(filename[l],"rb") 
                        p = MIMEBase('application', 'octet-stream')
                        p.set_payload((attachment).read())
                        encoders.encode_base64(p)
                        p.add_header('Content-Disposition', "attachment; filename= %s" % x[l])
                        msg.attach(p)
                    else:
                        break
                    
                text = msg.as_string()
                server.login(a,b)
                server.sendmail(a,d[j],text)
                     
                server.close()
            msg_box()
    except Exception as e:
        print(e)
        a=messagebox.askokcancel("Error","Read instructions")

layout()

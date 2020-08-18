#blocker specefic Sites 
import time
from datetime import datetime as dtime
# host_temp = path of your hosts file like C:\Users\test2/test1 
host_temp=r'path-hosts'
redirect='127.0.0.1'
website_list=['www.google.com','google.com','youtube.com']

while True:
    if dtime(dtime.now().year,dtime.now().month,dtime.now().day,0)< dtime.now() <dtime(dtime.now().year,dtime.now().month,dtime.now().day,16):
        with open(host_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                     pass
                else:
                    file.write(redirect+'   '+website+'\n')    
    else:
        print("fun hours")
        with open(host_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


       
   

            
    time.sleep(5)
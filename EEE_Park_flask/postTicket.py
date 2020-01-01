import sys

import requests
import datetime
from datetime import timedelta
def postTicket(lp,img_path,num_camera):
    post_data = {'lp':lp,'img_path':img_path ,'num_camera': num_camera}
    print(post_data)
    ans = requests.post("http://10.144.70.187:5000/add_ticket", data=post_data)
    print(ans)
    print(ans.text)
details = sys.argv
print(details)
lp,img_path,num_camera = details[1:]
# postTicket("11111999","C:/Users/elia/PycharmProjects/EEE_Park/static/70-558-53.jpg",1)
postTicket(lp,img_path,int(num_camera))
# if __name__=="__main__":
    #details = sys.argv
    #lp,img_path,num_camera = details[1:]
    #print(lp,img_path,num_camera)

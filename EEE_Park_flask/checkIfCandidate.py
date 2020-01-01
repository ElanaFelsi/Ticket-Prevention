import base64
import os
import sys

import requests
import datetime
from datetime import timedelta
def encodedImg(image_name):
    with open(f"{image_name}", "rb") as image_file:
        encoded_string_img = base64.b64encode(image_file.read())
    base64_string_img = encoded_string_img.decode('utf-8')
    payload = {'img_name': image_name, 'img': str(base64_string_img)}
    print("sendd",image_name)
    ans = requests.post("http://10.144.70.189:5000/upload-image", data=payload)
    print(ans.text)
    if os.path.exists(f"{image_name}"):
        os.remove(f"{image_name}")
        print(f"del {image_name}")
def checkIfCandidate(lp,img_name,num_camera):
    param = {'lp':lp,'num_camera': num_camera,'img_name':img_name}

    print("detect",lp,param)
    ans = requests.get("http://10.144.70.189:5000/checkLP", params=param)
    data = ans.text
    print(type(data),data)
    if data == "True":#return true -candidate
        print(img_name)
        encodedImg(img_name)
        ans = requests.post("http://10.144.70.189:5000/add_candidate", data=param)

        print("wooooooooooooooooow")

details = sys.argv
print(details)
lp,img_name,num_camera = details[1:]
checkIfCandidate(lp,img_name,int(num_camera))

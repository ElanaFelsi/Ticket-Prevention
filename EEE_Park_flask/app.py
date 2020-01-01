import base64
import os
import time

from EEE_Park import app
from flask import render_template, request
from tables import ticket_records,ticket_amount,camera_location,handicapped_lp
from add_to_db import add_tickets, add_candidates, add_license_plates, add_camera_location
from queries import check_lp, get_candidate, get_img_name
import datetime
from message import warning_sms, ticket_sms

@app.route('/')
def hello():
    # add_license_plates("1222222","+9720545891600")
    # add_license_plates("1111111","+972586601950")
    # add_tickets("1111111","70-558-53.jpg",1)
    # add_camera_location(1,["handicapped"])
    # add_handicapped("1234567","+972586601950")
    return "Helloooooo"

# set FLASK_APP=app.py
# python -m flask run --host=0.0.0.0
# set FLASK_ENV=development

@app.route('/ticket/<num_ticket>')
def show_ticket(num_ticket):
    record = ticket_records.objects(num_ticket=num_ticket)[0]
    if record:
        lp = record['lp']
        time = record['date_time']
        camera_loc = camera_location.objects(num_camera=record['num_camera'])[0]
        place = ""
        amount = 100 #defualt
        if camera_loc:
            place = camera_loc['location']
            print(camera_loc['ctype'][0])
            img = get_img_name(num_ticket)
            amount = ticket_amount.objects(ctype=camera_loc['ctype'][0])[0]
            t = str(time.time()).split(":")
            return render_template('show_ticket.html', LP=lp, Place=place, Time=f"{time.date()} {t[0]}:{t[1]}", Amount=amount['amount'],Img = img)
    return
@app.route('/checkLP', methods=['GET'])
def checkLP():
    _lp = request.args.get('lp')
    num_camera = request.args.get('num_camera')
    print("checked",_lp,num_camera)
    ans = check_lp(_lp, int(num_camera))
    return f"{ans}"


@app.route('/add_ticket', methods=['GET'])
def add_ticket():
    candidate = get_candidate()
    lp = candidate['lp']
    num_camera = candidate['num_camera']
    img_path = candidate['img']
    s_time = candidate['date_time']
    print("second",(datetime.datetime.now()-s_time).total_seconds())
    if (datetime.datetime.now()-s_time).total_seconds() > 1:
        num_ticket = add_tickets(lp,str(img_path), int(num_camera))
        time.sleep(8)
        ticket_sms(num_ticket)
    return f"{lp}"
@app.route("/upload-image", methods=[ "POST"])
def upload_image():
    img = request.form.get('img')
    img_name = request.form.get('img_name')

    imgdata = base64.b64decode(img)
    with open(os.path.join(os.getcwd(),f'static\image\{img_name}'), 'wb') as f:
        if not os.path.exists(f"{img_name}"):
            f.write(imgdata)
    return "got the image!"
@app.route("/add_candidate", methods=[ "POST"])
def add_candidate():
    img_name = request.form.get('img_name')
    lp=request.form.get('lp')
    num_camera=request.form.get('num_camera')
    add_candidates(lp,str(img_name),num_camera)
    warning_sms(lp)
    return "send warnning"


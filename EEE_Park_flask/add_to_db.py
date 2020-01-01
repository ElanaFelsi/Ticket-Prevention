import datetime

from tables import ticket_records,ticket_amount,camera_location,handicapped_lp,candidate_record,license_plates
from queries import get_camera_id,get_ticket_id

def add_tickets(lp,img_path,num_camera):
    num_ticket=get_ticket_id()
    row = ticket_records(num_ticket=num_ticket, lp=lp, date_time=datetime.datetime.now(),
                                                    img=img_path,num_camera = num_camera)
    row.save()
    return num_ticket
def add_camera_location(location,types):
    row = camera_location(num_camera=get_camera_id(), location="king goerge 20", ctype=types)
    row.save()
def add_ticket_amount(type,amount):
    row = ticket_amount(ctype=type, amount =amount)
    row.save()
def add_handicapped(lp):
    row = handicapped_lp(lp=lp)
    row.save()
def add_candidates(lp,img,num_camera):
    row = candidate_record(lp=lp,img=img,date_time=datetime.datetime.now(),num_camera=num_camera)
    row.save()
def add_license_plates(lp,phone):
    row = license_plates(lp=lp, phone_number=phone)
    row.save()

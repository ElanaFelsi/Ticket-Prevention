import sys
import smtplib, ssl

from tables import ticket_records, camera_location, handicapped_lp, candidate_record, license_plates


def get_camera_id():
    num_camera = 1;
    cameras = camera_location.objects()
    if cameras:
        num_camera = max(map(lambda item: item['num_camera'],cameras)) + 1
    return num_camera
def get_ticket_id():
    num_ticket = 1;
    tickets = ticket_records.objects()
    if tickets:
        num_ticket = max(map(lambda item: item['num_ticket'], tickets)) + 1
    return num_ticket

def get_img_name(num_ticket):
    return ticket_records.objects(num_ticket=num_ticket)[0]['img']

def get_candidate():
    candidate = candidate_record.objects().first()
    return candidate
def check_lp(lp,num_camera):#chek if this lp is candidate for getting ticket
    #need to check according the num camera type
    handicapped = handicapped_lp.objects()
    response = True
    print(handicapped)
    if handicapped:
       for h_lp in handicapped:
           print(h_lp['lp'],lp)
           if h_lp['lp'] == lp:
                print("its exist")
                response = False
                break
    # if response:
    #     send_warning_email(h_lp['email'])
    return response

def get_phone_number(license):
    print(license_plates.objects(lp=license)[0]['phone_number'])
    return license_plates.objects(lp=license)[0]['phone_number']
import mongoengine as me
class ticket_records(me.Document):
    num_ticket = me.IntField()
    lp = me.StringField(required=True)
    img = me.StringField()
    num_camera = me.IntField()
    date_time = me.DateTimeField()
class candidate_record(me.Document):
    lp = me.StringField(required=True)
    img = me.StringField()
    date_time = me.DateTimeField()
    num_camera = me.IntField()

class camera_location(me.Document):
    num_camera = me.IntField(required=True)
    location = me.StringField()
    ctype = me.ListField()

class license_plates(me.Document):
    lp = me.StringField(required=True)
    phone_number = me.StringField(required=True)

class handicapped_lp(me.Document):
    lp = me.StringField(required=True)

class ticket_amount(me.Document):
    ctype = me.StringField()
    amount = me.IntField()

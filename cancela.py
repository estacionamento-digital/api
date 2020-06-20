import serial
import time
import firebase_admin
from firebase_admin import credentials, firestore

arduino = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

cred = credentials.Certificate("pi-park-2020-firebase-adminsdk-y8zea-8181185594.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

cancela_ref = db.collection(u'cancela').document(u'i8lmwUc59Ptf4Qpp4LgH')
cancela = cancela_ref.get(field_paths={'cancela'}).to_dict().get('cancela')

if(cancela == 'aberta'):
    arduino.write(b'1')
else:
    arduino.write(b'0')
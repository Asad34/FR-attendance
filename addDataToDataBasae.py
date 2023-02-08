import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-40d84-default-rtdb.firebaseio.com/"
})


ref=db.reference('students')
data={
    "321654":{
        "Name": "Syed Ali Ahmed",
        "Major" : "software engineer",
        "Starting_Year" : 2017,
        "total_attendance":6,
        "Standing":'G',
        "Year" :4,
        "Last_attendace_Time":"2022-12-11  00:54:34"
    },
    "852741": {
        "Name": "Muhammad Adeel",
        "Major": "software engineer",
        "Starting_Year": 2017,
        "total_attendance": 6,
        "Standing": 'G',
        "Year": 4,
        "Last_attendace_Time": "2022-12-11  00:54:34"
    },
    "963852": {
        "Name": "Abuzar Hassan",
        "Major": "software engineer",
        "Starting_Year": 2017,
        "total_attendance": 6,
        "Standing": 'G',
        "Year": 4,
        "Last_attendace_Time": "2022-12-11  00:54:34"
    }



}

for key,value in data.items():
    ref.child(key).set(value)
print("done...")

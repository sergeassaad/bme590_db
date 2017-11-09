from database_setup import Patient
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/average_bmi/<age>")
def average_bmi(age):
    sum = 0
    count = 0
    for pat in Patient.objects.raw({"age": age}):
        count+=1
        sum += pat.bmi
    dict_out ={"average_bmi": float(sum/count)}
    return jsonify(dict_out)


@app.route("/new_patient", methods = ['POST'])
def new_patient():
    if type(request.json['name']) is not str or type(request.json['age']) is not int or type(request.json['bmi']) is not float:
        request.status_code = 406  #validation error status code
    u = Patient(request.json['name'], bmi=request.json['bmi'], age=request.json['age'])
    u.save()

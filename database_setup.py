from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://vcm-1834.vm.duke.edu:27017/bme590_db")

class Patient(MongoModel):
    name = fields.CharField(primary_key = True)
    bmi = fields.FloatField()
    age = fields.FloatField()
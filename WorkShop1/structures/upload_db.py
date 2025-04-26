from config import db
from models import Country, City, Building
import csv
import os
dirname = os.path.dirname(__file__)
dataFolder = os.path.join(dirname, 'data/')

def Country_upload():
    with open(dataFolder+'country.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Country(item[0])
            db.session.add(new_entry)
        db.session.commit()
        
def Country_rewriting():
    Country.query.filter(Country.id !=-1).delete()
    db.session.commit()

    Country_upload()

def City_upload():
    with open(dataFolder+'city.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = City(item[0],item[1])
            db.session.add(new_entry)
        db.session.commit()
        
def City_rewriting():
    City.query.filter(City.id !=-1).delete()
    db.session.commit()

    City_upload()

def Building_upload():
    with open(dataFolder+'building.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Building(item[0],item[1],item[2],item[3],item[4])
            db.session.add(new_entry)
        db.session.commit()
        
def Building_rewriting():
    Building.query.filter(Building.id !=-1).delete()
    db.session.commit()

    Building_upload()

def Reupload_tables():
    Country_rewriting()
    City_rewriting()
    Building_rewriting()

Reupload_tables()

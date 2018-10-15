from time import time
from datetime import datetime
from numpy import genfromtxt, array
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))

from app.models import Company
from instance.config import SQLALCHEMY_DATABASE_URI


def Load_Data(file_name):
    json_data = open(file_name).read()
    json_content = json.loads(json_data)
    return array(json_content)


Base = declarative_base()

if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)

    #Create the session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        file_name = "us_companies.json"
        data = Load_Data(file_name)
        for i in data:
            record = Company.Company(**{
                'name': i['Name']
            })
            q = session.query(Company.Company.id).filter(Company.Company.name == record.name)
            record_exists = session.query(q.exists()).scalar()
            if not record_exists:
                session.add(record)
            else:
                print('Duplicate entry found: ', record.name)

        session.commit()
    except Exception as e:
        print('Rolling back due to error: {}'.format(e))
        session.rollback()
    finally:
        session.close()
    print("Time elapsed: " + str(time() - t) + " s.")

from csv import DictReader
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


DATABASE_URI = "sqlite:///titanic_orm.db"
CSV_FILEPATH = 'titanic.txt'

engine = create_engine(DATABASE_URI)
Base = declarative_base(bind=engine)
session = Session(bind=engine)


#Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

class Passenger(Base):
    __tablename__='Passenger'
    Id = Column(Integer, primary_key=True)
    Survived = Column(Integer)
    Pclass = Column(Integer)
    Name = Column(String)
    Sex = Column(String)
    Age = Column(Integer)
    Siblings_Spouses_Aboard = Column(Integer)
    Parents_Children_Aboard = Column(Integer)
    Fare = Column(Float)

with open(CSV_FILEPATH,'r') as f:
    reader = DictReader(f) #csv 파일도 dict으로 바꿔줌! 
    row_list = []
    for row in reader:
        row_list.append(row)
                                  #dict 형식으로 바뀌어서 키값 넣어줌
        query1 = Passenger(Survived=row['Survived'], Pclass=row['Pclass'], Name=row['Name'], Sex=row['Sex'], Age=row['Age'], Siblings_Spouses_Aboard=row['Siblings/Spouses Aboard'],\
            Parents_Children_Aboard=row['Parents/Children Aboard'], Fare=row['Fare'])
        session.add(query1)
    session.commit()
    
   # https://velog.io/@dmstj907/Python%EC%9E%90%EB%8F%99%ED%99%94%EC%B2%98%EB%A6%AC-CSV%ED%8C%8C%EC%9D%BC-%EC%9D%BD%EA%B3%A0%EC%93%B0%EA%B8%B0

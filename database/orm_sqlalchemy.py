from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Definir la base de datos
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

#Definir modelo
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

#Crear la tabla
Base.metadata.create_all(engine)

#Insertar datos
Session = sessionmaker(bind=engine)
session = Session()
session.add(User(name='Dereck', age=25))
session.commit()

#Consultar datos
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
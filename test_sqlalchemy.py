from models import User
from db_connection import DBConnection

dbconnection = DBConnection()

session = dbconnection.get_session()

dbconnection.add(User(name="Tom", age=50))


# query one user
try:
    user = session.query(User).filter(User.name=='Tom').first()
    print(user.name)
except:
    print("there is no user")
finally:
    session.close()

# query all users
users = session.query(User).all()

[print(user.name) for user in users]

session.close()
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Session
engine = create_engine("mysql+mysqlconnector://root:test$@localhost/remote_db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
Base.metadata.create_all(engine)

#Insert Data (SQL Insert)

# #Create a new session
# session = Session(engine)
# #Create a new user
# new_user = User(name="Randy",email="RKO@nowhere.com")

# #Add the user to the session
# session.add(new_user)
# #Commit the session
# session.commit()
# #Close the session
# session.close()



# session = Session(engine)
# #Query Data (SQL Select)
# #Query all users

# query = select(User)
# users = session.execute(query).scalars().all()
    
# #print the users
# for user in users:
#     print(user.id, user.name, user.email)
# #Close the session
# session.close()

# session = Session(engine)

#Query Data (SQL DELETE)

# user_to_delete = session.query(User).filter_by(id=3).first()

# if user_to_delete:
#     session.delete(user_to_delete)
#     session.commit()
#     print(f"User with id {user_to_delete.id} deleted.")
# else:
#     print("User not found.")
# #Close the session
# session.close()

# session = Session(engine)
# # Query users with a specific email
# query = select(User).where(User.name == "Randy")
# user = session.execute(query).scalars().first()


# print(user.name)  # Outputs: Alice


session = Session(engine)
#Update Data (SQL UPDATE)
# Query the user
query = select(User).where(User.id == 1)
user = session.execute(query).scalars().first()

# Update the user's name
user.name = 'Alton'

# Commit the changes
session.commit()
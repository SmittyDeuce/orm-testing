from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# Database connection
engine = create_engine("mysql+mysqlconnector://root:test@localhost/remote_db")

# Base class for models
class Base(DeclarativeBase):
    pass

# User model
class User(Base):
    __tablename__ = "user_account"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(200))

    # One-to-Many: User -> List of Pet objects
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner", cascade="all, delete-orphan")

# Pet model
class Pet(Base):
    __tablename__ = "pets"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    # Many-to-One: Pet -> User
    owner: Mapped["User"] = relationship(back_populates="pets")
# Create tables
Base.metadata.create_all(engine)

session = Session(engine)
# Insert Data (SQL Insert)
# Create a new user
new_user = User(name='Alton', fullname="Alton S")
session.add(new_user)
# Commit the session
session.commit()
# Close the session
session.close()

#select all users
session = Session(engine)
query = select(User)
users = session.execute(query).scalars().all()
# Print the users
for user in users:
    print(user.id, user.name, user.fullname)
# Close the session
session.close()



session = Session(engine)
new_pet = Pet(name="Olivia", animal="Hamster", user_id=1)  # Assuming User with id=1 exists
session.add(new_pet)
session.commit()

#First we query for our User, Alicia 
query = select(User).where(User.name == 'Alton')
user = session.execute(query).scalars().first()

# Accessing the pets relationship
for pet in user.pets:
    print(pet.name)  # Outputs: Olivia
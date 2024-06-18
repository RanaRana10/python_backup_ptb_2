

'''
Here i will defines the class of my main datbase logic 
so that i can use this in other places easily
Here i used pathlib's Path so that the .db file will saved in the folder
'''

from datetime import datetime
from pathlib import Path
import random
from typing import List

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Boolean ,DateTime, Integer, String

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_filename = "user_information_1_checking.db"
folder_name = Path("RanaUniverse") / "data_store_folder"
folder_name.mkdir(parents= True, exist_ok= True)
file_location = folder_name / db_filename


file_url = f"sqlite+pysqlite:///{file_location}"
engine = create_engine(url= file_url, echo= False)

Session = sessionmaker(bind= engine)
session = Session()


Base = declarative_base()


class UserDetails(Base):
    __tablename__ = "user_details"

    id_ = Column(Integer, primary_key= True)
    user_id_ = Column(Integer)
    user_name_ = Column(String)
    full_name_ = Column(String)
    is_allowed_ = Column(Boolean)
    validity_ = Column(DateTime)

    def __init__(
            self,
            user_id_:int = 0,
            user_name_:str = None,
            full_name_:str = None,
            is_allowed_:bool = None,
            validity_:datetime = None
    ):
        self.user_id_ = user_id_
        self.user_name_ = user_name_
        self.full_name_ = full_name_
        self.is_allowed_ = is_allowed_
        self.validity_ = validity_

    def __repr__(self):
        user_obj_details = f"<UserDetails(id={self.id_}, user_id={self.user_id_}, user_name={self.user_name_}, full_name={self.full_name_}, is_premium={self.is_allowed_}, validity={self.validity_})>"
        return user_obj_details


    '''Below are fun taking the class instance'''

    def add_user_return_id_(self):
        """This will take the user obj and return the inserted id_"""
        session.add(self)
        session.commit()
        inserted_id_ = self.id_
        print(inserted_id_, self)
        # session.close()
        return inserted_id_


    def delete_user_old(self):
        '''This is old fun'''
        session.delete(self)
        session.commit()

    def delete_user(self):
        try:
            session.delete(self)
            session.commit()
            print("User deleted successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting user: {e}")

    @staticmethod
    def return_user_obj(id_: int = 1):
        user_obj = session.query(UserDetails).filter(UserDetails.id_ == id_).first()
        return user_obj if user_obj else None


    @staticmethod
    def count_total_users():
        '''Count the total number of users'''
        count = session.query(UserDetails).count()
        session.close()
        return count
    

    @staticmethod
    def get_all_users():
        '''Get all users from the database'''
        users = session.query(UserDetails).all()
        session.close()
        return users



    # from typing import List
    # def add_multiple_users(users: List['UserDetails']):
    @staticmethod
    def add_multiple_users(users: type[List["UserDetails"]]):
        """Add multiple UserDetails objects to the database.and show the id_"""
        session.add_all(users)
        session.commit()

        for user in users:
            print(user.id_, user.full_name_)
            




    @staticmethod
    def insert_many_row_one_by_one_fake(number_of_row: int = 1):
        '''This is not good fun, rather i need to make a add_all fun'''
        for i in range(number_of_row):
            user_obj: UserDetails = UserDetails(
                user_id_= fake.random_int(100, 300),
                user_name_= (fake.name()).replace(" ", "_"),
                full_name_= fake.name(),
                is_allowed_= fake.boolean(),
                validity_= fake.date_time(end_datetime = datetime(2025, 1, 1)))
            user_obj.add_user_return_id_()


    @staticmethod            
    def insert_many_rows_fake(number_of_rows: int = 1):
        '''Insert multiple rows into the database using add_all method.'''
        users = []
        for i in range(number_of_rows):
            user = UserDetails(
                user_id_=fake.random_int(100, 300),
                user_name_=(fake.name()).replace(" ", "_"),
                full_name_=fake.name(),
                is_allowed_=fake.boolean(),
                validity_=fake.date_time(end_datetime=datetime(2025, 1, 1))
            )
            users.append(user)
        
        session.add_all(users)
        session.commit()
        print(users)
        print(users.__len__())


# This below line is the most important as it will do the main things

Base.metadata.create_all(engine)




if __name__ == "__main__":
    '''This is just for the example as if it is the another main.py scripts'''

    from faker import Faker
    fake = Faker()
    print("Starting the Main Function of this Scripts Running")

    user_1 = UserDetails(
        user_id_= random.randint(100,222),
        user_name_= (fake.name()).replace(" ", "_"),
        full_name_= fake.name(),
        is_allowed_= random.choice([True, False]),
        validity_= fake.date_time_between(start_date= datetime(2025,1,1,1,1,0), end_date= datetime(2025,7,1,1,1,0))
    )
    user_2 = UserDetails(
        user_id_= random.randint(100,222),
        user_name_= (fake.name()).replace(" ", "_"),
        full_name_= fake.name(),
        is_allowed_= random.choice([True, False]),
        validity_= fake.date_time_between(start_date= datetime(2025,1,1,1,1,0), end_date= datetime(2025,7,1,1,1,0))
    )
    user_3 = UserDetails(
        user_id_= random.randint(100,222),
        user_name_= (fake.name()).replace(" ", "_"),
        full_name_= fake.name(),
        is_allowed_= random.choice([True, False]),
        validity_= fake.date_time_between(start_date= datetime(2025,1,1,1,1,0), end_date= datetime(2025,7,1,1,1,0))
    )

    # print(UserDetails.get_all_users())
    user_1 = UserDetails(
        user_id_= 888,
        user_name_= "rana_uni",
        full_name_="Rana Universe",
        is_allowed_= True,
        validity_= datetime(2026,7,1,1,1,0))
    user_1.add_user_return_id_()




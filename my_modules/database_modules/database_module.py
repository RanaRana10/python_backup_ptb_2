

'''

Here will some special and needful database system
All Database Logic will stay here and if need more modules

here i have just made this for learing how to handle, 
bool, int, string, datetime obj with column, 
though it does not i understand fully to use.

Any Sugesstion Please Contact 🍌🍌🍌
Just For Testing For Rana Universe
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''




from datetime import datetime, timedelta
from pathlib import Path

from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Boolean, DateTime, Integer, String

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


'''🍌🍌🍌 Below my logic is starting 🍌🍌🍌'''

fake = Faker()



db_filename = "database_file.db"
folder_name = Path("RanaUniverse")
folder_name.mkdir(parents=True, exist_ok= True)
file_location = folder_name / db_filename

file_url = f"sqlite+pysqlite:///{file_location}"
engine = create_engine(url=file_url, echo= False)

Session = sessionmaker(bind= engine)
session = Session()

Base = declarative_base()




class UserInformation(Base):
    """
    A class to represent user information stored in the database.

    List of columns:
    - id_: it will automaic generate
    - user_id_: Integer representing the user's ID.
    - username_: String representing the user's username.
    - full_name_: String representing the user's full name.
    - is_allowed_: Boolean indicating whether the user is allowed.
    - validity_: DateTime indicating the validity of the user's account.
    - total_files_: Integer representing the total number of files associated with the user.

    This class provides a convenient way to interact with user information stored in the database.
    """

    __tablename__ = "user_informations"

    id_ = Column(Integer, primary_key= True)
    user_id_ = Column(Integer)
    username_ = Column(String)
    full_name_ = Column(String)
    is_allowed_ = Column(Boolean)
    validity_ = Column(DateTime)
    total_files_ = Column(Integer)


    def __init__(
            self,
            user_id_: int = None,
            username_: str = None,
            full_name_: str = None,
            is_allowed_: bool = None,
            validity_: datetime = None,
            total_files_: int = None,
    ):
        self.user_id_ = user_id_
        self.username_ = username_
        self.full_name_ = full_name_
        self.is_allowed_ = is_allowed_
        self.validity_ = validity_
        self.total_files_ = total_files_


    def __repr__(self):
        rana_string = (
            f"<UserInformation("
            f"id_={self.id_}, "
            f"user_id_={self.user_id_}, "
            f"username_={self.username_}, "
            f"full_name_={self.full_name_}, "
            f"is_allowed_={self.is_allowed_}, "
            f"validity_={self.validity_}, "
            f"total_files_={self.total_files_}"
            f")>"
        )
        return rana_string

    def delete_user_row_123(self):
        '''delete the row from my database'''
        session.delete(self)
        session.commit()

    def delete_user_row(self):
        '''Delete the row from the database. and return'''
        try:
            session.delete(self)
            session.commit()
            return True
        except Exception as e:
            print(f"Error deleting row from database: {e}")
            session.rollback()
            return False


    def add_user_only(self):
        '''This will just add a new row no information will output'''
        session.add(self)
        session.commit()

    def add_user_return_id_(self):
        '''This is the special and my favourite for one obj insert'''
        print(f"{self.full_name_} Has Just trying to join the database")
        session.add(self)
        session.commit()
        return self.id_


    def change_user_id_(self, new_user_id: int = None):
        '''Change the user_id value of any row.
        This is used for the cases when i will want to transfer
        any plan of a user to a new accouont
        '''
        self.user_id_ = new_user_id
        session.commit()
        return self.id_


    def change_username_123(self, new_username: str = None):
        '''This will change the username value of any row '''
        self.username_ = new_username
        session.commit()
        return self.username_

    def change_username_123(self, new_username: str = None):
        '''This will change the username value of any row '''
        self.username_ = new_username
        session.commit()
        return new_username
    
    def change_username_(self, new_username: str = None):
        '''This will change the username value of any row'''
        try:
            self.username_ = new_username
            session.commit()
            return self.username_
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return None


    def change_full_name_(self, new_fullname: str = None):
        '''Change the full name value of any row.'''
        self.full_name_ = new_fullname
        session.commit()
        return self.full_name_


    def change_is_allowed_(self, new_is_allowed: bool = None):
        '''Change the is_allowed value of any row.'''
        self.is_allowed_ = new_is_allowed
        session.commit()
        return self.is_allowed_


    def change_validity_(self, new_validity: datetime = None):
        '''Change the validity value of any row.'''
        self.validity_ = new_validity
        session.commit()
        return self.change_validity_


    def change_total_files_(self, new_total_files: int = None):
        '''Change the total_files value of any row.'''
        self.total_files_ = new_total_files
        session.commit()
        return self.total_files_


    def increase_total_files_(self, how_many_to_increase: int = 0):
        '''This will add the value and make the chages and save'''
        print("Before the update the value is", self.total_files_)
        self.total_files_ += how_many_to_increase
        session.commit()
        print("After the update the value is", self.total_files_)
        return self.total_files_


    def decrease_total_files_(self, how_many_to_decrease: int = 0):
        '''This will subtract the value and make the changes and save'''
        print("Before the update the value is", self.total_files_)
        self.total_files_ -= how_many_to_decrease
        session.commit()
        print("After the update the value is", self.total_files_)
        return self.total_files_


    def increase_and_decrease_total_files_(self, increase_count: int = 0, decrease_count: int = 0):
        '''No use, This will update the value and make the changes and save'''
        print("Before the update the value is", self.total_files_)
        self.total_files_ += increase_count
        self.total_files_ -= decrease_count
        session.commit()
        print("After the update the value is", self.total_files_)
        return self.total_files_


    def increase_validity_(self, how_many_time: timedelta = None):
        print("Before the update the value is", self.validity_)
        if how_many_time:
            self.validity_ += how_many_time
            session.commit()
            print("After the update the value is", self.validity_)
            return self.validity_
        else:
            print("No changes occurs as it is None")
            return None











Base.metadata.create_all(engine)






if __name__ == "__main__":

    '''Below dict is just for remember'''
    method_dict = {
        UserInformation.delete_user_row: "delete a user fullys",
        UserInformation.add_user_only: "Only add user, do nothing",
        UserInformation.add_user_return_id_: "Print the id_ after insert",
        UserInformation.change_user_id_: "Change user_id though no need, suppose a user changes his plan to new account",
        UserInformation.change_username_: "Change the username if it",
        UserInformation.change_full_name_: "Change his full name",
        UserInformation.change_is_allowed_: "is_allowed_ change",
        UserInformation.change_validity_: "Make the changes in the datetime obj",
        UserInformation.change_total_files_: "Changes for int learning 🍌 This is not good to use rather use below fun",
        UserInformation.increase_total_files_: "This will take the value and then increase this by plus",
        UserInformation.increase_and_decrease_total_files_: "This will do both on the parameter",
        UserInformation.increase_validity_: "add some date here"
    }
    
    
    fake_user_obj = UserInformation(
        user_id_= fake.random_int(100, 5000),
        username_= fake.user_name(),
        full_name_= fake.name(),
        is_allowed_= fake.boolean(),
        validity_= fake.future_datetime(datetime.now() + timedelta(days=5)),
        total_files_= 0
    )
    # fake_user_obj.add_user_return_id_()

    row_1_obj = session.query(UserInformation).filter(UserInformation.id_ == 1).first()

    # row_1_obj.update_total_files(80, 95)
    # row_1_obj.change_total_files_(99)
    # row_1_obj.increase_total_files(3)
    time_to_increase = timedelta(days= -1)
    # row_1_obj.increase_validity_(time_to_increase)
    row_1_obj.change_validity_(datetime(2000,1,1))




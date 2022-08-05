#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at =  datetime.datetime.now()


    def __str__(self):
        """ the string representation of the str object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__)
    def save(self):
        """
        updating the public instance attribute updated_at with the current 
        datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        result_dict = self.__dict__
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = strftime(%Y-%m-%dT%H:%M:%S.%f)
        result_dict["updated_at"] = strftime(%Y-%m-%dT%H:%M:%S.%f)

        return result_dict


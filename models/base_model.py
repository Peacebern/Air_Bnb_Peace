#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):

        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


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
        """
        :return: this returns a dictionary containing all keys/values of __dict__of the instance
        """
        result_dict = self.__dict__
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = result_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        result_dict["updated_at"] = result_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return result_dict


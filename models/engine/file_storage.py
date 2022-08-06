#!/usr/bin/python3
"""
file storage  file to save the python files in json file using dump
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(os.getcwd()).resolve()
# This is created so that so that the json file is created in the main directory directly rather than the engine directly


class FileStorage:
    """
    filestorage class to return j.son files
    """

    __file_path = BASE_DIR / "file.json"  # here the json file is created in the directory which path has been stored in BASE_DIR Variable
    __objects = {}  #here the __objects private class attribute stores the objects already created in the basemodel file in a dictionary

    def __init__(self):
        pass

    def all(self):
        """
        :return: the dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """

        :param obj:takes in the object dictionary and
        :return: the obj with key
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        this saves the dictionary which is in object form in the base model and then saves it in json file
        :return: uses the dump function to return the objects in json file
        """
        save_dict = {}

        if FileStorage.__objects:
            for key, value in FileStorage.__objects.items():
                save_dict[key] = value.to_dict()

            with open(FileStorage.__file_path, "w") as f:
                json.dump(save_dict, f)

    def reload(self):
        """

        :return:
        """
        if FileStorage.__file_path.exists():
            from models.base_model import BaseModel
            reload_dict = {}

            with open(FileStorage.__file_path, "r") as f:
                reload_dict = json.load(f)

                for key, value in reload_dict.items():
                    FileStorage.__objects[key] = BaseModel(**value)






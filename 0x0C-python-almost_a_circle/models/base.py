#!/usr/bin/python3
"""Base Class Module"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = self. __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON string
        representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries == []:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes the JSON string
        representation of list_objs to a file"""

        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))

        filename = str(cls.__name__ + ".json")

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """fuction  that returns the list of the JSON string
        representation json_string"""
        if not json_string or json_string == "":
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ function that returns a list of instances"""
        name = str(cls.__name__) + '.json'
        try:
            with open(name, 'r+', encoding='utf-8') as f:
                y = cls.from_json_string(f.read())
            ls = []
            for instance in y:
                ls.append(cls.create(**instance))
            return ls
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))

        filename = str(cls.__name__ + ".csv")

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new))

    @classmethod
    def load_from_file_csv(cls):
        if not json_string or json_string == "":
            json_string = "[]"
        return json.loads(json_string)
    """

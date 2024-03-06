#!/usr/bin/python3
"""
Defines a class named Base.
This class will be the base class of all other classes in this project.
"""


import json
import turtle


class Base:
    """
    Base class for all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor for the Base class.
        """
        # self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the json represenatation of an object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(
                cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
                )

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist

        list_dicts = cls.from_json_string(json_data)
        return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes objects to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    file.write(
                        f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n"
                        )
                elif cls.__name__ == "Square":
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            return []

        instances = []
        for line in lines:
            attrs = line.strip().split(",")
            if cls.__name__ == "Rectangle":
                instance = cls(
                    int(attrs[0]),
                    int(attrs[1]),
                    int(attrs[2]),
                    int(attrs[3]),
                    int(attrs[4])
                    )
            elif cls.__name__ == "Square":
                instance = cls(
                    int(attrs[0]),
                    int(attrs[1]),
                    int(attrs[2]),
                    int(attrs[3])
                    )
            instances.append(instance)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all the Rectangles and Squares using Turtle graphics module.
        """
        # Initialize turtle screen
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("white")
        screen.title("Rectangles and Squares")

        # Create turtle object
        pen = turtle.Turtle()

        # Draw rectangles
        pen.color("blue")
        pen.penup()
        for rectangle in list_rectangles:
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.penup()

        # Draw squares
        pen.color("red")
        pen.penup()
        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.penup()

        # Close screen when clicked
        screen.exitonclick()
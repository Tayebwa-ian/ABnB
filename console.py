#!/usr/bin/python3
"""The console Module
Description:
    This is provides shell like functionalities to run commands in this project
    More explicitly it provides a prompt to run basic commands
    commands that interact with the overall project
"""
import cmd
from models import (storage, User, City,
                    Amenity, Place, BaseModel, State, Review)


classes = {
    "User": User,
    "City": City,
    "Place": Place,
    "State": State,
    "BaseModel": BaseModel,
    "Review": Review,
    "Amenity": Amenity,
}


class HBNBCommand(cmd.Cmd):
    """Customised AirBnB console (command prompt)
    Description:
        Functions under this class run several commands input via the prompt
    """
    prompt = "(hbnb) "

    def do_quit(self, value) -> bool:
        """Exits the program"""
        return True

    def help_quit(self) -> None:
        """Text to display when help command in run with quit cmd"""
        print("Quit command to exit the program")

    def do_EOF(self, value) -> bool:
        """Exits the program"""
        return True

    def help_EOF(self) -> None:
        """Text to display when help command in run with EOF cmd"""
        print("EOF command to exit the program\n")

    def do_create(self, value) -> None:
        """Create an instance of the specified class saves it and print id
        Arg:
            value: the string containing the class and other needed value
        Return: None
        """
        if not value:
            print("** class name missing **")
        else:
            try:
                obj = classes[value]()
                obj.save()
                print(f"{obj.id}")
            except NameError:
                print("** class doesn't exist **")

    def help_create(self) -> None:
        """Text to display when help command in run with create cmd"""
        print("Create a new instance of a class "\
              "\nUsage: create User (creates a new user instance)")

    def do_show(self, value) -> None:
        """
        Description:
            Prints the string representation of an instance
            based on the class name and id
        Arg:
            value: the string containing the class and other needed value
        Return: None
        """
        temp_obj = value.split()
        if len(temp_obj) < 1:
            print("** class name missing **")
        elif len(temp_obj) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            # join the class name and id with a dot in middle
            key = ".".join(temp_obj)
            if key in all_obj.keys():
                new_obj = classes[temp_obj[0]](**all_obj[key])
                print(new_obj)
            else:
                try:
                    classes[temp_obj[0]]()
                    print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")

    def help_show(self) -> None:
        """Text to display when help command in run with show cmd"""
        print("Prints a string representation of an instance "\
              "\nUsage: show User user-id "\
              "(prints a str rep of a user instance)")

    def do_destroy(self, value) -> None:
        """
        Description:
            Delete an instance based on the class name and id
        Arg:
            value: the string containing the class and other needed value
        Return: None
        """
        temp_obj = value.split()
        if len(temp_obj) < 1:
            print("** class name missing **")
        elif len(temp_obj) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            # join the class name and id with a dot in middle
            key = ".".join(temp_obj)
            if key in all_obj.keys():
                del all_obj[key]
                for k in all_obj.keys():
                    classes[temp_obj[0]](**all_obj[k]).save()
            else:
                try:
                    classes[temp_obj[0]]()
                    print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")

    def help_destroy(self) -> None:
        """Text to display when help command in run with destroy cmd"""
        print("Delete an instance based on the class name and id "\
              "\nUsage: delete User user-id "\
              "(deletes user instance with id user-id)")

    def do_all(self, value) -> None:
        """
        Description:
            Prints all string representation of all instances
            based or not on the class name
        Arg:
            value: the string containing the class and other needed value
        Return: None
        """
        all_obj = storage.all()
        print_list = []
        if value:
            try:
                classes[value]
                for key in all_obj.keys():
                    cl = key.split(".")
                    if cl[0] == value:
                        # create object from all_obj dict and store in list
                        li = classes[cl[0]](**all_obj[key])
                        print_list.append(str(li))
            except KeyError:
                print("** class doesn't exist **")
        else:
            for key in all_obj.keys():
                cl = key.split(".")
                # create object from all_obj dict and store in list
                li = classes[cl[0]](**all_obj[key])
                print_list.append(str(li))
        if len(print_list) > 0:
            print(print_list)

    def help_all(self) -> None:
        """Text to display when help command in run with all cmd"""
        print("Prints all string representation of all instances "\
              "based or not on the class name \nUsage: all User "\
              "(print all str rep of User objects)")

    def do_update(self, value) -> None:
        """
        Description:
            Updates an instance based on the class name
            and id by adding or updating attribute
        Arg:
            value: the string containing the class and other needed value
        Return: None
        """
        temp_obj = value.split()
        if len(temp_obj) < 1:
            print("** class name missing **")
        elif len(temp_obj) < 2:
            print("** instance id missing **")
        elif len(temp_obj) < 3:
            print("** attribute name missing **")
        elif len(temp_obj) < 4:
            print("** value missing **")
        else:
            all_obj = storage.all()
            # join the class name and id with a dot in middle
            key = ".".join(temp_obj[:2])
            if key in all_obj.keys():
                all_obj[key][temp_obj[2]] = temp_obj[3]
                for k in all_obj.keys():
                    classes[temp_obj[0]](**all_obj[k]).save()
            else:
                try:
                    classes[temp_obj[0]]
                    print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")

    def help_update(self) -> None:
        """Text to display when help command in run with update cmd"""
        print("Updates an instance based on the class name "\
              "and id by adding or updating attribute "\
              "\nUsage: update User 1234-1234-1234 first_name IAN "\
              "(updates User with ID 1234-1234-1234 with "\
              "first_name attribute and value IAN)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

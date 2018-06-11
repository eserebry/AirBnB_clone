#!/usr/bin/python3
"""
Console for AirBnB clone
"""
import cmd
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand processor
    """
    prompt = ' (hbnb) '

    def do_EOF(self, line):
        """
        Method to exit with EOF command
        """
        return True

    def do_quit(self, line):
        """
        Method to exit with quit command
        """
        return True

    def check_class(cls):
        """
        Method helper to identify cls is valid
        """
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        for key, value in classes.items():
            if cls == key:
                return value
            else:
                return None

    def do_create(self, line):
        """
        Method creates new instance of obj
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] is None:
                print("** class name missing**")
            else:
                valid_cls = check_class(args[0])
                if valid_cls is not None:
                    instance = valid_class()
                    instance.save()
                    print(instance.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, line):
        """
        Method show str rep of instance using cls name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except Exception:
                print("** instance id missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:

if __name__ == '__main__':
    HBNBCommand().cmdloop()

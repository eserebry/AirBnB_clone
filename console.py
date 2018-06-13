#!/usr/bin/python3
"""
Console for AirBnB clone
"""
import cmd
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime



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
                    obj = storage.all()
                    key = str(args[0]) + '.' + str(args[1])
                    try:
                        print(obj[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Method destroys an instance
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except:
                print("** instance id missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:
                    obj = storage.all()
                    key = str(args[0]) + '.' str(args[1])
                    try:
                        del obj[key]
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """
        Method print str rep based on class name or not
        """
        args = line.split()
        obj = storage.all()
        counter = 0
        try:
            args[0]
            valid_class = check_class(args[0])
            if valid_class is None:
                print("** class doesn't exist **")
            for key in obj.keys():
                obj_class = (obj[k].__class__.__name__)
                if obj_class == args[0]):
                    print(obj[k])
                    counter++
            if counter == 0 and valid_class is not None:
                print([])
        except:
            for key in obj.keys():
                print(obj[key])
                counter++
            if counter == 0:
                print([])

    def do_update(self, line):
        """
        Method update values based on instance
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except:
                print("** instance id missing **")
            try:
                args[2]
            except:
                print("** attribute name missing **")
            try:
                args[3]
            except:
                print("** value missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:
                    obj = storage.all()
                    key = str(args[0]) + '.' + str(args[1])
                    try:
                        if args[3].isdigit():
                            args[3] = int(args[3])
                        else:
                            args[3] = args[3].replace('"', '')
                        setattr(obj[key], args[2], args[3])
                        setattr(obj[key], "updated_at", datetime.now())
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

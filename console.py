#!/usr/bin/python3
"""
Console for AirBnB clone
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand processor
    """
    prompt = ' (hbnb) '

    def do_greet(self, line):
        """
        REMOVE ME LATER
        """
        print ("hello")

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

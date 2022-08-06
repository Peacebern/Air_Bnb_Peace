#!/usr/bin/python3


import cmd

class HBNBCommand(cmd.Cmd):

    intro = "welcome to the AirBnB_CONSOLE"
    prompt = "(hbnb)"

    def do_quit(self, line): # do_quit is in to make sure the console recognizes the keyword quit.
        """
        returns true and quits the program
        ps: if you want the console to recognize a key word make it a method e.g think will be "def do_think"
        ps: "line" parameter is for fancy we put it in cause these kinds of methods accepts arguements
        """
        return True

    def do_EOF(self, line):
        """
        used to quit the console, used by ctrl + D
        """
        print("")   # this print func here is so that it prints on a new line when this error occurs
        return True
    def emptyline(self):
        pass
















if __name__ == '__main__':
    HBNBCommand().cmdloop()
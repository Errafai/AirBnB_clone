#!/usr/bin/python3
"""contains the console cmd interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    def do_quit(self, arg):
        """the command exist from the (hbnb) cmd"""
        return True

    def emptyline(self):
        """do nothing when an empty line is entred"""
        pass

    def do_EOF(self, arg):
        """exit when Ctrl+D is pressed"""
        return True








if __name__ == '__main__':
    HBNBCommand().cmdloop()

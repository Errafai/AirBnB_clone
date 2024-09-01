#!/usr/bin/python3
"""contains the console cmd interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """repsent the HBNBCommand class
    that define the console of the Airbnb clone"""

    prompt = "(hbnb) "

    def default(self, line):
        """handle command that are not exist"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        if "." in line:
            line = line.split(".")
            method = line[1].split("(")[0]
            method_arg = line[1].split("(")[1].split(")")[0]
            if method_arg is None or len(method_arg) == 0:
                return argdict[method](line[0])
            else:
                args = line[0] + " " + method_arg
                return argdict[method](args)
        else:
            return False

    def do_quit(self, arg):
        """the command exist from the (hbnb) cmd"""
        return True

    def emptyline(self):
        """do nothing when an empty line is entred"""
        pass

    def do_EOF(self, arg):
        """exit when Ctrl+D is pressed"""
        return True

    def do_create(self, arg):
        """create a new instance of the BaseModel class"""
        if arg is None or len(arg) == 0:
            print("** class name missing **")
        else:
            arg = arg.split()
            try:
                bm = eval(arg[0])()
                print(bm.id)
                storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """show the str representation of the instance"""
        if len(args) == 0 or args is None:
            print("** class name missing **")
            return

        args = args.split()

        if args[0] not in globals():
            print("** class doesn't exist **")
        else:
            try:
                if len(args) == 1:
                    print("** instance id missing **")
                    return

                obj = storage.all()
                inst_id = args[0] + "." + args[1]

                if inst_id in obj:
                    print(obj[inst_id])
                else:
                    print("** no instance found **")

            except IndexError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete an instance using the id and
        save changes to the json file"""
        arg = arg.split()
        if arg is None or len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            obj = storage.all()
            inst_id = arg[0] + "." + arg[1]
            if inst_id in obj:
                del obj[inst_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """print a list of all str representation
        of all instances of the class"""
        arg = arg.split()
        if len(arg) == 0 :
            obj = storage.all()
            list_insts = [obj[i].__str__() for i in obj]
            print(list_insts)
        elif arg[0] in globals():
            obj = storage.all()
            list_insts = [obj[i].__str__() for i in obj if arg[0] in i]
            print(list_insts)
        elif arg[0] not in globals():
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update the instance by adding new attrs
        to them specified in the arg"""

        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in globals():
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            inst_id = arg[0] + "." + arg[1]
            if inst_id not in obj:
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                setattr(obj[inst_id], arg[2], eval(arg[3]))
                storage.save()

    def do_count(self, line):
        """show all instance of a speefic class"""
        line = line.split()
        if line[0] not in globals():
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            i = 0
            for k in obj.keys():
                if line[0] in k:
                    i += 1
            print(i)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

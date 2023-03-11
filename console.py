#!/usr/bin/python3
"""
AirBnB v: 0.1 -> The Console v: 1.0
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage

model_type = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "State": State,
    "Amenity": Amenity,
    "Review": Review
}

err_msg = (
    "** class name missing **",
    "** class doesn't exist **",
    "** instance id missing **",
    "** no instance found **",
    "** attribute name missing **",
    "** value missing **",
)


class HBNBCommand(cmd.Cmd):
    """ simple command processor example. """

    prompt = "(hbnb) "

    def emptyline(self):
        """
         handle empty line + enter
        """
        pass

    def iserror(self, line, len_args):
        """
        handle arguments error
        """
        if not line:
            print(err_msg[0])
            return True
        args = line.split()

        if len_args >= 1 and args[0] not in model_type.keys():
            print(err_msg[1])
            return True
        elif len_args == 1:
            return False
        elif len_args >= 2 and len(args) < 2:
            print(err_msg[2])
            return True
        data = storage.all()

        """ remove all the \" """
        for i in range(1, len(args)):
            if args[i][0] == "\"":
                args[i] = args[i].replace("\"", "")
        key = f"{args[0]}.{args[1]}"

        if len_args >= 2 and key not in data.keys():
            print(err_msg[3])
            return True
        elif len_args == 2:
            return False
        if len_args >= 4:
            if len(args) < 3:
                print(err_msg[4])
                return True
            if len(args) < 4:
                print(err_msg[5])
                return True
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Argument:
            create <class name>
            e.g "create BaseModel"
        """
        if self.iserror(line, 1):
            return
        args = line.split()
        if args[0] in model_type.keys():
            object = model_type.get(args[0])()
            print(object.id)
            object.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        Arguments:
            <class name> <id>
            e.g show "BaseModel aaaa-bbbb-cccc-dddd"
        """
        if self.iserror(line, 2):
            return
        args = line.split()
        for i in range(1, len(args)):
            args[i] = args[i].replace("\"", "")
        key = f"{args[0]}.{args[1]}"
        object = storage.all().get(key)
        if object:
            print(str(object))

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name
        Example Usage:
            "all" or "all <class name>"
        """
        data = storage.all()
        if not line:
            print([
                str(value) for value in data.values()
            ])
            return
        if self.iserror(line, 1):
            return
        args = line.split()
        same_models = [
            str(value) for value in data.values()
            if args[0] == value.__class__.__name__
        ]
        print(same_models)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Arguments:
            <class name> <id>
            e.g destroy "BaseModel aaaa-bbbb-cccc-dddd"
        """
        if self.iserror(line, 2):
            return
        data = storage.all()
        args = line.split()
        key = f"{args[0]}.{args[1]}"
        if key in data.keys():
            del data[key]
        storage.save()

    def do_update(self, line):
        """
        updates an instance based on the class name and id by adding
        or updating attribute.

        Arguments:
            <class name> <id> <attribute name> <attribute value>
            e.g update "BaseModel aaaa-bbbb-cccc-dddd email
                \"example@host.com\""
        """
        if self.iserror(line, 4):
            return
        args = line.split()
        data = storage.all()
        # attributes that can't be updated
        nattributes = (
            "id", "created_at", "updated_at"
        )
        key = f"{args[0]}.{args[1]}"

        """ remove \" from arguments"""
        for i in range(1, len(args)):
            if args[i][0] == "\"":
                args[i] = args[i].replace("\"", "")
        attr_name = args[2]
        attr_value = args[3]

        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif float(attr_value):
                attr_value = float(attr_value)
        except ValueError:
            pass
        if attr_name not in nattributes:
            setattr(data[key], attr_name, attr_value)
        storage.save()

    def do_EOF(self, line):
        """ EOF: Quits command with ctrl+d """
        return True

    def do_quit(self, line):
        """ quit command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

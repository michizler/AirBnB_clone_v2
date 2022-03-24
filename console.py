#!/usr/bin/python3
""" Console Module """
import cmd
import re
import sys

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] is '{' and pline[-1] is '}' \
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, arg):
        """ Create an object of any class
            Usage: create <Class name> <param 1> <param 2> <param 3>...
        """
        if arg:
            try:
                args = arg.split()
                template = models.dummy_classes[args[0]]
                new_instance = template()
                try:
                    for pair in args[1:]:
                        pair_split = pair.split("=")
                        if (hasattr(new_instance, pair_split[0])):
                            value = pair_split[1]
                            flag = 0
                            if (value.startswith('"')):
                                value = value.strip('"')
                                value = value.replace("\\", "")
                                value = value.replace("_", " ")
                            elif ("." in value):
                                try:
                                    value = float(value)
                                except:
                                    flag = 1
                            else:
                                try:
                                    value = int(value)
                                except:
                                    flag = 1
                            if (not flag):
                                setattr(new_instance, pair_split[0], value)
                        else:
                            continue
                    new_instance.save()
                    print(new_instance.id)
                except:
                    new_instance.rollback()
            except:
                print("** class doesn't exist **")
                models.storage.rollback()
        else:
            print("** class name missing **")

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        """ Method to show an individual object """
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        print(models.storage.all()[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, arg):
        """ Destroys a specified object """
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        garbage = models.storage.all().pop(key)
                        del (garbage)
                        models.storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, arg):
        """ Shows all objects, or all objects of a class"""
        result = []
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                current_inst = models.dummy_classes[arg[0]]
                for i, o in models.storage.all(current_inst).items():
                    if i.split('.')[0] == arg[0]:
                        result.append(str(o))
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models.storage.all().items():
                result.append(str(obj))
        if result:
            print(result)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, arg):
        """Count current number of class instances"""
        count = 0
        if arg:
            arg = arg.split()
            if arg[0] in models.dummy_classes:
                for instance, obj in models.storage.all().items():
                    if instance.split('.')[0] == arg[0]:
                        count += 1
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models.storage.all().items():
                count += 1
        print(count)


def help_count(self):
    """ """
    print("Usage: count <class_name>")


def do_update(self, arg):
    """ Updates a certain object with new info """
    if arg:
        arg = arg.split()
        if arg[0] in models.dummy_classes:
            if len(arg) > 1:
                key = "{}.{}".format(arg[0], arg[1])
                try:
                    instance = models.storage.all()[key]
                    if len(arg) > 2:
                        if len(arg) > 3:
                            setattr(instance, arg[2], arg[3].strip('"'))
                            instance.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                except:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    else:
        print("** class name missing **")


def help_update(self):
    """ Help information for the update class """
    print("Updates an object with new information")
    print("Usage: update <className> <id> <attName> <attVal>\n")


def default(self, line):
    """
    handle invalid commands and
    special commands like <class name>.<command>()
    """
    match = re.fullmatch(r"[A-Za-z]+\.[A-Za-z]+\(.*?\)", line)
    if match:
        splited = line.split('.')
        if splited[0] in models.dummy_classes:
            parsed = splited[1].split("(")
            parsed[1] = parsed[1].strip(")")
            args = parsed[1].split(",")
            args = [arg.strip() for arg in args]
            if len(args) >= 3:
                temp = args[2]
                args = [arg.strip('"') for arg in args[:2]]
                args.append(temp)
            else:
                args = [arg.strip('"') for arg in args]
            command = self.fetch_command(parsed[0])
            if command:
                reconstructed_args = [arg for arg in args]
                reconstructed_args.insert(0, splited[0])
                reconstructed_command = " ".join(reconstructed_args)
                command(self, reconstructed_command)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("** class doesn't exist **")
    else:
        print("*** Unknown syntax: {}".format(line))

    def help_default(self):
        """ Help information for the default class """
        print("handle invalid commands")
        print("Usage: default <class name>.<command>()\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

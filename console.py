#!/usr/bin/python3
'Console program'
import cmd
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel}

class HBNBCommand(cmd.Cmd):
    'hbnb command interpreter'
    prompt = '(hbnb) '


    def do_quit(self, s):
        'Exits the shell'
        exit()

    def do_EOF(self, s):
        'Exits the shell'
        exit()

    def do_create(self, args):
        'create instance of basemodel, saves it'
        args = args.split()
        if args is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes.get(args[0])()
            print(new_instance.id)
            storage.save(new_instance)

    def do_show(self, args):
        'print string repr of an instance based on class name'
        args = args.split()
        'expecting: args = [name, name_id]'
        if len(args) != 2:
        # if args[0] is None:
            print("** class name missing **")
        # elif args[1] is None:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            try:
                print(args[1])
            except:
                print("++ no instance found ++")

    def emptyline(self):
        'emptyline method - does nothing'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

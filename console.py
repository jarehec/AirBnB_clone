#!/usr/bin/python3
'Console program'
import cmd


class HBNBCommand(cmd.Cmd):
    'hbnb command interpreter'
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'FileStorage': FileStorage}

    def do_quit(self, s):
        'Exits the shell'
        exit()

    def do_EOF(self, s):
        'Exits the shell'
        exit()

    def do_create(self, name):
        'create instance of basemodel, saves it'
        if name is None:
            print("** class doesn't exist **")
        elif name is not "BaseModel":
            print("** class name missing **")
        else:
            new_instance = name
            print(new_instance.id)
            FileStorage.save(new_instance)

    def do_show(self, name, name_id):
        'print string repr of an instance based on class name'
        if name is None:
            print("** no instance found **")
        elif name_id is None:
            print("** instance id missing **")
        elif name.__class__ is None:
            print("** class doesn't exist **")
        else:
            print(name)

    def emptyline(self):
        'emptyline method - does nothing'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
'Console program'
import cmd


class HBNBCommand(cmd.Cmd):
    'hbnb command interpreter'
    prompt = '(hbnb) '

    def do_quit(self, s):
        'Exits the shell'
        exit()

    def do_EOF(self, s):
        'Exits the shell'
        exit()

    def emptyline(self):
        'emptyline method - does nothing'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

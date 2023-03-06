#!/usr/bin/python3
"""
AirBnB v: 0.1 -> The Console v: 0.01
Contains entry point of the command interpreter
"""

import cmd


class CmdConsole(cmd.Cmd):
    """ simple command processor example. """

    prompt = "(hbnb)"

    def do_create(self, line):
        """
        create a new instance of @classname class,
        and print its ID.
        """
        pass

    def do_destroy(self, line):
        """
        destroys an instance
        """
        pass

    def do_all(self, line):
        """
        print all objects
        """
        pass

    def do_show(self, line):
        """
        used to display a specific object
        """
        pass

    def do_EOF(self, line):
        """ EOF: Quits command with ctrl+d """
        return True

    def do_quit(self, line):
        """ handle 'quit' command """
        return True


if __name__ == '__main__':
    CmdConsole().cmdloop()

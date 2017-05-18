import logging
import cmd, sys
import pprint
import shlex
from christie_projectors import ChristieProjector

logging.basicConfig(filename='logging.log',level=logging.DEBUG)

projectors = {}

class controlSession(cmd.Cmd):
    intro = "Christie Projector Control - Type 'help' for command info"
    prompt = ('Projector: ')
    file = None

    def do_add(self, arg):
        """Add projector add '192.168.0.xxx"""
        ip = arg
        proj = ChristieProjector(ip)
        if projectors.get(ip):
            print('error projector already exists')
        else:
            projectors[ip] = proj

    def do_remove(ip):
        pass

    def do_send_to(self, arguments):
        """Send telnet command to projector command 192.168.0.xxx 'telnet-command'"""
        args = shlex.split(arguments)
        ip = args[0]
        command = args[1]
        proj = projectors.get(ip)
        proj.sendCommand(command)

    def do_show_projectors(self, arg):
        for proj in projectors.keys():
            pprint.pprint(proj)

    def do_bye(self, arg):
        try:
            return True  
        except Exception as e:
            raise e
    

    def save_projectors(self):
        pass


if __name__ == '__main__':
    controlSession().cmdloop()
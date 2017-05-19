import logging
import cmd, sys
import pprint
import shlex
import pickle
import os
import time

try:
    import readline
    import rlcompleter
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except ImportError:
    print("Module readline not available")

from christie_telnet import christie_telnet

SEND_COMMANDS = christie_telnet.commands.keys()

from christie_projectors import ChristieProjector

projectors = {}
logging.basicConfig(filename='logging.log',level=logging.DEBUG)

#self.projectors = {}

class controlSession(cmd.Cmd):
    intro = "Christie Projector Control - Type 'help' for command info"
    prompt = ('Projector: ')
    file = None        
    
    def __init__(self):
        cmd.Cmd.__init__(self, completekey='tab', stdin=None, stdout=None)
        self.projectors = {}

    def do_add(self, arg):
        """Add projector add '192.168.0.xxx"""
        ip = arg
        proj = ChristieProjector(ip)
        if projectors.get(ip):
            print('error projector already exists')
        else:
            self.projectors[ip] = proj

    def do_remove(self, ip):
        self.projectors.pop(ip, None)

    def do_start_aligning(self, args):
        color = 1
        for ip in self.projectors.keys():
            proj = self.projectors[ip]
            proj.sendCommand('(CLE %s)'%color)
            proj.sendCommand('(CLE %s)'%color)
            color = color + 1
            proj.sendCommand('(ITP 1)') 
            proj.sendCommand('(ITP 1)')

    def do_stop_aligning(self, args):
        for ip in self.projectors.keys():
            proj = self.projectors[ip]
            proj.sendCommand('ITP 0')
            proj.sendCommand('ITP 0')
            proj.sendCommand('CLE 7')
            proj.sendCommand('CLE 7')

    def do_save(self, args):
        with open('%s.obj'%args, 'wb') as fp:
            pickle.dump(self.projectors, fp)

    def do_open(self, args):
        with open('%s.obj'%args, 'rb') as fp:
            self.projectors = pickle.load(fp)

    def do_send(self, args):
        """Send telnet command to projector command 192.168.0.xxx 'telnet-command'
            Commands available 
            $s"""
        (ip, command) = shlex.split(args)
        proj = projectors.get(ip)
        proj.sendCommand(command)

    def complete_send(self, text, line, begidx, endidx):
        return [i for i in SEND_COMMANDS if i.startswith(text)]

    def do_send_stack(self, args):
        try:
            (stack, command) = shlex.split(args)
        except:
            (stack, command) = None, None
        for ip in self.projectors.keys():
            proj = self.projectors[ip]
            if proj.stack == int(stack):
                proj.sendCommand(command)

    def do_list(self, arg):
        for proj in self.projectors.keys():
            pprint.pprint(proj)

    def do_bye(self, arg):
        self.do_save('BACKUP')
        try:
            return True  
        except Exception as e:
            raise e
    


if __name__ == '__main__':
    controlSession().cmdloop()
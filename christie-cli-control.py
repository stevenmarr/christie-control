ip_list = {
1:[
'111',
'112',
'113'],
2:[
'121',
'122',
'123'],
3:[
'131',
'132',
'133']
}


subnet = '192.168.0.'

from telnetlib import Telnet
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("telnet_command", 
        help = """
        Command list: 
        'test-pattern-off', 'test-pattern-grid', 'test-pattern-greyscale', 
        'test-pattern-white', 'test-pattern-gray', 'test-pattern-white', 
        """)
    parser.add_argument("stack", 
        help = "projector stack to address 0 for all", 
        type = int)
    args = parser.parse_args()
    telnet_lookup(args.telnet_command, args.stack)


def telnet_lookup(command, stack):
    cle_number = 2
    if stack == 0:
        keys = ip_list.keys()
    else: keys = [stack]
    for key in keys:
        for ip in ip_list[key]:
            ip = ('%s%s'%(subnet,ip), 3002)
            if command == 'test-pattern-off':
                telnet_commands = ['ITP 0']
            elif command == 'test-pattern-grid':
                telnet_commands = ['ITP 1']
            elif command == 'test-pattern-greyscale':
                telnet_commands = ['ITP 2']
            elif command == 'test-pattern-white':
                telnet_commands = ['ITP 3']
            elif command == 'test-pattern-grey':
                telnet_commands = ['ITP 4']
            elif command == 'test-pattern-white':
                telnet_commands = ['ITP 5']
                print(hello)
            elif command == 'alignment-tests-go':
                cle_number = cle_number + 1
                telnet_commands = ['%s %s'%('CLE', (cle_number%3)+1), 'ITP 1']
            elif command == 'alignment-tests-stop':
                telnet_commands = ['CLE 0', 'ITP 0']
            elif command == 'shutter-projectors':
                telnet_commands = ['SHU 0']
            elif command == 'unshutter-projectors':
                telnet_commands = ['SHU 1']
            elif command == 'ping':
                telnet_commands = []
                ping_projector(ip)
            else:
                telnet_commands = [command]
            #tn.close
        if telnet_commands:
            print_telnet (ip, telnet_commands)

def print_telnet(ip, telnet_commands):
    print (telnet_commands)
    #tn = Telnet('%s%s'%(subnet,ip), 3002)
    for telnet_command in telnet_commands:
        #print (ip, telnet_command)
        
        try:
            tn = Telnet('%s%s'%(subnet,ip), 3002)
            tn.write(telnet_command)
        except Exception as e:
            print(e, ip)

def ping_projector(ip):
    print ("Ping ", ip)

if __name__ == '__main__':
    main()
from telnetlib import Telnet
import argparse
import os

ip_list = {
1:[
'111',
'112'],
2:[
'121',
'122'],
3:[
'131',
'132'],
4:[
'141',
'142'],
5:[
'151',
'152'],
6:[
'161',
'162'],
8:[
'181',
'182']
}

subnet = '192.168.0.'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("telnet_command", 
        help = """
        Command list: 
        *** Frame ****
        'set-frame-delay-2f', 'set-frame-delay-default',

        *** Test Patterns ***
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
    telnet_commands = []
    if stack == 0:
        keys = ip_list.keys()
    else: keys = [stack]
    for key in keys:
        telnet_commands = []
        for ip in ip_list[key]:
            telnet_commands = []
            ip = '%s%s'%(subnet,ip)
            if command == 'test-pattern-off':
                telnet_commands.append('(ITP 0)')
            elif command == 'set-frame-delay-3f':
                telnet_commands.append('(FRD 3000)')
            elif command == 'set-red':
                telnet_commands.append('(CLE 1)')
            elif command == 'set-green':
                telnet_commands.append('(CLE 2)')
            elif command == 'set-frame-delay-default':
                telnet_commands.append('(FRD 1000)')
            elif command == 'test-pattern-grid':
                telnet_commands.append('(ITP 1)')
            elif command == 'test-pattern-greyscale':
                telnet_commands.append('(ITP 2)')
            elif command == 'test-pattern-white':
                telnet_commands.append('(ITP 3)')
            elif command == 'test-pattern-grey':
                telnet_commands.append('(ITP 4)')
            elif command == 'test-pattern-white':
                telnet_commands.append('(ITP 5)')
            elif command == 'alignment-tests-go':
                cle_number = cle_number + 1
                telnet_commands.append('(%s %s)'%('CLE', (cle_number%5)+1))
                telnet_commands.append('(ITP 1)')
            elif command == 'alignment-tests-stop':
                telnet_commands.append('(CLE 0)')
                telnet_commands.append('(ITP 0)')
            elif command == 'unshutter':
                telnet_commands.append('(SHU 0)')
            elif command == 'shutter':
                telnet_commands.append('(SHU 1)')
            elif command == 'power-off':
                telnet_commands.append('(PWR 0)')
            elif command == 'power-on':
                telnet_commands.append('(PWR 1)')
            elif command == 'ping':
                telnet_commands.append(None)
                ping_projector(ip)
            else:
                telnet_commands.append([command])
            #tn.close
            if telnet_commands:
                print_telnet (ip, telnet_commands)

def print_telnet(ip, telnet_commands):
    #print (telnet_commands)
    #tn = Telnet('%s%s'%(subnet,ip), 3002)
    for telnet_command in telnet_commands:
        try:
            tn = Telnet(ip, 3002, 1)
            tn.write(telnet_command)
        except Exception as e:
            print(e, ip)

def ping_projector(ip):
    
    print ("************************************************")
    ip_status_list = []
    os.system("stty -echoctl")
    response = os.system("ping -t 1 " + ip)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    #ip_status_list.append("IP %s condition is %s"%(ip, pingstatus))
    #for status in ip_status_list:
    print (pingstatus)
    print ("Ping ", ip)

if __name__ == '__main__':
    main()
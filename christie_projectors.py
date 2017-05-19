import logging
import time

from christie_telnet import christie_telnet
from telnetlib import Telnet

TIMEOUT = 0.7

logging.basicConfig(filename='obj_file.log',level=logging.DEBUG)

class ChristieProjector(object):
    """Christie Projector object

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, IP, blend=None, style='J', PORT=3002):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            IP (str): IP address of projector ex. '192.168.0.111'
            style (str, optional): Model type default = 'J'
            port (int, optional): Projector port default = 3002

        """
        self.ip = IP
        try:
            self.stack = int(IP[-2])
        except:
            self.stack = 9
        self.blend = blend
        self.style = style
        self.port = PORT

    def sendCommand(self, input_command):
        command = christie_telnet.commands.get(input_command, '(%s)'%input_command)
        self.__sendTelnetCommand(command)

    def sendQuery(self, query):
        pass

    def __sendTelnetCommand(self, command):
        """send telnet command and return response"""
        #print("telnet", command)
        try:
            tn = Telnet(self.ip, self.port, TIMEOUT)
            tn.write(command)
            response = tn.read_eager()
            logging.info('Sent telnet command %s, %s:%s \
                and received response %s',
                command, self.ip, self.port, response)
            time.sleep(.3)
            tn.close()
        except Exception as e:
            logging.error('Error sending telnet command %s to %s:%i - %s',
                command, self.ip, self.port, e)


"""The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

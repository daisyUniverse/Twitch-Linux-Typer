from socket import socket
import random
import json

with open('config.json', 'r') as f:
  config = json.load(f)

class Chat:

    def __init__(self):

        self.socket = socket()
        self.socket.connect(('irc.twitch.tv', 6667))
        nick = (config['NICK']+str(random.randint(1000,9999)))

        self.socket.send(("PASS "  + config['PASS'] +       "\n").encode('utf-8'))
        self.socket.send(("NICK "  + nick +                 "\n").encode('utf-8'))
        self.socket.send(("JOIN #" + config['CHANNEL'] +    "\n").encode('utf-8'))

        loading = True

        while loading:
            read_buffer_join = self.socket.recv(1024)
            read_buffer_join = read_buffer_join.decode()

            for line in read_buffer_join.split('\n')[0:-1]:
                print(line)
                loading = 'End of /NAMES list' not in line

    def listen(self) -> (str, str):
        read_buffer = self.socket.recv(1024).decode()
        for line in read_buffer.split('\r\n'):
            if 'PING' in line and 'PRIVMSG' not in line:
                self.socket.send('PONG tmi.twitch.tv\r\n'.encode())

            elif line != '':
                parts = line.split(':', 2)
                return parts[1].split('!', 1)[0], parts[2] 


from socket import socket

config = {
    "PASS" : "PUT YOUR OAUTH HERE (oauth: part included)",
    "NICK" : "Whatever you want your bot's nick to be",
    "CHANNEL": "The target channel you want to listen to"
}

class Chat:

    def __init__(self):

        self.socket = socket()
        self.socket.connect(('irc.twitch.tv', 6667))

        self.socket.send(("PASS "+config['PASS']+"\n").encode('utf-8'))
        self.socket.send(("NICK "+config['NICK']+"\n").encode('utf-8'))
        self.socket.send(("JOIN #"+config['CHANNEL']+"\n").encode('utf-8'))

        loading = True

        while loading:
            read_buffer_join = self.socket.recv(1024)
            read_buffer_join = read_buffer_join.decode()

            for line in read_buffer_join.split('\n')[0:-1]:
                loading = 'End of /NAMES list' not in line

    def listen(self) -> (str, str):
        read_buffer = self.socket.recv(1024).decode()
        for line in read_buffer.split('\r\n'):
            if 'PING' in line and 'PRIVMSG' not in line:
                self.socket.send('PONG tmi.twitch.tv\r\n'.encode())

            elif line != '':
                parts = line.split(':', 2)
                return parts[1].split('!', 1)[0], parts[2] 


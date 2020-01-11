import socket


class SystemInfo:

    def __init__(self):
        self.username = None

    
    def get_username(self):
        self.username = socket.gethostname()
        return self.username


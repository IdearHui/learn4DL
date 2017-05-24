# coding=utf-8
class Connections(object):
    """
    提供Connection集合操作
    """
    def __init__(self):
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def dump(self):
        for conn in self.connections:
            print conn

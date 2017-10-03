import asyncio
import sys

TELNET_EOL = '\r\n'


class ChatRoom:

    def __init__(self, name, port, loop):
        self._name = name
        self._port = port
        self._loop = loop
        self._username_streams = {}

    @property
    def name(self):
        return self._name

    def run(self):
        coro = asyncio.start_server(
            client_connected_cb=self.client_connected,
            host='',
            port=self._port
        )
        return self._loop.run_until_complete(coro)

    async def client_connected(self, reader, writer):
        writeline(writer, f'Welcome to {self.name}')
        registered_user = await self.user_registration(reader, writer)
        if registered_user:
            self.user_arrived(registered_user)
            await self.user_activity(registered_user, reader, writer)
            self.deregister_user(registered_user)
        await writer.drain()

    def user_departed(self, registered_user):
        self.broadcast(f'User {registered_user} departed.')

    def user_arrived(self, registered_user):
        self.broadcast(f'User {registered_user} arrived.')

    async def user_registration(self, reader, writer):
        while True:
            write(writer, 'Enter user name: ')
            data = await reader.readline()
            if not data:
                return None
            try:
                line = data.decode('utf-8')
            except UnicodeDecodeError as e:
                write(writer, str(e))
            else:
                username = line.strip()
                if self.register_user(username, reader, writer):
                    return username

    async def user_activity(self, username, reader, writer):
        while True:
            data = await reader.readline()
            if not data:
                return None
            try:
                line = data.decode('utf-8')
            except UnicodeDecodeError as e:
                write(writer, str(e))
            else:
                self.interpret_line(line.strip(), username, writer)

    def interpret_line(self, line, username, writer):
        if line == 'NAMES':
            self.list_users(writer)
        else:
            self.message_from(username, line)

    def register_user(self, username, reader, writer):
        if username in self.users():
            writeline(writer, f'Username {username} not available.')
            return False
        self._username_streams[username] = (reader, writer)
        return True

    def deregister_user(self, username):
        del self._username_streams[username]
        self.broadcast(f'User {username} departed.')

    def list_users(self, writer):
        writeline(writer, 'Users here:')
        for username in self.users():
            writeline(writer, ' {username}')

    def users(self):
        return self._username_streams.keys()

    def message_from(self, username, message):
        self.broadcast(f'{username}: {message}')

    def broadcast(self, message):
        for _, writer in self._username_streams.values():
            writeline(writer, message)


def writeline(writer, line):
    write(writer, line)
    write(writer, TELNET_EOL)


def write(writer, text):
    writer.write(text.encode('utf-8'))


def main(argv):
    name = argv[1] if len(argv) >= 2 else "Chatterbox Streams"
    port = int(argv[2]) if len(argv) >= 3 else 1234
    loop = asyncio.get_event_loop()
    chat_room = ChatRoom(name, port, loop)
    chat_room.run()
    loop.run_forever()


if __name__ == '__main__':
    main(sys.argv)

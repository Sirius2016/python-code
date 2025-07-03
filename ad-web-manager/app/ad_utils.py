from ldap3 import Server, Connection, ALL, NTLM

class ActiveDirectoryManager:
    def __init__(self, server_address, domain, username, password):
        self.server_address = server_address
        self.domain = domain
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        server = Server(self.server_address, get_info=ALL)
        self.connection = Connection(server, f"{self.domain}\\{self.username}", self.password, auto_bind=True)

    def add_user(self, username, password, first_name, last_name, email):
        user_dn = f"CN={username},OU=Users,DC={self.domain},DC=com"
        self.connection.add(user_dn, 'user', {'givenName': first_name, 'sn': last_name, 'mail': email})
        self.connection.extend.microsoft.add_password(user_dn, password)

    def delete_user(self, username):
        user_dn = f"CN={username},OU=Users,DC={self.domain},DC=com"
        self.connection.delete(user_dn)

    def close(self):
        if self.connection:
            self.connection.unbind()
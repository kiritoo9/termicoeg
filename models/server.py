from dataclasses import dataclass

@dataclass
class Server:
    servername: str
    hostname: str
    username: str
    password: str
    port: str
    description: str

    def to_dict(self):
        return {
            "servername": self.servername,
            "hostname": self.hostname,
            "username": self.username,
            "password": self.password,
            "port": self.port,
            "description": self.description
        }
import json

class Storages:
    filepath: str = "storages/database.json" # storage of list servers

    def init(self, data: list = []):
        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)


    def loads(self):
        server_list = None
        with open(self.filepath, "r") as file:
            server_list = json.load(file)
        return server_list

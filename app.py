import pexpect
import pyfiglet
from rich.console import Console
from rich.table import Table

from models.server import Server
from services.storages import Storages

class Termicoeg:

    def user_input(self):
        console = Console()

        # ask user for input
        console.print("\n[cyan]You have no server on database, please input your first server:[/] ")
        servername = console.input("\n[magenta]Server name*[/]: ")
        hostname = console.input("[magenta]Hostname*[/]: ")
        username = console.input("[magenta]Username*[/]: ")
        password = console.input("[magenta]Password*[/]: ")
        port = console.input("[magenta]Port[/]: ")
        description = console.input("[magenta]Description[/]: ")

        if hostname == "" and username == "" and password == "":
            console.print("\n[red]Make sure you input field with star bro![/]")
            return None
        else:
            # append into server_lists
            return Server(
                servername=servername,
                hostname=hostname,
                username=username,
                password=password,
                port=port,
                description=description
            )


    def init(self):
        try:
            console = Console()

            # print welcome message
            welcome_message = pyfiglet.figlet_format("TERMICOEG!", font="slant")
            console.print("[cyan]" + welcome_message + "[/]")

            # list of server:storage
            storages = Storages()
            server_lists = storages.loads()

            # ask for server choosed
            use_existing: bool = False
            server_choosed: Server = None

            if server_lists is None:
                server_choosed = self.user_input()
            else:
                table = Table(title="List of your servers")
                table_columns = ["Server Name", "Hostname", "Notes"]
                for i in range(len(table_columns)):
                    table.add_column(table_columns[i], style="magenta")

                for i in range(len(server_lists)):
                    table.add_row(server_lists[i].get("servername"), server_lists[i].get("hostname"), server_lists[i].get("description"))
                table.add_row("new", "-- ADD NEW SERVER --", "TYPE 'new' TO ADD NEW SERVER")
                console.print(table)

                # ask users for wich server they want to connect
                input_servername: str = console.input("\nPut [bold red]Server Name[/] you want to connect: ")
                for i in range(len(server_lists)):
                    if input_servername == server_lists[i].get("servername"):
                        server_choosed = Server(
                            servername=server_lists[i].get("servername"),
                            hostname=server_lists[i].get("hostname"),
                            username=server_lists[i].get("username"),
                            password=server_lists[i].get("password"),
                            port=server_lists[i].get("port"),
                            description=server_lists[i].get("description"),
                        )
                        use_existing = True
                        break
                
                # check if user try to add new server
                if input_servername == "new":
                    server_choosed = self.user_input()

            # re-write server lists
            if use_existing is False and server_choosed is not None:
                server_lists.append(server_choosed.to_dict())
                storages.init(server_lists)

            # run
            if server_choosed is not None:
                child = pexpect.spawn(f'ssh {server_choosed.username}@{server_choosed.hostname} -p {server_choosed.port}')
                child.expect('password:')
                child.sendline(server_choosed.password)
                child.interact()
            else:
                console.print("[bold red]No server choosed[/]")
        except Exception as e:
            print(e)


app = Termicoeg()
app.init()
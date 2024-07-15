import typer

from cli.commands import server, index


app = typer.Typer(name="suchak")

app.add_typer(server.app, name="server")
app.add_typer(index.app, name="index")

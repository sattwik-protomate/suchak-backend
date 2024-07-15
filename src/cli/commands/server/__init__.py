import typer

from cli.commands.server.run import run


app = typer.Typer()


app.command(name="run")(run)

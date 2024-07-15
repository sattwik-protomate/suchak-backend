import typer

from cli.commands.index.all import all


app = typer.Typer()


app.command(name="all")(all)

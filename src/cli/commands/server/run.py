import typer
from typing_extensions import Annotated
from typing import Optional

import rich


def run(
    port: Annotated[
        Optional[int],
        typer.Argument(help="The port to start the server on"),
    ] = 8080
) -> None:
    """
    Runs the server.
    """
    rich.print(f"Started server on port {port}")

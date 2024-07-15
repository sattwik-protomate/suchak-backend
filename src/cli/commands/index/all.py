import rich.status
import typer
from typing_extensions import Annotated
from typing import List

import rich
from rich.console import Console

import time


def all(
    doc_paths: Annotated[
        List[str], typer.Argument(help="The path to the folder containing the documents")
    ]
) -> None:
    console = Console()
    console.log("Starting document indexing...", style="cyan")
    for path in doc_paths:
        with console.status(status="Indexing documents", spinner="dots12") as status:
            console.log(f"Indexing `{path}`")
            time.sleep(1)
            console.log("Done", style="bright_green")

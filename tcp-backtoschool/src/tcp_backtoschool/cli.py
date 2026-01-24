"""Console script for tcp_backtoschool."""

import typer
from rich.console import Console

from . import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for tcp_backtoschool."""
    console.print("Replace this message by putting your code into tcp_backtoschool.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")

    utils.back_to_school()

    console.print("DEBUG Done.")


if __name__ == "__main__":
    app()

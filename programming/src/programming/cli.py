"""Console script for tcp_backtoschool."""

import typer
from rich.console import Console
from rich.table import Table

from .programs import PROGRAMS, get_program

app = typer.Typer()
console = Console()


def display_menu() -> None:
    """Display the program menu in 3 columns."""
    console.print("\n[bold cyan]Pick a program to run (1-30):[/bold cyan]\n")

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Col1", style="white", width=30)
    table.add_column("Col2", style="white", width=30)
    table.add_column("Col3", style="white", width=30)

    # Arrange programs in 3 columns (10 rows)
    num_rows = 10
    for row in range(num_rows):
        cols = []
        for col in range(3):
            idx = row + col * num_rows
            if idx < len(PROGRAMS):
                prog = PROGRAMS[idx]
                cols.append(f"[green]{prog.id:2}.[/green] {prog.name}")
            else:
                cols.append("")
        table.add_row(*cols)

    console.print(table)
    console.print()


@app.command()
def main(
    program: int = typer.Argument(None, help="Program number to run (1-30)"),
) -> None:
    """TCP Back to School - Challenge Runner.

    Run without arguments to see the menu, or pass a program number directly.
    """
    if program is None:
        display_menu()
        try:
            choice = console.input("[bold yellow]Enter program number (or 'q' to quit): [/bold yellow]")
            if choice.lower() == "q":
                console.print("[dim]Goodbye![/dim]")
                raise typer.Exit()
            program = int(choice)
        except ValueError:
            console.print("[red]Invalid input. Please enter a number between 1 and 30.[/red]")
            raise typer.Exit(code=1) from None

    selected = get_program(program)
    if selected is None:
        console.print(f"[red]Invalid program number: {program}. Please choose 1-30.[/red]")
        raise typer.Exit(code=1)

    console.print(f"\n[bold]Running: {selected.name}[/bold]")
    console.print(f"[dim]{selected.description}[/dim]\n")

    try:
        selected.run()
    except Exception as e:
        console.print(f"[red]Error running program: {e}[/red]")
        raise typer.Exit(code=1) from e


if __name__ == "__main__":
    app()

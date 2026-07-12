"""Back to School - TCP Challenge.

Connect to the server and solve the math problem to get the flag.
"""

import re
import socket

from rich.console import Console

NAME = "Back to School"
DESCRIPTION = "TCP challenge: calculate square root and multiply"

HOST = "challenge01.root-me.org"
PORT = 52002

console = Console()


def run() -> None:
    """Run the Back to School challenge."""
    console.print("[bold blue]Back to School Challenge[/bold blue]")
    console.print(f"Connecting to {HOST}:{PORT}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        response = s.recv(4096)
        response_text = response.decode("utf-8", errors="replace")
        console.print(f"[dim]Received:[/dim] {response_text}")

        result = _calculate(response_text)
        console.print(f"[dim]Sending result:[/dim] {result.strip()}")
        s.sendall(result.encode("utf-8"))

        response = s.recv(4096)
        console.print(f"[bold green]{response.decode('utf-8', errors='replace')}[/bold green]")


def _calculate(response_text: str) -> str:
    """Parse the challenge and calculate the answer."""
    match = re.search(r"square root of (\d+) and multiply by (\d+)", response_text)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = (num1**0.5) * num2
        return f"{result:.2f}\n"
    else:
        raise ValueError("Could not find the numbers in the response.")

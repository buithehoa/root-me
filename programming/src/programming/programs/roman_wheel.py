"""Roman Wheel - TCP Challenge."""

import codecs
import re
import socket

from rich.console import Console

NAME = "Roman Wheel"
DESCRIPTION = "Decode the ROT13-encoded string"

HOST = "challenge01.root-me.org"
PORT = 52021

console = Console()


def run() -> None:
    """Run the Roman Wheel challenge."""
    console.print("[bold blue]Roman Wheel Challenge[/bold blue]")
    console.print(f"Connecting to {HOST}:{PORT}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        response = s.recv(4096)
        response_text = response.decode("utf-8", errors="replace")
        console.print(f"[dim]Received:[/dim] {response_text}")

        encoded = _extract_encoded_string(response_text)
        decoded = codecs.decode(encoded, "rot_13")
        console.print(f"[dim]Sending result:[/dim] {decoded}")
        s.sendall(f"{decoded}\n".encode())

        final_response = s.recv(4096).decode("utf-8", errors="replace")
        console.print(f"[bold green]{final_response}[/bold green]")


def _extract_encoded_string(response_text: str) -> str:
    """Extract the encoded payload from the server prompt."""
    match = re.search(r"my string is '([^']+)'", response_text)
    if not match:
        raise ValueError("Could not find encoded string in server response.")
    return match.group(1)

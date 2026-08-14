#!/usr/bin/env python3
"""TCP Uncompress Me.

Connects to challenge01.root-me.org:52022, decodes base64 + zlib payloads,
and sends back the original message within the 2-second time limit.
"""

from __future__ import annotations

import base64
import re
import socket
import zlib
from re import Pattern

from rich.console import Console

NAME = "TCP Uncompress Me"
DESCRIPTION = "Decode zlib-compressed, base64-encoded strings over TCP"

HOST = "challenge01.root-me.org"
PORT = 52022
TIMEOUT = 2.0

B64_RE: Pattern[bytes] = re.compile(rb"([A-Za-z0-9+/=]{8,})")

console = Console()


def decode_payload(blob: bytes) -> str:
    """Decode base64, decompress zlib, return original string."""
    raw = base64.b64decode(blob)
    text = zlib.decompress(raw)
    return text.decode("utf-8", errors="replace")


def run() -> None:
    """Run the program."""
    console.print(f"[cyan]Connecting to {HOST}:{PORT}...[/cyan]")

    with socket.create_connection((HOST, PORT), timeout=TIMEOUT) as sock:
        sock.settimeout(TIMEOUT)
        buffer = b""

        while True:
            try:
                chunk = sock.recv(4096)
            except TimeoutError:
                continue

            if not chunk:
                break

            buffer += chunk

            text = chunk.decode("utf-8", errors="replace")
            # Split and print each prompt on its own line
            parts = text.split("my string is")
            for i, part in enumerate(parts):
                if i == 0:
                    console.print(part, end="")
                else:
                    console.print(f"\nmy string is{part}", end="")

            matches: list[bytes] = B64_RE.findall(buffer)
            if not matches:
                continue

            candidate = matches[-1]

            try:
                answer = decode_payload(candidate)
            except Exception:
                continue

            sock.sendall((answer + "\n").encode("utf-8"))
            buffer = b""


if __name__ == "__main__":
    run()

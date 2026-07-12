"""Shared utilities for tcp_backtoschool challenges."""

import socket

from rich.console import Console

console = Console()


def create_tcp_connection(host: str, port: int) -> socket.socket:
    """Create a TCP socket connection to the specified host and port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


def recv_all(sock: socket.socket, buffer_size: int = 4096) -> str:
    """Receive data from socket and decode as UTF-8."""
    response = sock.recv(buffer_size)
    return response.decode("utf-8", errors="replace")

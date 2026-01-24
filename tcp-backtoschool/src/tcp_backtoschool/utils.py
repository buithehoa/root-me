import re
import socket

from rich.console import Console

HOST = "challenge01.root-me.org"
PORT = 52002

console = Console()

def back_to_school():
    console.print("DEBUG Connecting to the server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        response = s.recv(4096)
        response_text = response.decode("utf-8", errors="replace")
        console.print(f"DEBUG Received: {response_text}")

        result = calculate(response_text)
        console.print(f"DEBUG Sending result: {result}")
        s.sendall(result.encode("utf-8"))

        response = s.recv(4096)
        console.print(response.decode("utf-8", errors="replace"))


def calculate(response_text):
    match = re.search(r"square root of (\d+) and multiply by (\d+)", response_text)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = (num1**0.5) * num2
        return f"{result:.2f}\n"
    else:
        raise ValueError("Could not find the numbers in the response.")

"""CAPTCHA Me If You Can - Break the CAPTCHA in less than 3 seconds.

Challenge URL: http://challenge01.root-me.org/programmation/ch8/
"""

import base64
import re

import ddddocr
import requests
from rich.console import Console

NAME = "CAPTCHA Me If You Can"
DESCRIPTION = "Break the CAPTCHA in less than 3 seconds"
URL = "http://challenge01.root-me.org/programmation/ch8/"
MAX_ATTEMPTS = 20

console = Console()


def extract_captcha_image(html: str) -> bytes | None:
    """Extract and decode the base64 CAPTCHA image from HTML."""
    match = re.search(r"data:image/png;base64,([A-Za-z0-9+/=]+)", html)
    if not match:
        return None
    return base64.b64decode(match.group(1))


def extract_flag(html: str) -> str | None:
    """Extract the flag from the success response."""
    match = re.search(r"flag est (\w+)", html)
    return match.group(1) if match else None


def solve_captcha(ocr: ddddocr.DdddOcr, session: requests.Session) -> str | None:
    """Attempt to solve a single CAPTCHA. Returns the flag on success."""
    response = session.get(URL, timeout=10)

    img_data = extract_captcha_image(response.text)
    if not img_data:
        console.print("[red]Could not find CAPTCHA image![/red]")
        return None

    text = ocr.classification(img_data)
    console.print(f"  OCR result: [cyan]{text}[/cyan]")

    response = session.post(URL, data={"cametu": text}, timeout=10)

    if "Rat" in response.text:  # "Raté" means failed in French
        return None

    console.print("\n[bold green]SUCCESS![/bold green]")
    return extract_flag(response.text) or response.text


def run() -> None:
    """Run the CAPTCHA solver."""
    console.print(f"[bold cyan]{NAME}[/bold cyan]")
    console.print(f"[dim]URL: {URL}[/dim]\n")

    console.print("[yellow]Initializing OCR engine...[/yellow]")
    ocr = ddddocr.DdddOcr(show_ad=False)

    for attempt in range(1, MAX_ATTEMPTS + 1):
        console.print(f"[dim]Attempt {attempt}/{MAX_ATTEMPTS}...[/dim]")

        session = requests.Session()
        result = solve_captcha(ocr, session)

        if result:
            console.print(f"[bold green]Flag: {result}[/bold green]")
            return

    console.print(f"\n[red]Failed after {MAX_ATTEMPTS} attempts.[/red]")
    console.print("[yellow]Try running again - OCR accuracy varies.[/yellow]")

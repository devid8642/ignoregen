from time import sleep
from typing import List, Optional

import typer
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

from ignoreme import api_client

app = typer.Typer(
    help='CLI for donotcommit.com – generate .gitignore files easily.'
)
console = Console()


@app.command()
def list():
    """
    List all available gitignore templates.
    """
    console.print('[bold green]Fetching templates from donotcommit.com...[/]')
    sleep(0.5)  # Simulate a delay for the user experience

    templates = api_client.list_templates()

    columns = Columns(templates, equal=True, expand=True)
    console.print(Panel(columns, title='Available Templates', expand=True))


@app.command()
def generate(
    templates: List[str],
    output: Optional[str] = typer.Option(
        None, help='Path to output .gitignore file'
    ),
):
    """
    Generate a .gitignore for the specified templates.
    """
    try:
        content = api_client.get_gitignore(templates)
    except ValueError as e:
        console.print(f'[bold red]Error:[/] {e}')
        raise typer.Exit(code=1)

    if output:
        with open(output, 'w', encoding='UTF-8') as f:
            f.write(content)
        console.print(f'[green]✅ .gitignore written to:[/] {output}')
    else:
        console.print(content)


if __name__ == '__main__':
    app()

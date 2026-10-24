import click

@click.group()
def cli():
    """Демонстраційна CLI-утиліта на базі Click."""
    pass

@cli.command()
@click.option('--name', required=True, help="Ім'я для перевірки (не має починатися на p/P).")
def say(name):
    """Виводить ім'я, якщо воно проходить перевірку."""
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)

if __name__ == '__main__':
    cli()
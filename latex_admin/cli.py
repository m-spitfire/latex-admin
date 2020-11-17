"""Console script for latex_admin."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for latex_admin."""
    click.echo("Replace this message by putting your code into "
               "latex_admin.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

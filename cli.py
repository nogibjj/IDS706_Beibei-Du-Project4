import click
import statistics
import pandas as pd
from mylib.runhealth import health_generator

df = pd.read_csv('fetal_health.csv')


@click.command()
#@click.option("--health", help="Health status to add")
def statushealth():
    """Pass in additional fruit"""

    chosen_random_ten = health_generator(df)
    click.echo(
        click.style(
            f"Your choice was randomly selected: {statistics.mode(set(chosen_random_ten))}", fg="red", bold=True
        ))


if __name__ == "__main__":
    #pylint: disable=no-value-for-parameter
    statushealth()

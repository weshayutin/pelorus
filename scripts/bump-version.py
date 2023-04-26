#!/usr/bin/env python3

import argparse
from pathlib import Path

from lib.charts import bump

parser = argparse.ArgumentParser(description="Bump versions in given helm charts")
parser.add_argument(
    "charts",
    metavar="chart",
    type=Path,
    nargs="+",
    help="The path to the Chart.yaml file, or the directory containing it",
)

for path in parser.parse_args().charts:
    bump(path)
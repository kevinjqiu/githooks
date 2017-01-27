"""
hooks - git hooks

Usage:
    hooks install
    hooks ls
    hooks update
"""

import sys
from docopt import docopt
from hooks import commands


__version__ = '0.1'


def cli():
    arguments = docopt(__doc__, version=__version__)
    sys.exit(commands.dispatch(arguments))

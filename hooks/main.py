"""
hooks - git hooks

Usage:
    hooks install
    hooks ls
"""

from docopt import docopt


__version__ = '0.1'


def cli():
    arguments = docopt(__doc__, version=__version__)
    print(arguments)
import shutil
import os


def dispatch(arguments):
    command = arguments['COMMAND']
    try:
        if command == 'install':
            return install(arguments)
        elif command == 'update':
            return update(arguments)
        elif command == 'ls':
            return ls(arguments)
        else:
            raise RuntimeError('No action specified')
    except RuntimeError as e:
        print(str(e))
        return 1


def _ensure_cwd_is_a_git_repo():
    """Is the current working directory a git repo?"""
    dot_git = os.path.join(os.getcwd(), '.git')
    if not (os.path.exists(dot_git) and os.path.isdir(dot_git)):
        raise RuntimeError('Must be in a git repository')


def install(args):
    """\
Install the hooks into the current git repository.

Usage:
    install [-f]

Options:
    -f  Overwrite without prompt when the hook already exists."""
    _ensure_cwd_is_a_git_repo()
    git_hook_directory = os.path.join(os.getcwd(), '.git', 'hooks')
    source = os.path.join(os.path.dirname(__file__), 'githooks', 'prepare-commit-msg')
    dest = os.path.join(git_hook_directory, 'prepare-commit-msg')
    shutil.copy(source, dest)
    print('prepare-commit-msg hook installed')


def update(args):
    pass


def ls(args):
    pass

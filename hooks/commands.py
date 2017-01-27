def dispatch(arguments):
    try:
        if arguments['install']:
            return install(arguments)
        elif arguments['update']:
            return update(arguments)
        elif arguments['ls']:
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

def dispatch(arguments):
    try:
        if arguments['install']:
            return install(arguments)
        elif arguments['update']:
            return update(arguments)
        elif arguments['ls']:
            return ls(arguments)
        else:
            return 1
    except:
        return 1


def install(args):
    pass


def update(args):
    pass


def ls(args):
    pass

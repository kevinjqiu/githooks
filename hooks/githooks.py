import functools
import subprocess


HOOKS = {
    'prepare-commit-msg': []
}


def get_active_hooks(hook_type):
    return HOOKS.get(hook_type, [])


def prepare_commit_msg_hook(fn):
    @functools.wraps(fn)
    def wrapper(temp_msg_file):
        return fn(temp_msg_file)

    HOOKS['prepare_commit_msg'] = wrapper
    return wrapper


@prepare_commit_msg_hook
def append_jira_ticket_id(temp_msg_file):
    branch_name = subprocess.check_output('git symbolic-ref --short HEAD')
    jira_ticket, _ = branch_name.split('-', 2)
    with open(temp_msg_file, 'rw') as fh:
        msg = fh.read()
        msg = '{}: {}'.format(jira_ticket, msg)
        fh.write(msg)

import click
import questionary
from goodgit.branch import list_branches, new_branch, switch_branch
from goodgit.commit import add, commit as ggcommit, push_to_remote, uncommit
from goodgit.merge import merge_branches
from goodgit.publish import publish
from goodgit.search import git_grep_interactive
from goodgit.ssh import add_ssh_account
from goodgit.timetravel import timetravel
from goodgit.web import gg_web

@click.group()
def cli():
    """GoodGit CLI"""
    pass

@cli.command()
def branch():
    list_branches()

    selection = questionary.select(
        "What do you wanna do next?",
        choices=['Create a new branch', 'Switch Branches', 'Nothing']
    ).ask()

    if selection == 'Create a new branch':
        new_branch()

    elif selection == 'Switch Branches':
        switch_branch()
    
    else:
        return

@cli.command()
def commit():
    add()
    ggcommit()
    push_to_remote()

@cli.command()
def uncommit():
    uncommit()

@cli.command()
def merge():
    merge_branches()


@cli.command()
def publish():
    publish()

@cli.command()
def search():
    git_grep_interactive()

@cli.command()
def setup():
    add_ssh_account()

@cli.command()
def web():
    gg_web()

@cli.command()
def timetravel():
    timetravel()
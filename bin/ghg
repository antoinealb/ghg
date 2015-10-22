#!/usr/bin/env python3
import subprocess
import sys
import platform
import argparse


def github_url_from_remote(u):
    if u.startswith('https://'):
        return u

    repo = u.split(':')[1]
    repo = repo[:-4]

    return 'https://github.com/{}'.format(repo)


def github_url_from_remote_output(output):
    origin = [s for s in output.splitlines() if 'origin' in s]
    pull_origin = [s for s in origin if 'push' in s][0]
    pull_url = pull_origin.split()[1]

    return github_url_from_remote(pull_url)


def get_remote():
    try:
        raw = subprocess.check_output('git remote -v'.split(),
                                      stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None

    return github_url_from_remote_output(raw.decode('ascii'))


def open_url(url):
    if 'Darwin' in platform.system():
        command = 'open {url}'.format(url=url).split()
    else:
        command = 'xdg-open {url}'.format(url=url).split()

    subprocess.call(command,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description="Opens a Github URL.")
    parser.add_argument("repository",
                        help="Repository to open (e.g. antoinealb/ghg).",
                        nargs='?',
                        action='store',
                        default=None)

    return parser.parse_args(args)


def main():
    args = parse_arguments()

    if args.repository:
        url = 'https://github.com/{}'.format(args.repository)
        open_url(url)
    else:
        remote = get_remote()
        if remote is None:
            print('No remote')
        else:
            open_url(remote)

if __name__ == '__main__':
    main()

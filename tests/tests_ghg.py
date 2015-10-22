from unittest import TestCase
from unittest.mock import patch, ANY

import ghg


class GithubUrlFromRemote(TestCase):
    def test_https_remote(self):
        url = 'https://github.com/cvra/master-firmware'
        result = ghg.github_url_from_remote(url)
        self.assertEqual(result, url)

    def test_git_remote(self):
        url = 'git@github.com:cvra/cvra.github.io.git'
        expected = 'https://github.com/cvra/cvra.github.io'

        result = ghg.github_url_from_remote(url)

        self.assertEqual(result, expected)

    def test_remote_output(self):
        command_output = """
origin	git@github.com:antoinealb/master-firmware.git (fetch)
origin	git@github.com:antoinealb/master-firmware.git (push)
cvra	git://github.com/cvra/master-firmware.git (fetch)
cvra	git://github.com/cvra/master-firmware.git (push)
nuft	git://github.com/nuft/master-firmware.git (fetch)
nuft	git://github.com/nuft/master-firmware.git (push)
"""

        expected = 'https://github.com/antoinealb/master-firmware'

        result = ghg.github_url_from_remote_output(command_output)
        self.assertEqual(result, expected)


@patch('platform.system')
@patch('subprocess.call')
class URlOpenTestCase(TestCase):
    def test_open_osx(self, call, system):
        system.return_value = 'Darwin'
        url = 'https://github.com/cvra/master'

        ghg.open_url(url)

        call.assert_any_call(['open', url], stdout=ANY, stderr=ANY)

    def test_open_linux(self, call, system):
        system.return_value = 'Linux'
        url = 'https://github.com/cvra/master'

        ghg.open_url(url)

        call.assert_any_call(['xdg-open', url], stdout=ANY, stderr=ANY)


class ArgumentParsingTestCase(TestCase):
    def test_parse_repo(self):
        args = ghg.parse_arguments(['cvra/master'])
        self.assertEqual('cvra/master', args.repository)

    def test_no_repository(self):
        args = ghg.parse_arguments([])
        self.assertIsNone(args.repository)

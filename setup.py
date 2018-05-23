from setuptools import setup
setup(
      name='ghg',
      version = '0.2.0',
      description = 'Simple script to quickly go on a Github page',
      author = 'antoinealb',
      url = 'http://github.com/antoinealb/ghg',
      py_modules = ['ghg.ghg'],
      scripts = ['bin/ghg', 'bin/github-get-stars'])

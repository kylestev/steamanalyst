from setuptools import setup, find_packages

def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name = 'steamanalyst',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = parse_requirements(),
    author = 'Kyle Stevenson',
    author_email = 'kyle@kylestevenson.me',
    description = 'This package can be used to parse CS:GO items from Steam Analyst\'s API.',
    keywords = 'csgo steamanalyst item prices steam market api',
    license = 'MIT',
    url = 'https://github.com/kylestev/steamanalyst'
)

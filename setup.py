from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='py-nand2tetris',
    version='0.0.1',
    description='nand2tetris implementation in python',
    long_description=readme,
    author='Ryo Nakabayashi',
    author_email='ryonakabayashi@gmail.com',
    url='https://github.com/ryought/py-nand2tetris',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'tools', 'refs')),
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)

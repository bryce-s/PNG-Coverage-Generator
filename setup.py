from setuptools import setup
setup(
    name = 'pngcoverage',
    version = '0.1.0',
    packages = ['pngcoverage'],
    entry_points = {
        'console_scripts': [
            'pngcoverage = pngcoverage.__main__:main'
        ]
    })
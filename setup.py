from setuptools import setup

setup(
    name='m2scorer',
    version='0.1.0',    
    description='M2scorer for Python3.',
    url='https://github.com/petrpechman/m2scorer',
    author='Petr Pechman',
    author_email='hugo.pechman@outlook.com',
    packages=['m2scorer'],
        entry_points="""
        [console_scripts]
        m2scorer=m2scorer.m2scorer:main
    """,
    install_requires=[]
)

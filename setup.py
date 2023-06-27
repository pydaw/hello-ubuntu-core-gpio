from setuptools import setup

setup(
    name='helloworldgpio',
    version='1.0.0',
    url='https://github.com/yourusername/myprogram',
    author='Daniel Wärnelöv',
    author_email='daniel.pean@gmail.com',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'helloworldgpio=src.helloworldgpio:main',
        ],
    },
)
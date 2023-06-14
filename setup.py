from setuptools import setup, find_packages

setup(
    name='sekiryu',
    version='0.0.2',
    description='Sekiryu: Enables users to perform a wide range of advanced reverse engineering tasks on binary files.',
    author='20urc3',
    author_email='20urc3@bushido-sec.com',
    url='https://github.com/20urc3/Sekiryu',
    packages=find_packages(),
    install_requires=[
        dataplane==0.0.20
        Jinja2==3.1.2
        numpy==1.24.2
        openai==0.26.5
        pandas==1.5.3
        setuptools==59.6.0
    ],
    entry_points={
        'console_scripts': [
            'sekiryu = sources.sekiryu:main'
        ]
    }
)

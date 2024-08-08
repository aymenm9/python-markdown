from setuptools import setup, find_packages

setup(
    name='pythonMarkdown',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # List any dependencies your package needs here
    ],
    author='Merad Aymen El Hadi',
    author_email='ay28mene@gmail.com',
    description='Recreation of python-markdown part of **CS50W Project:1** for learning purposes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
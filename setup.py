from setuptools import setup, find_packages

def file_content(path):
    try:
        with open(path) as f:
            return f.read()
    except IOError:
        return ''

setup(
    name='arthas',
    version='1.0',
    packages=find_packages(),
    license=file_content('LICENSE'),
    long_description=file_content('README'),
    author='linpelvis',
    author_email='linpelvis@gmail.com',
    maintainer='linpelvis',
    url=''
)

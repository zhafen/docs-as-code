from setuptools import setup, find_packages

setup(
    name='my-python-package',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package for documentation as code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-python-package',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
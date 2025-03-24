from setuptools import setup, find_packages

setup(
    name="docs-as-code",
    version="0.1.0",
    author="Zach Hafen-Saavedra",
    author_email="z.hafen.saavedra@gmail.com",
    description="A Python package for documentation as code.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zhafen/docs-as-code",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)

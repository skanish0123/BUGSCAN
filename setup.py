from setuptools import setup, find_packages

setup(
    name="BUGSCAN",
    version="2.0",
    author="ANISH",
    author_email="anish@bugscan.com",
    description="Advanced Security Toolkit - Host Scanner, Port Scanner, IP Lookup & More",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/skanish0123/BUGSCAN",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: Android",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "bugscan=bugscan.main:main",
        ],
    },
)
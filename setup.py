# coding=utf-8

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

with open("README.rst") as fd:
    long_description = fd.read()


def read_version():
    p = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                     "freehp",
                     "version.py")
    with open(p, "rb") as f:
        return f.read().decode("utf-8").split("=")[-1].strip().strip('"')


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)


def main():
    if sys.version_info < (3, 5):
        raise RuntimeError("Python 3.5+ is required")
    install_requires = [
        "aiohttp",
        "pyyaml"
    ]
    tests_requires = install_requires + ["pytest", "pytest-aiohttp"]
    setup(
        name="freehp",
        version=read_version(),
        url="https://github.com/jadbin/freehp",
        description="Free HTTP proxy",
        long_description=long_description,
        author="jadbin",
        author_email="jadbin.com@hotmail.com",
        license="Apache 2",
        zip_safe=False,
        packages=find_packages(exclude=("tests",)),
        include_package_data=True,
        entry_points={
            "console_scripts": ["freehp = freehp.cli:main"]
        },
        install_requires=install_requires,
        tests_require=tests_requires,
        cmdclass={"test": PyTest},
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Topic :: Internet :: WWW/HTTP"
        ],
    )


if __name__ == "__main__":
    main()

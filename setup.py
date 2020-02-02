import setuptools
import os

pkg_vars = {}
pkg_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pkg_dir, "falconbot", "_version.py"), "r") as fh:
    exec(fh.read(), pkg_vars)

with open(os.path.join(pkg_dir, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="falconbot",
    version=pkg_vars['__version__'],
    author="FrozenFOXX",
    author_email="frozenfoxx@churchoffoxx.net",
    description="An automated bot that watches social media accounts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frozenfoxx/falconbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License v2",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    scripts=[
        "scripts/falconbot",
    ],
    entry_points = {
        "console_scripts": ["falconbot=falconbot.falconbot:main"],
    },
    data_files=[
        ('/etc/falconbot', ['conf/falconbot.conf'])
    ],
    include_package_data=True,
)


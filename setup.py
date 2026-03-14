"""
Hikari - Modified version with OnyxCord support
This is a modified version of Hikari that preserves unknown component types
"""
from setuptools import setup, find_packages

setup(
    name="hikari-onyxcord",
    version="2.5.0.onyx1",
    description="Hikari modified to support OnyxCord modal components",
    author="Hikari Development Team (Modified for OnyxCord)",
    python_requires=">=3.10",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0,<4",
        "attrs>=22.1.0",
        "colorlog>=6.7.0,<7",
        "multidict>=6.0.0,<7",
    ],
    extras_require={
        "speedups": [
            "aiodns>=3.0.0,<4",
            "cchardet>=2.1.7,<3; python_version<'3.10'",
            "ciso8601>=2.2.0,<3",
            "orjson>=3.8.0,<4",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

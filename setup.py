from setuptools import setup

setup(
    name="shuffled",
    packages=["shuffled"],
    package_dir={"": "src"},
    version="0.2",
    description="Iterate randomly over large integer ranges",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Bertrand Bonnefoy-Claudet",
    author_email="bertrand@bertrandbc.com",
    url="https://github.com/bbc2/shuffled",
    download_url="https://github.com/bbc2/shuffled/tarball/v0.2",
    keywords=["random", "integer", "iterator"],
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=[
        "cryptography",
    ],
    extras_require={
        "tests": [
            "pytest",
            "pytest-cov",
            "unittest2",
        ],
        "dev": [
            "black",
            "mypy",
            "flake8",
        ],
    },
    package_data={
        "shuffled": ["py.typed"],
    },
)

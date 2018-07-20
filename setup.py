import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commercetools",
    version="0.0.1",
    author="Federico Moro",
    author_email="fede@devgurus.io",
    description="Commercetools SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevgurusSupport/commercetools-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymultimediacompression",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="Abdullrhman Aljasser",
    author_email="abdullrhmanaljasser@gmail.com",                     # Full name of the author
    description="Package provide easy to use functions to compress different types of media",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["pymultimediacompression"],             # Name of the python package
    install_requires=[
        'ffmpeg',
        'ffmpeg-python'
    ]                     # Install other dependencies if any
)
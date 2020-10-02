import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proposal-forecast", 
    version="1.0.0",
    author="Yves Deutschmann",
    author_email="yves.deutschmann@gmail.com",
    description="small website to propose to my girlfriend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YvesDeutschmann/proposal-website",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
)
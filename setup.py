import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="angryuser",
    version="0.0.1",
    author="Gideon Tong",
    author_email="gideon@gideontong.com",
    description="Tweets if the internet is offline or slower than what you're paying for",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gideontong/AngryInternetUser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
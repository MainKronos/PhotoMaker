import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="photomaker",
    version="1.0.1",
    author="MainKronos",
    description="A library to create funny pictures with your friends' photos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MainKronos/PhotoMaker",
    packages=setuptools.find_packages(),
    install_requires=['Pillow'],
	license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
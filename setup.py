from setuptools import setup, find_packages

setup(
    name="MsgPackConnection",
    version="1.0.0",
    description="Simple library for exchanging python objects via TCP",
    url="https://github.com/LevitatingOrange/MsgPackConnection",
    license="MIT",
    py_modules=["MsgPackConnection"],
    install_requires=["msgpack-python"],
    python_requires=">=3"
)

# MsgPackConnection

A very simple library to exchange python objects via TCP.
It uses msgpack to serialize and deserialize the data and the
low-level python socket api to make a TCP connection.

## Usage
### Server
```python
with create_connection(server_ip, server_port, True) as c:
    c.write({"foo":"bar"})
    c.read()
    # => {"baz":"bar"}
```
### Client
```python
with create_connection(server_ip, server_port, False) as c:
    c.write({"baz":"bar"})
    c.read()
    # => {"foo":"bar"}
```
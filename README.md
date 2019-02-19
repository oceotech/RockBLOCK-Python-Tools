# RockBLOCK Python Tools

[![Build Status](https://travis-ci.org/oceotech/RockBLOCK-Python-Tools.svg?branch=master)](https://travis-ci.org/oceotech/RockBLOCK-Python-Tools)

A python library and command line application for interfacing with the RockBLOCK web services.

## Install

```sh
pip install rockblock-tools
```

## Usage

### Sending a Message

Simple:
```sh
rockblock send [imei] [user] [pass] "Hello, World"
```

```sh
rockblock send [imei] [user] [pass] "Hello, World" --data-format=raw
```

With hexadecimal encoding:
```sh
rockblock send [imei] [user] [pass] 48656c6c6f2c20576f726c6421 --data-format=hex
```

With base64 encoding:
```sh
rockblock send [imei] [user] [pass] SGVsbG8sIFdvcmxkIQ== --data-format=base64
```

### Listening for Messages

The following command sets up a service listening for web hooks on port 80. It will print incoming messages to the console:
```sh
rockblock listen console 0.0.0.0 80
```

To write the incoming messages to a CSV file:
```sh
rockblock listen csv 0.0.0.0 80 path/to/file.csv
```

To publish the incoming messages to an MQTT server (localhost:1883):
```sh
rockblock listen mqtt 0.0.0.0 80 localhost 1883 my/mqtt/topic --mqtt-user=user --mqtt-pass=pass --mqtt-qos=0
```

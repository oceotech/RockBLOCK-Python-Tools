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

To listen to messages from the RockBLOCK web service, you need to make sure that your listener is visible from the public internet. If you are setting up the listener on a home network, this will likely require [port forwarding](https://portforward.com/).

In the command examples below, the listener is running on the normal HTTP port (`80`) and accepting external inbound connections (binding to `0.0.0.0`).

To connect your listener, add the web address of your listener (e.g. `http://your-ip-here/`) to a delivery group on the RockBLOCK admin portal. You can use the "Test Delivery Groups" page to test your listener without using credits.

#### Console Output

Command:
```sh
rockblock listen console 0.0.0.0 80
```

Example Output:
```
---------- MESSAGE ----------
Iridium Latitude  33.2938
Iridium Longitude 125.2902
Device Type       ROCKBLOCK
Transmit Time     2020-02-19 00:22:50
MOMSN             663
IMEI              300434063480220
Serial            16302
Data              Hello! This is a test message from RockBLOCK!
Iridium CEP       15.0
-----------------------------
```

#### CSV Output

Command:
```sh
rockblock listen csv 0.0.0.0 80 path/to/file.csv
```

Example Output:
```csv
Iridium Latitude,Iridium Longitude,Device Type,Transmit Time,MOMSN,IMEI,Serial,Data,Iridium CEP
75.5254,62.6541,ROCKBLOCK,2020-02-19 00:23:47,680,300434063480220,16302,There are 10 types of people who understand binary,9.0
46.4861,159.9892,ROCKBLOCK,2020-02-19 00:23:47,326,300434063480220,16302,Abcdefghijklmnopqrstuvwxyz1234567890,110.0
```

#### MQTT Output

Command (for an MQTT server running at localhost:1883):
```sh
rockblock listen mqtt 0.0.0.0 80 localhost 1883 my/mqtt/topic --mqtt-user=user --mqtt-pass=pass --mqtt-qos=0
```

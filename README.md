# HowLong

[![Build Status](https://travis-ci.org/mattjegan/HowLong.svg?branch=master)](https://travis-ci.org/mattjegan/HowLong)
[![Code Health](https://landscape.io/github/mattjegan/HowLong/master/landscape.svg?style=flat)](https://landscape.io/github/mattjegan/HowLong/master)
[![PyPI version](https://badge.fury.io/py/howlong.svg)](https://badge.fury.io/py/howlong)

A simple command line application that lets you know how long your command has been running.

## Installation

### From PyPi

```
pip install howlong
```

### From source

```
git clone https://github.com/mattjegan/howlong.git
cd HowLong
python setup.py install
```

## Usage

Time a command
```
$ howlong python helloworld.py
Running python helloworld.py
0:00:01.003903
Hello, World!
0:00:02.005022
Finished python helloworld.py
```

Change the interval at which `howlong` times
```
howlong -i 0.5 <command>
```

Display help
```
howlong -h
usage: howlong [-h] [-i [interval]] C [C ...]

Time a process

positional arguments:
  C              a valid command

optional arguments:
  -h, --help     show this help message and exit
  -i [interval]  the timer interval, defaults to 1 second
```

## Contributing

### Submitting an issue or feature request

If you find an issue or have a feature request please open an issue at [Github HowLong Repo](https://github.com/mattjegan/howlong).

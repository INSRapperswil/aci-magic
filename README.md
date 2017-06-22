# ACI magic
Collection of some helpful Cisco ACI Python scripts.

## Prerequisites
All script require [acitoolkit](https://github.com/datacenter/acitoolkit). 
Please refer to their documentation in order to install it.

You can also use PIP to install acitoolkit:
```bash
pip2.7 search acitoolkit
```

## Usage
First you have to rename the file `credentials_template.py` to `credentials.py` and edit the credentials inside this file.

Now you should be able to run the scripts with `./<script-name>.py`.

## Debug
If you run into an error like `'Connection aborted.', error(54, 'Connection reset by peer')`, install `requests[security]`:
```bash
pip install requests[security]
```
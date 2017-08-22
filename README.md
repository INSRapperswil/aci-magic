# ACI magic
Collection of some helpful Cisco ACI Python scripts.

## Prerequisites
All scripts require [acitoolkit](https://github.com/datacenter/acitoolkit). 
Please refer to their documentation in order to install it.

You can also use PIP to install acitoolkit:
```bash
pip install acitoolkit
```

## Usage
First you have to rename the file `credentials_template.py` to `credentials.py` and edit the credentials inside this file.
Now you should be able to run the scripts with `./<script-name>.py`.


## Development
**Hint:** Use `arya` [datacenter/arya](https://github.com/datacenter/arya) in order to generate Python code (Cobra) from a JSON POST example captured with the Cisco ACI API Inspector.
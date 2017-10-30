# ACI magic
Collection of some helpful Cisco ACI Python scripts.

## Prerequisites
All scripts require [acitoolkit](https://github.com/datacenter/acitoolkit) **or** the ACI Cobra SDK. 

You can use PIP to install acitoolkit:
```bash
pip install acitoolkit
```

Download the Cobra SDK from [https://APIC_ADDRESS/cobra/_downloads/](https://APIC_ADDRESS/cobra/_downloads/) and install the two `.egg` files using the following commands:
```bash
easy_install acimodel-<version>-py2.7.egg
easy_install acicobra-<version>-py2.7.egg
```

## Usage
First you have to rename the file `credentials_template.py` to `credentials.py` and edit the credentials inside this file.
Now you should be able to run the scripts with `./<script-name>.py`.


## Development
**Hint:** Use `arya` [datacenter/arya](https://github.com/datacenter/arya) in order to generate Python code (Cobra) from a JSON POST example captured with the Cisco ACI API Inspector.
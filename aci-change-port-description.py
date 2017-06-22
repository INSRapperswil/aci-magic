#!/usr/bin/env python

#######################################################################
#
# This script sets the port descriptions to the hostname,
# which is connected to the corresponding port. It uses LLDP
# to detect the hostname of the adjacent neighbor.
#
# To verify the script changes, login to your leaf switches:
# 1. ssh <ip-of-your-controller> -l <username>
# 2. attach <leaf-X-name>
# 3. show interface status
#
#######################################################################

from acitoolkit.acitoolkit import *
import credentials

session = Session(credentials.URL, credentials.LOGIN, credentials.PASSWORD)
resp = session.login()
if not resp.ok:
    print 'Login to ACI was not successful'

tenants = Tenant.get(session)





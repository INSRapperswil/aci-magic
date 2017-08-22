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

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest

from cobra.model.fv import Tenant
import cobra.model.lldp

import credentials as cred

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_tenant(tenant, tenant_list):
    for tenant_entry in tenant_list:
        if tenant_entry.name == tenant:
            return tenant_entry

# configReq = ConfigRequest()
session = LoginSession(cred.URL, cred.LOGIN, cred.PASSWORD)
moDir = MoDirectory(session)

moDir.login()

uniMo = moDir.lookupByDn('uni')
# uniMo = moDir.lookupByClass('polUni')

# fvTenantMo = Tenant(uniMo, 'TestTenant')
testTenantMo = moDir.lookupByClass("fvTenant", propFilter='and(eq(fvTenant.name, "TestTenant"))')
lldpAdjEps = moDir.lookupByClass('lldpAdjEp')
if lldpAdjEps:
    print "Found adjacent hosts via LLDP:"
for adjEp in lldpAdjEps:
    print str(adjEp.dn) + " is connected to " + str(adjEp.sysName)

# configReq.addMo(tenant1Mo)

# moDir.commit(configReq)
moDir.logout()

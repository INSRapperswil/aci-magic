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

from cobra.model.infra import Infra, HPathS, RsHPathAtt, SHPathS, RsSHPathAtt

import credentials as cred
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Concatenates tDN of RsHPathAtt
def concat_path_ep(dn):
    pod = re.search('pod-(\d+)', dn)
    node = re.search('node-(\d+)', dn)
    port = re.search('\[(eth\d+/\d+)\]', dn)
    if port and node:
        return 'topology/pod-' + pod.group(1) + '/paths-' + node.group(1) + '/pathep-[' + port.group(1) + ']'
    return None


# Checks if its a leaf switch
def is_leaf(dn):
    node = re.search('node-(\d+)', dn)
    return int(node.group(1)) < 199


# Returns the node name
def get_node_name(dn):
    node = re.search('node-(\d+)', dn)
    return node.group(1)


session = LoginSession(cred.URL, cred.LOGIN, cred.PASSWORD)
moDir = MoDirectory(session)
moDir.login()
uniMo = moDir.lookupByDn('uni')

lldpAdjEps = moDir.lookupByClass('lldpAdjEp')
if lldpAdjEps:
    print "Found adjacent hosts via LLDP:"
for adjEp in lldpAdjEps:
    print str(adjEp.dn) + " is connected to " + str(adjEp.sysName)

infraInfra = Infra(uniMo)

for adjEp in lldpAdjEps:
    if is_leaf(str(adjEp.dn)):
        infraHPathS = HPathS(infraInfra, name="adjEp-{0}-{1}".format(str(adjEp.sysName), get_node_name(str(adjEp.dn))),
                             descr=str(adjEp.sysName))
        infraRsHPathAtt = RsHPathAtt(infraHPathS, tDn=concat_path_ep(str(adjEp.dn)))
    else:
        infraSHPathS = SHPathS(infraInfra, name="adjEp-{0}-{1}".format(str(adjEp.sysName), get_node_name(str(adjEp.dn))),
                               descr=str(adjEp.sysName))
        infraRsSHPathAtt = RsSHPathAtt(infraSHPathS, tDn=concat_path_ep(str(adjEp.dn)))

configReq = ConfigRequest()
configReq.addMo(infraInfra)
moDir.commit(configReq)

moDir.logout()

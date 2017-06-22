#!/usr/bin/env python

#######################################################################
#
# This script creates some basic filter sets which are usually
# multiple times used and application specific.
#
#######################################################################

from acitoolkit.acitoolkit import Tenant, Session, Filter, FilterEntry
import credentials
import csv


def get_tenant(tenant, tenant_list):
    for tenant_entry in tenant_list:
        if tenant_entry.name == tenant:
            return tenant_entry




session = Session(credentials.URL, credentials.LOGIN, credentials.PASSWORD)
resp = session.login()
if not resp.ok:
    print 'Login to ACI was not successful'

common_tenant = get_tenant('common', Tenant.get(session))

filterX = Filter('VoIP_Telephony', common_tenant)

FilterEntry('SIP',
             applyToFrag='no',
             dFromPort='5060',
             dToPort='5061',
             etherT='ip',
             prot='tcp',
             parent=filterX)

if common_tenant:
    resp = common_tenant.push_to_apic(session)
    if resp.ok:
        print 'Successfully committed changes'
    else:
        print 'Failed to commit changes'
        print resp.text

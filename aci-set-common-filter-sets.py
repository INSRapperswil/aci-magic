#!/usr/bin/env python

#######################################################################
#
# This script creates some basic filter sets which are usually
# multiple times used and application specific.
#
#######################################################################

from acitoolkit.acitoolkit import Tenant, Session, Filter, FilterEntry
import pandas as pd
import credentials as cred


def get_tenant(tenant, tenant_list):
    for tenant_entry in tenant_list:
        if tenant_entry.name == tenant:
            return tenant_entry


session = Session(cred.URL, cred.LOGIN, cred.PASSWORD)
resp = session.login()
if not resp.ok:
    print 'Login to ACI was not successful'

common_tenant = get_tenant('common', Tenant.get(session))

data = pd.read_csv('filter_entries.csv')
filterObj = dict()
for f in data.filterName.unique():
    filterObj[f] = Filter(f, common_tenant)

for index, row in data.iterrows():
    FilterEntry(str(row['filterEntryName']),
                applyToFrag=str(row['applyToFrag']),
                arpOpc=str(row['arpOpc']),
                stateful=str(row['stateful']),
                etherT=str(row['etherT']),
                prot=str(row['prot']),
                sFromPort=str(row['sFromPort']),
                sToPort=str(row['sToPort']),
                dFromPort=str(row['dFromPort']),
                dToPort=str(row['dToPort']),
                parent=filterObj[str(row['filterName'])])

if common_tenant:
    resp = common_tenant.push_to_apic(session)
    if resp.ok:
        print 'Successfully committed changes'
    else:
        print 'Failed to commit changes'
        print resp.text

import censys.data
import sys
import json
import requests

# API_URL = "https://www.censys.io/api/v1"
UID = "610a08f3-78a4-4b5b-82dd-b196aeeb19e4"
SECRET = "1eC4vP5hir8MP7UN9vbUdIHRpJo5bp8X"

c = censys.data.CensysDat(api_id=UID, api_secret=SECRET)

# Get a Series
ssh_series = c.view_series('22-ssh-banner-full_ipv4')

# View all the files in each scan
for scan in ssh_series['results']['historical']:
    print c.view_result('22-ssh-banner-full_ipv4', scan['id'])

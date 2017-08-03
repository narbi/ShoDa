#!/usr/bin/python
# pip install shodan
import shodan

SHODAN_API_KEY = "T9NuuJ24Fhj4UC8hZ94w8EtSv4f7XkWg"
api = shodan.Shodan(SHODAN_API_KEY)

# Top SCADA Protocols
# protocols = ['ICS', 'SCADA', 'MODBUS', 'DNP3', 'IEC 61850', 'SCADA FTP'];
protocols = ['ICS', 'SCADA', 'MODBUS', 'MODBUS TCP/IP'];

# Create facets
FACETS = [
    'port',
    'os',
    'device',
    'version',
    ('country', 10),
]

FACET_TITLES = {
    'port': 'Top 5 Ports',
    'os': 'Top 5 Operating Systems',
    'device': 'Top 5 Devices',
    'version': 'Top 5 Product Versions',
    'country': 'Top 10 Countries'
}

for protocol in protocols:
  try:
    # Search Shodan
    query = protocol
    results = api.count(query, facets=FACETS)
    # Show the results
    print ('Total Results for %s: %s \n' % (protocol, results['total']))
    for facet in results['facets']:
        print ('\n')
        print (FACET_TITLES[facet])
        for term in results['facets'][facet]:
            print ('%s: %s' % (term['value'], term['count']))
    print ('-------------------------------------')
  except shodan.APIError:
    print ('Error: %s' % e)

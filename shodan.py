#!/usr/bin/python
# pip install shodan
import shodan

SHODAN_API_KEY = "T9NuuJ24Fhj4UC8hZ94w8EtSv4f7XkWg"
api = shodan.Shodan(SHODAN_API_KEY)

# Top SCADA Protocols
protocols = ['MODBUS', 'DNP3', 'ISC 61850', 'FTP'];

# Create facets
FACETS = [
    'org',
    'domain',
    'port',
    'asn',
    ('country', 20),
]

FACET_TITLES = {
    'org': 'Top 10 Organizations',
    'domain': 'Top 10 Domains',
    'port': 'Top 10 Ports',
    'asn': 'Top 10 Autonomous Systems',
    'country': 'Top 20 Countries',
}


for protocol in protocols:
  try:
    # Search Shodan
    query= protocol
    results = api.count(query, facets=FACETS)
    # Show the results
    print ('Total Results for %s: %s \n' % (protocol, results['total']))
    for result in results['matches']:
      print (FACET_TITLES[facet])
    for term in result['facets'][facet]:
      print ('%s: %s' % (term['value'], term['count']))
    print ('-------------------------------------')
  except shodan.APIError:
    print ('Error: %s' % e)

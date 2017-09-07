#!/usr/bin/python
# pip install shodan
import shodan
import sys
SHODAN_API_KEY = "T9NuuJ24Fhj4UC8hZ94w8EtSv4f7XkWg"
api = shodan.Shodan(SHODAN_API_KEY)

try:
        query = 'port=502'
        result = api.search(query)

        # Loop through the matches and print each IP
        for service in result['matches']:
                print (service['ip_str'])
except Exception as e:
        print ('Error: %s' % e)
        sys.exit(1)
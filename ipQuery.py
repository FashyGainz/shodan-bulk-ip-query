import json
import shodan
import argparse
import time
SHODAN_API_KEY = "<YOUR API KEY HERE>"
api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Get a list of IPs and return shodan info.')
parser.add_argument('--filename', '-f', default='iplist.txt')
args=parser.parse_args()

with open(args.filename, 'r') as f:
        ips = [line.strip() for line in f]


awsInfo = {}
for ip in ips:
        try:
                print "Retrieving Info"
                hostinfo = api.host(ip)
                awsInfo[ip] = hostinfo
                time.sleep(2)
                print "Info collected"
        except shodan.APIError, e:
                awsInfo[ip] = '{}'.format(e)
                time.sleep(2)
                print "No information found"

print json.dumps(awsInfo)

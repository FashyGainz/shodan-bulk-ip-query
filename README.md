# Shodan Bulk IP Query
This tool gets a list of IPs in a file (one IP per line) and queries shodan.io. It prints the query results in JSON format to stdout. 

# Usage
`# python ipQuery.py` will take as default filename: `iplist.txt` as filename to read the IPs from. You can always use `-f` or `--filename` as an argument to provide your filename. 

`# python -f myawesomepath/myawesomefilename.foo`

# TODO
- Throttling for big queries.

Fixed 03/20/19 by adding time.sleep() function with 2 seconds in the try and else. 
Also added some extra text to tell you when each lookup is completed.

- Combine IPs to make one bulk query.

Fake and gay. I really dont care about this

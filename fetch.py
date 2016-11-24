import urllib2,csv,cookielib

#site = "http://xueqiu.com/S/AAPL/historical.csv"
# http://www.nasdaq.com/screening/company-list.aspx
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#req = urllib2.Request(site, headers=hdr)
symbolTest = 'APPL'
Exchange = 'NASDAQ'
# Exchange = 'NYSE'
# Exchange = "AMEX"

try:
    with open(Exchange +'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Symbol'], row['Name'])
            symbol = row['Symbol'].strip()

            if '^' not in symbol:
                site = "http://xueqiu.com/S/" + symbol + "/historical.csv"
                req = urllib2.Request(site, headers=hdr)
                page = urllib2.urlopen(req)
                #content = page.read()
                with open(Exchange + '/'+symbol+'.csv','w') as symbolCSV:
                    symbolCSV.write(page.read())
            else:
            	print 'symbol contains ^, not valid, passed...'

except urllib2.HTTPError, e:
    print e.fp.read()

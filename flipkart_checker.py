import urllib2
import re
import subprocess
# URL to the product
flipkart_url = '<ENTER THE URL HERE>'
flipkart_fetch = urllib2.urlopen(flipkart_url).read()

product = re.findall('This item is currently out of stock', flipkart_fetch);

if len(product) == 0: 
	message = "The Product is back in stock at Flipkart "
else:
	message = "Product is not available yet'
subprocess.Popen(['notify-send', message])

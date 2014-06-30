import urllib2
import re
import subprocess
# URL to the product
flipkart_url = 'URL to product'
flipkart_fetch = urllib2.urlopen(flipkart_url).read()
# the magic line (don't edit this)
product = re.findall('Notify me when this product is in stock', flipkart_fetch);
# message to print 
if len(product) == 0: 
   message = "your product is back in stock at Flipkart "
   subprocess.Popen(['notify-send', message])
else:
# this line only prints in terminal
   print 'Your product is not available '

import urllib2
import re
import subprocess
flipkart_url = 'http://www.flipkart.com/moto-g/p/itmdsmbxcrm9wy8r'
flipkart_fetch = urllib2.urlopen(flipkart_url).read()

product = re.findall('Notify me when this product is in stock', flipkart_fetch);

if len(product) == 0: 
   message = "Moto E back in stock at Flipkart "
   subprocess.Popen(['notify-send', message])
else:
   print 'Your product is not avialble :('

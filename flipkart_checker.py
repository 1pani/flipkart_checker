import urllib.request as u
import re
import subprocess
# URL to the product
flipkart_url = '<ADD HOSTNAME TO PRODUCT'
flipkart_fetch = u.urlopen('http://' + flipkart_url).read().decode('utf-8')

product = re.findall('This item is currently out of stock', flipkart_fetch)

if len(product) == 0: 
	message = "The Product is back in stock at Flipkart "
else:
	message = "Product is not available yet"
subprocess.Popen(['notify-send', message])

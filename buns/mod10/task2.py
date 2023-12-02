import requests
import re

site_request1 = requests.get('https://habr.com/ru/companies/singularis/articles/516798/')
site_request2 = requests.get('http://www.columbia.edu/~fdc/sample.html')

match1 = re.findall(r"<h3.*?>(.*)</h3.*?>", site_request1.text)
match2 = re.findall(r"<h3.*?>(.*)</h3.*?>", site_request2.text)


print(match1)
print(match2)
import requests
import math

URL = ''
res = requests.get(URL)

total_items = res.json()['meta']['total'] #total 

items_per_page = 10
iterations = math.ceil(total_items / items_per_page)
results = []

for offset in range(iterations):
  params = {'offset': offset * items_per_page}
  output = requests.get(URL, params=params)
  results += output.json()['result']
 
print(results)

from scrapy.selector import Selector
import requests
url = 'https://mintyscore.com/top-drops/influencers?sort=minty_score&order=desc&name='
response = requests.get(url)
body = response.text
selector=Selector(text=body).xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/text()')
print(selector.getall())
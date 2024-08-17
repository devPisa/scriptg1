import requests
from lxml import html

response = requests.get('https://g1.globo.com/')

if (response.status_code == 200):
    corpoTexto = response.text
    siteXml = html.fromstring(corpoTexto)
    manchetes = siteXml.xpath('//div/div[2]/div/h2/a')
    print(manchetes[0].text_content())

else:
    print('Dados não encontrato')
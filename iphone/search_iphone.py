import requests
from bs4 import BeautifulSoup

class SearchIphone:
    def __init__(self):
        self.headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            'accept-encoding': 'gzip, deflate, br',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'upgrade-insecure-requests': '1',
            'referer': 'https://www.google.com/'
        }

        self.url = 'https://www.amazon.com.br/s?k=iPhone&page={0}&qid=1611118341&ref=sr_pg_{0}'
    
    def get(self, page=1):
        try:
            html = requests.get(self.url.format(page), headers=self.headers)
        except requests.exceptions.RequestException:
            return None
    
        bs = BeautifulSoup(html.content, 'html.parser')
        iphones = bs.findAll('div', attrs={'class':'a-section a-spacing-medium'})

        iphone_data = []
        for d in iphones:
            name = d.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
            price = d.find('span', attrs={'class':'a-offscreen'})

            data = []

            if name is not None:
                data.append(name.get_text())
            else:
                data.append('produdo desconhecido')
            
            if price is not None:
                data.append(price.get_text())
            else:
                data.append('---')
            
            iphone_data.append(data)
        
        return iphone_data
# -*- coding: utf-8 -*-
"""
@author: Lumix888
"""

import requests
from bs4 import BeautifulSoup
import json
   
start_url = 'https://www.osta.ee/en/category/computers/desktop-computers'

#print(page)


def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print (soup)


    items_list = soup.find_all("li", class_ = "col-md-4 mb-30")
    #print(items_list)
   
    for item in items_list:
        data = {'Title':'', 'Price':'', 'Picture href':''}
        
        data['Title'] = item.h3['title']
        data['Price'] = item.find('div', class_='offer-thumb__price--current').contents[0].strip()
        data['Picture href'] = item.img['data-original']  
        
        print(data)

        with open('items_list.json', 'a') as json_file:
            json.dump(data, json_file)                
      
    try:    
        next_page = soup.find("a", class_='icon next page-link')['href']
        if next_page:
            #print(next_page)
            next_page = "https://www.osta.ee/en/" + next_page
            print(next_page)
            parse(next_page)
    except:
        print("No more pages")   
        

if __name__ == '__main__':
    parse(start_url)

    
    
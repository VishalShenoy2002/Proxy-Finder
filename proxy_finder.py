import requests
from bs4 import BeautifulSoup
import sys

class ProxyList:
    def __init__(self):
        print('''
        ______                     ______ _           _           
        | ___ \                    |  ___(_)         | |          
        | |_/ / __ _____  ___   _  | |_   _ _ __   __| | ___ _ __ 
        |  __/ '__/ _ \ \/ / | | | |  _| | | '_ \ / _` |/ _ \ '__|
        | |  | | | (_) >  <| |_| | | |   | | | | | (_| |  __/ |   
        \_|  |_|  \___/_/\_\\__, | \_|   |_|_| |_|\__,_|\___|_|   
                            __/ |                                
                            |___/                                 
        ''')

        print('Start Finding Proxies Press Ctrl-C to Quit...')
        self.proxy_site="https://free-proxy-list.net/"
        self.request=requests.get(self.proxy_site,allow_redirects=True).text
        self.soup=BeautifulSoup(self.request,'html.parser')
        self.proxy_list=[]
        self.proxy=[]

        for element in range(8):
            for proxy_item in self.soup.find_all('td'):

                if len(self.proxy)==8:
                    self.proxy_list.append(self.proxy)
                    self.proxy=[]
                   
                self.proxy.append(proxy_item.get_text())

    def find_elite_proxy(self):

        elite_proxies=[]

        for proxy in self.proxy_list:
            if 'elite' in proxy[4]:
                elite_proxies.append(proxy)

        return elite_proxies

    def find_anonymous_proxy(self):

        anonymous_proxies=[]

        for proxy in self.proxy_list:
            if 'anonymous' in proxy[4]:
                anonymous_proxies.append(proxy)
        
        return anonymous_proxies

    def find_proxy_by_country(self,country):
        proxy_by_country=[]

        for proxy in self.proxy_list:
            if country.lower() in proxy[3].lower():
                proxy_by_country.append(proxy)

        if len(proxy_by_country)==0:
            return "No Proxy Found"

        return proxy_by_country  
  

def print_proxy(proxy_list):
    for proxy in proxy_list:
        print('---'*20)
        print('IP Address: {}\nPort: {}\nCountry: {}\nAnonymity: {}\nGoogle: {}\nHttps: {}'.format(proxy[0],proxy[1],proxy[3],proxy[4].title(),proxy[5].title(),proxy[6].title()))
        print('Full Address: {}:{}'.format(proxy[0],proxy[1]))
        print('---'*20)
    
if __name__=="__main__":
    proxy=ProxyList()
    proxies=proxy.proxy_list
    while True:
        try:
            print('\nChoose An Option to See the Proxies')
            print('---'*25)
            for option in ['1.List All Proxies','2.Filter List of Proxies\n',]:
                print(option)
            
            opt=int(input('Enter Option Number: '))

            if opt==1:
                
                no_of_proxies=int(input('Enter How Many Number of Proxies You want to See :'))
                
                if len(proxies)<no_of_proxies:
                    print('The Number You have Provided is Currently more than the Proxies Available')
                
                all_proxy_list=[]
                for index in range(no_of_proxies):
                    all_proxy_list.append(proxies[index])
                    
                print_proxy(all_proxy_list)
            
            elif opt==2:

                for filter_options in ['1.Based On Country','2.Based On Anonymity\n']:
                    print(filter_options)
                
                
                filter_opt=int(input('Enter Option Number :'))

                if filter_opt==1:

                    country=input('Enter Country Name :')
                    print_proxy(proxy.find_proxy_by_country(country))

                elif filter_opt==2:

                    for filter_options in ['1.Elite Proxy','2.Anonymous Proxy\n']:
                        print(filter_options)
                    anonymity=int(input('Enter Option Number :'))

                    if anonymity==1:
                        print_proxy(proxy.find_elite_proxy())
                    
                    elif anonymity==2:
                        print_proxy(proxy.find_anonymous_proxy())
                    
                else:
                    print('Wrong Option')


        except KeyboardInterrupt:
            sys.exit(0)
import requests
from bs4 import BeautifulSoup
import csv



def scraping(payload,name):
    
    with open (name,'w', newline='',encoding='utf-8') as csvfile:
        fielname=['resolucion','identificador','resumen','estado']
        writer=csv.DictWriter(csvfile,fieldnames=fielname)
        writer.writeheader()
    #response = requests.get('https://app.scrapingbee.com/api/v1/', params=params)
    
        response = requests.get('https://api.scraperapi.com', params=payload)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            normas = soup.find('div',class_='region region-content').find('div',class_='content').find_all('div',class_='node node-norma-juridica node-teaser')
            paginas = soup.find('div',class_='region region-content').find('div',class_='content').find('div',class_="item-list")
            for norma in normas:
                if norma.find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix') is not None:
                    estado = norma.find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix').find("div",class_='field-items').find("div",class_='field-item even').a.text
                else:
                    estado = 'No disponible'
                resolucion = norma.find('h2',class_='title').a.text
                if norma.find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix') is not None:
                    identificador_de_norma = norma.find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                else:
                    identificador_de_norma = 'No disponible'
                resumen = norma.find('div',class_='content clearfix').find('div',class_='field field-name-body field-type-text-with-summary field-label-above').find('div',class_='field-items').find('div',class_='field-item even').p.text

                writer.writerow({
                    'resolucion':resolucion,
                    'identificador':identificador_de_norma,
                    'resumen':resumen,
                    'estado':estado
                })
            if paginas is not None:
                otras_paginas = paginas.find('ul',class_="pager").find_all('li',class_="pager-item")
                for paginas1 in otras_paginas:
                    a = paginas1.find('a')
                    href = a['href']
                    payload['url']= "https://www.gacetaoficial.gob.cu"+href
                    
                    #response1 = requests.get('https://app.scrapingbee.com/api/v1/', params=params)
                    response1 = requests.get('https://api.scraperapi.com', params=payload)
                    if response1.status_code == 200:
                        soup1 = BeautifulSoup(response1.text,'html.parser')
                        normas1 = soup1.find('div',class_='region region-content').find('div',class_='content').find_all('div',class_='node node-norma-juridica node-teaser')
                        for norma1 in normas1:
                            
                            if norma1.find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix') is not None:
                                estado = norma1.find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix').find("div",class_='field-items').find("div",class_='field-item even').a.text

                            else:
                                estado = 'No disponible'
                            resolucion = norma1.find('h2',class_='title').a.text
                            if norma1.find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix') is not None:
                                identificador_de_norma = norma1.find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                            
                            else:
                                identificador_de_norma = 'No disponible'
                            resumen = norma1.find('div',class_='content clearfix').find('div',class_='field field-name-body field-type-text-with-summary field-label-above').find('div',class_='field-items').find('div',class_='field-item even').p.text

                            writer.writerow({
                                    'resolucion':resolucion,
                                    'identificador':identificador_de_norma,
                                    'resumen':resumen,
                                    'estado':estado
                                    })
                    else:
                        print(f"Error: {response.status_code}")
                
                
            csvfile.closed
        else:
            print(f"Error: {response.status_code}")



url = ["https://www.gacetaoficial.gob.cu/es/artes-de-pesca","https://www.gacetaoficial.gob.cu/es/autorización-de-pesca","https://www.gacetaoficial.gob.cu/es/período-de-pesca","https://www.gacetaoficial.gob.cu/es/pesca","https://www.gacetaoficial.gob.cu/es/pesca-ilegal","https://www.gacetaoficial.gob.cu/es/prohibición-de-pesca"]
names=['data/artes_de_pesca.csv','data/autorizacion.csv','data/periodo_de_pesca.csv','data/pesca.csv','data/pesca_ilegal.csv','data/prohibicion_de_pesca.csv']

#API_KEY = "RBXGBJ4QGJZW5CJYE42MRF3X765IQZZX4ERWD5EI2QD2YFH1MJ3Y3QV7USZKPVE4MPZ6QROME2GVB1IH"

APIKEY='34e4d4a1a227d76dfe3b0dc97110bede'
for i,name in enumerate(names):
    '''params = {
    'api_key': API_KEY,
    'url': url[i],
    'render_js': 'false'
    }'''
    payload = {'api_key':APIKEY, 'url': url[i]}
    scraping(payload,name)



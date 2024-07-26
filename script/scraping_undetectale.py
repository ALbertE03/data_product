import requests
from bs4 import BeautifulSoup
import csv



def scraping(payload,name):
    
    with open (name,'w', newline='',encoding='utf-8') as csvfile:
        fielname=['resolución','publicado','identificador','resumen','numero','año','norma_que_modifica','normas_que_la_modifican','norma_que_la_deroga','estado','normas_que_deroga']
        writer=csv.DictWriter(csvfile,fieldnames=fielname)
        writer.writeheader()
        #response = requests.get('https://app.scrapingbee.com/api/v1/', params=params)
    
        response = requests.get('https://api.scraperapi.com', params=payload)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            normas = soup.find('div',class_='region region-content').find('div',class_='content').find_all('div',class_='node node-norma-juridica node-teaser')
            paginas = soup.find('div',class_='region region-content').find('div',class_='content').find('div',class_="item-list")
            for norma in normas:
                resolucion = norma.find('h2',class_='title').a.text
                normas_que_deroga=""
                la_deroga = norma.find('div',class_='node-links').find('ul',class_='links inline').find('li',class_='node-readmore first last').find('a')
                href1 = la_deroga['href']
                payload['url']= "https://www.gacetaoficial.gob.cu"+href1
                response2 = requests.get('https://api.scraperapi.com', params=payload)
                soup1= BeautifulSoup(response2.text,'html.parser')

                if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-gaceta-oficial-norma field-type-viewfield field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').find('div',class_='view-content') is not  None:
                    publicado= soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-gaceta-oficial-norma field-type-viewfield field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').find('div',class_='view-content').find('div',class_='views-row views-row-1 views-row-odd views-row-first views-row-last').find('div',class_='views-field views-field-title').a.text
                else:
                    publicado = 'No disponible'
                print(publicado)

                if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix') is not  None:
                    identificador_de_norma = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                else:
                    identificador_de_norma = 'No disponible'
                print(identificador_de_norma)

                resumen = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-body field-type-text-with-summary field-label-above').find('div',class_='field-items').div.p.text

                if  soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-numero-v field-type-text field-label-inline clearfix') is not None:
                    numero = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-numero-v field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                else:
                    numero = 'No disponible'

                año = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-anno-norma field-type-datestamp field-label-inline clearfix').find('div',class_='field-items').div.span.text

                if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-modifica-norma field-type-entityreference field-label-above') is not None:
                    norma_que_modifica = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-modifica-norma field-type-entityreference field-label-above').find('div',"field-items").div.a.text
                else:
                    norma_que_modifica = "No modifica"

                norma_que_la_modifica = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-que-la-modifican field-type-viewfield field-label-above').find('div',class_='field-items').find('div',class_='field-item even').div.text
                norma_que_la_deroga = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-norma-que-la-deroga field-type-viewfield field-label-above').find('div',class_='field-items').find('div',class_='field-item even').div.text
                
                if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix') is not None:
                    estado = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').a.text
            
                else:
                    estado = 'No disponible'
                if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-deroga-norma field-type-entityreference field-label-above') is not None:
                    listas = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-deroga-norma field-type-entityreference field-label-above').find('div',class_='field-items').find_all('div')
                    for div in listas:
                        ld= div.a.text
                        ld+=','
                        normas_que_deroga+=ld
                else:
                    normas_que_deroga = "No deroga"
                writer.writerow({
                    'resolución':resolucion,
                    'publicado':publicado,
                    'identificador':identificador_de_norma,
                    'resumen':resumen,
                    'numero':numero,
                    'año':año,
                    'norma_que_modifica':norma_que_modifica,
                    'normas_que_la_modifican':norma_que_la_modifica,
                    'norma_que_la_deroga':norma_que_la_deroga,
                    'estado':estado,
                    'normas_que_deroga':normas_que_deroga
                    
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
                            resolucion = norma1.find('h2',class_='title').a.text
                            normas_que_deroga=""
                            la_deroga = norma1.find('div',class_='node-links').find('ul',class_='links inline').find('li',class_='node-readmore first last').find('a')
                            href1 = la_deroga['href']
                            payload['url']= "https://www.gacetaoficial.gob.cu"+href1
                            response2 = requests.get('https://api.scraperapi.com', params=payload)
                            soup1= BeautifulSoup(response2.text,'html.parser')

                            if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-gaceta-oficial-norma field-type-viewfield field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').find('div',class_='view-content') is not  None:
                                publicado= soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-gaceta-oficial-norma field-type-viewfield field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').find('div',class_='view-content').find('div',class_='views-row views-row-1 views-row-odd views-row-first views-row-last').find('div',class_='views-field views-field-title').a.text
                            else:
                                publicado = 'No disponible'
                            print(publicado)
                            if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix') is not  None:
                                identificador_de_norma = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-identificador-de-norma field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                            else:
                                identificador_de_norma = 'No disponible'

                            resumen = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-body field-type-text-with-summary field-label-above').find('div',class_='field-items').div.p.text

                            if  soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-numero-v field-type-text field-label-inline clearfix') is not None:
                                 numero = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-numero-v field-type-text field-label-inline clearfix').find('div',class_='field-items').div.text
                            
                            else:
                                numero = 'No disponible'

                            año = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-anno-norma field-type-datestamp field-label-inline clearfix').find('div',class_='field-items').div.span.text

                            if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-modifica-norma field-type-entityreference field-label-above') is not None:
                                norma_que_modifica = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-modifica-norma field-type-entityreference field-label-above').find('div',"field-items").div.a.text
                            else:
                                norma_que_modifica = "No modifica"

                            norma_que_la_modifica = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-que-la-modifican field-type-viewfield field-label-above').find('div',class_='field-items').find('div',class_='field-item even').div.text
                            norma_que_la_deroga = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-norma-que-la-deroga field-type-viewfield field-label-above').find('div',class_='field-items').find('div',class_='field-item even').div.text
                            
                            if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix') is not None:
                                estado = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-estado-norma-juridica field-type-taxonomy-term-reference field-label-inline clearfix').find('div',class_='field-items').find('div',class_='field-item even').a.text
                        
                            else:
                                estado = 'No disponible'

                            if soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-deroga-norma field-type-entityreference field-label-above') is not None:
                                listas = soup1.find('div',class_='container content-main').find('div',class_='region region-content').find('div',class_='content').find('div',class_='node node-norma-juridica').find('div',class_='content clearfix').find('div',class_='field field-name-field-normas-deroga-norma field-type-entityreference field-label-above').find('div',class_='field-items').find_all('div')
                                for div in listas:
                                    ld= div.a.text
                                    ld+=','
                                    normas_que_deroga+=ld
                            else:
                                normas_que_deroga = "No deroga"
                            
                            writer.writerow({
                                'resolución':resolucion,
                                'publicado':publicado,
                                'identificador':identificador_de_norma,
                                'resumen':resumen,
                                'numero':numero,
                                'año':año,
                                'norma_que_modifica':norma_que_modifica,
                                'normas_que_la_modifican':norma_que_la_modifica,
                                'norma_que_la_deroga':norma_que_la_deroga,
                                'estado':estado,
                                'normas_que_deroga':normas_que_deroga
                                
                            })
                    else:
                        print(f"Error: {response.status_code}")
                
                
            csvfile.closed
        else:
            print(f"Error: {response.status_code}")






url = ["https://www.gacetaoficial.gob.cu/es/autorización-de-pesca","https://www.gacetaoficial.gob.cu/es/artes-de-pesca","https://www.gacetaoficial.gob.cu/es/período-de-pesca","https://www.gacetaoficial.gob.cu/es/pesca","https://www.gacetaoficial.gob.cu/es/pesca-ilegal","https://www.gacetaoficial.gob.cu/es/prohibición-de-pesca"]
names=['data/autorizacion.csv','data/artes_de_pesca.csv','data/periodo_de_pesca.csv','data/pesca.csv','data/pesca_ilegal.csv','data/prohibicion_de_pesca.csv']

#API_KEY = "RBXGBJ4QGJZW5CJYE42MRF3X765IQZZX4ERWD5EI2QD2YFH1MJ3Y3QV7USZKPVE4MPZ6QROME2GVB1IH"

APIKEY='34e4d4a1a227d76dfe3b0dc97110bede'
for i,name in enumerate(names):
                
    payload = {'api_key':APIKEY, 'url': url[i]}
    scraping(payload,name)
    
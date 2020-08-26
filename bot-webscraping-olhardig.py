import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

urls = ['https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584','https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786','https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030','https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772','https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999','https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683']
def gera_json(url):
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    texto_div = soup.find(class_='mat-txt')
    paragrafos = texto_div.find_all('p')

    conteudo = []

    for paragrafo in paragrafos:
        remove = ''.join(paragrafo.text.split('"'))
        remove_linha = ''.join(remove.split('”'))
        remove_aspas = ''.join(remove_linha.split('“'))

        texto = remove_aspas
        conteudo.append(texto)

    body = ''.join(conteudo)

    author = soup.find(class_='meta-item meta-aut').text

    title = soup.find("meta",  property="og:title")['content']

    type_document = soup.find("meta",  property="og:type")['content']

    obj = {
        'author': author,
        'body': body,
        'title': title,
        'type': type_document,
        'url': url
    }

    def cria_nome(author):
        nome = author.split(',')[0]
        nome2 ='a'.join(nome.split('Ã'))
        nome3 = ''.join(nome2.split('£'))
        nome_formatado = '_'.join(nome3.split(' ')).lower() + '.json'
        return nome_formatado



    with open(cria_nome(author), 'w', encoding='utf-8') as json_file:
        json.dump(obj, json_file, ensure_ascii = False)

for url in urls:
    gera_json(url)
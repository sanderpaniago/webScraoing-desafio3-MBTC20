import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos'

req = requests.get(url)
content = req.content

soup = BeautifulSoup(content, 'html.parser')

texto_div = soup.find(class_='content-single__sidebar-content__content')
paragrafos = texto_div.find_all('p')

conteudo = []


for paragrafo in paragrafos:
  remove = ''.join(paragrafo.text.split('"'))
  remove_linha = ''.join(remove.split('”'))
  remove_aspas = ''.join(remove_linha.split('“'))

  texto = remove_aspas
  conteudo.append(texto)

del conteudo[-2:]

body = ''.join(conteudo)

title = soup.find("meta",  property="og:title")['content']

type_document = soup.find("meta",  property="og:type")['content']



obj = {
  'author': 'Isabella Câmara',
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

with open(cria_nome('Isabella Camara'), 'w', encoding='utf-8') as json_file:
    json.dump(obj, json_file, ensure_ascii = False)
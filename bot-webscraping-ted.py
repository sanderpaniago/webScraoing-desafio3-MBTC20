import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

urls = ['https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674', 'https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br', 'https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br', 'https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br', 'https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br', 'https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br', 'https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br']




def gera_body(soup):
  conteudo_div = soup.find_all(class_='Grid--with-gutter')
  conteudos = []

  for cont in conteudo_div:
    p = cont.find('p').text
    textConvertido = convertText(p)
    conteudos.append(textConvertido)

  textoFinal = ''.join(conteudos)
  return textoFinal  

def get_title(soup):
  limpa_title = soup.find("meta",  property="og:title")['content']
  title = ''.join(limpa_title.split('"'))
  return title

def get_author(soup):
  lista = soup.title.text
  separando_lista = lista.split(':')
  author = separando_lista[0]
  return author

def convertText(texto):
  text = ' '.join(texto.split('\n\t\t\t\t\t\t\t\t\t\t\t'))
  text2 = ' '.join(text.split('\n\t\t\t\t\t\t\t\t\t'))
  text3 = ' '.join(text2.split('\n'))
  text4 = ''.join(text3.split('"'))
  return text4

def get_type(soup):
    type_document = soup.find("meta",  property="og:type")['content']
    return type_document


def gera_json(url):
  req = requests.get(url)
  content = req.content

  soup = BeautifulSoup(content, 'html.parser')

  author = get_author(soup)
  body = gera_body(soup)
  title = get_title(soup)
  type_document = get_type(soup)


  obj = {
    'author': author,
    'body': body,
    'title': title,
    'type': 'video',
    'url': url
  }
  arquivo = '_'.join(author.split(' ')).lower() + '.json'

  with open( arquivo , 'w', encoding='utf-8') as json_file:
    json.dump(obj, json_file, ensure_ascii = False)

    return 'Operação concluida com sucesso'



for url in urls: 
  gera_json(url)
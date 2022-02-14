import requests
import json


def Cep(codigo):
  
  url=requests.get(f'https://cep.awesomeapi.com.br/json/{codigo}')
  ctd = json.loads(url.content)

  del ctd['ddd']
  del ctd['address_type']
  del ctd['address_name']
  del ctd['lat']
  del ctd['lng']
  del ctd['cep']
  ctd['Endereco:']=ctd.pop('address')
  del ctd['city_ibge']
  ctd['Cidade:']=ctd.pop('city')
  ctd['Bairro:']=ctd.pop('district')
  ctd['Estado:']=ctd.pop('state')


  lista=[]
  for i in ctd:
    lista.append(f'{i} {ctd.get(i)}')

  return lista

def maps(codigo):
  map_url=requests.get(f'https://cep.awesomeapi.com.br/json/{codigo}')
  map_ctd = json.loads(map_url.content)

  

  latitude = map_ctd['lat']
  longitude = map_ctd['lng']

  url = f'https://www.google.com/maps?api=1&q={float(latitude)}%2C{float(longitude)}&hl=es;z=14&output=embed'
  
  return url


  


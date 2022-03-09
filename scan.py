import sys
import re
import socket
import requests as r
from os import system
from time import sleep
from bs4 import BeautifulSoup as b

ports = []

url = r.get("https://documentacao.senior.com.br/gestao-de-pessoas-hcm/6.2.35/captura/portslist.htm").content

html = b(url, "html.parser")

div = html.find("div", class_="body")

for a in div.find_all("table"):
  tbody = a.find_all('tbody')
  for a in tbody:
    tr = a.find_all('tr')
    for a in tr:
      td = a.findAll('td')
      for a in td:
        striped = str(a.text.split())
        kk = re.findall('\d+', striped)
        for a in kk:
         ports.append(a)
         for a in kk:
           with open('ports.txt', 'a') as w:
             w.write(f'{a}\n')
           print(f"Carregando lista de PORTAS! aguarde ")
           sleep(0.2)
           system("clear")
           print(f"Carregando lista de PORTAS! aguarde. ")
           sleep(0.2)
           system("clear")
           print(f"Carregando lista de PORTAS! aguarde.. ")
           sleep(0.2)
           system("clear")
           print(f"Carregando lista de PORTAS! aguarde... ")
           sleep(0.2)
           system("clear")
print("finalizado.")

lista = []

with open('ports.txt', 'r') as r:
  read = r.read().split()
  print(f"total portas: {len(ports)}")
  print('-'*40)
  for num in read:
    if num not in lista:
      lista.append(num)
    else:
      print(f'removendo duplicada {num} aguarde...')
      pass

with open('ports.txt', 'w+') as w:
  for a in lista:
    w.write(f"{a}\n")

try:
  IP_SCAN = str(sys.argv[1])
  print()
except:
  print()
  print("ERRO! IP MAL INFORMADO OU FORA DE SERVIÇO")
  sys.exit()

system("clear")
print("~~~~~~~~~~~~~ SCAN IP/SITE VIA PORT ~~~~~~~~~~~~~ ")

with open('ports.txt') as ler:
  ports_ = ler.read().split()

  for port in ports_:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(0.5)

    connect = client.connect_ex((IP_SCAN, int(port)))
    if connect == 0:
      print(f"Status: {connect}   => port {port} open")
    else:
      print(f"Status: {connect}  => port {port}")

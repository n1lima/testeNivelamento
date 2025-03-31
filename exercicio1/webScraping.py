import requests
from bs4 import BeautifulSoup
import zipfile

response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

content = response.content

site = BeautifulSoup(content, 'html.parser')

pdf_links = site.find_all('a', class_='internal_link', href=True)#Preferi optar por buscar a classe dos dois links, que tem o mesmo nome 'internal_link'

pdf_urls = []#Criei uma lista vazia para poder colocar as urls corretas, pois, não é certo que só usando a class delas que irá achar elas

for link in pdf_links:  #Percorre todos os links encontrados
    href = link['href']  #Irá pegar apenas a url achada do link

    #Verifica se o link termina em .pdf, pois o anexo I possui uma extensão '.xls'
    if href.endswith('.pdf'):
        
        #Verifica se é um dos arquivos que queremos
        if 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf' in href or \
           'Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf' in href:
            pdf_urls.append(href)  #Caso for um desses arquvios, adiciona à lista 


#Aqui baixa apenas os PDFs desejados
for pdf_url in pdf_urls:
    pdf_name = pdf_url.split('/')[-1]  #Pega apenas o nome do arquivo
    response = requests.get(pdf_url)  #Realiza o download do PDF
    with open(pdf_name, 'wb') as file:
        file.write(response.content)#Grava o contéudo no arquivo

#Aqui compacta em zip urilizando a biblioteca zipfile 
with zipfile.ZipFile('anexos.zip', 'w') as zipf:
    for pdf in pdf_urls:
       pdf_name = pdf.split("/")[-1] #Pega apenas o nome do arquivo novamente
       zipf.write(pdf_name)  #Adicionando ao ZIP
print('Arquivos compactados em anexos.zip')#Finalizando, aparecendo no terminal, quando o processo é concluído
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as error:
    print('\33[31mO site Pudim não está acessível no momento.\33[m')
else:
    print('\33[32mConsegui acessar o site Pudim com sucesso!\33[m')

    # conteúdo html do site
    print(site.read())

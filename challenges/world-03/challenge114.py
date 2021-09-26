import requests

try:
    requests.get('http://www.pudim.com.br')
    print('\33[32mConsegui acessar o site Pudim com sucesso!\33[m')
except Exception as error:
    print('\33[31mO site Pudim não está acessível no momento.\33[m')


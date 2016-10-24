# -*- coding: UTF-8  -*-
# autor @EXPL01T3R0
import bs4, requests

def get_acao(code):
    global msg
    acao = bs4.BeautifulSoup(requests.get('http://cotacoes.economia.uol.com.br/acao/index.html?codigo='+str(code)).text, 'html.parser')
    if acao.find(class_='error'):
        return('Nenhum dado encontrato para esse cÃ³digo')
    else:
        data = acao.find(class_='data').text
        dados = acao.find('tbody').text.split('\n')
        dados.pop(0);dados.pop(0)
        info = acao.find('dl').text.split('\n')
        return('''
Data: {data}
Horario: {hora}
------------------
Acao: {nacao}
Code: {code}
Isin: {isin}

Status:       {status}
Ultimo Valor: {ult}
Maior Valor:  {maior}
Menor Valor:  {menor}
Abertura:     {abert}
Volume:       {volume}'''.format(data = data, hora = dados[1], nacao = info[8], code = code, isin = info[10], status = dados[0], ult = dados[4],
                                 maior = dados[5], menor = dados[6], abert = dados[7], volume = dados[8]))


code = input('Codigo da acao: ')
print(get_acao(code))

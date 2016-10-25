# -*- coding: UTF-8  -*-
# autor @EXPL01T3R0
import bs4, requests

def get_acao(code):
    global msg
    acao = bs4.BeautifulSoup(requests.get(
        'http://cotacoes.economia.uol.com.br/acao/index.html?codigo=' + str(code)).text, 
        'html.parser')
    if acao.find(class_='error'):
        return('Nenhum dado encontrato para esse código da ação.')
    else:
        data = acao.find(class_='data').text
        dados = acao.find('tbody').text.split('\n')
        dados.pop(0);dados.pop(0)
        info = acao.find('dl').text.split('\n')
        return(
            u'Resultado da consulta: '     + '\n'
            + u'---------------------'     + '\n'
            + u'Data: '         + data     + '\n'
            + u'Horário: '      + dados[1] + '\n'
            + u'---------------------'     + '\n'
            + u'Ação: '         + info[8]  + '\n'
            + u'Code: '         + code     + '\n'
            + u'Isin: '         + info[10] + '\n'
            + u''                          + '\n'
            + u'Status:       ' + dados[0] + '\n'
            + u'Último Valor: ' + dados[4] + '\n'
            + u'Maior Valor:  ' + dados[5] + '\n'
            + u'Menor Valor:  ' + dados[6] + '\n'
            + u'Abertura:     ' + dados[7] + '\n'
            + u'Volume:       ' + dados[8] + '\n'
        )

code = input('Código da ação: ')
print(get_acao(code))

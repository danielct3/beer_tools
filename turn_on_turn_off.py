# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 05:40:57 2018

@author: daniel
"""

import datetime 
import config
import time
import le_arq_temp
import liga_geladeira
import logging


def dia_hora():
    return " -- "+time.strftime('%d/%m/%y %X')

inter_geladeira = config.intervalo_geladeira 
delta_temperatura = config.delta_temperatura
temperatura_alvo = config.temperatura_alvo

logging.basicConfig(filename='cerveja.log',level=logging.DEBUG)
logging.info("Teste do Logging "+dia_hora())


liga_gel = False

while True:
    if ( le_arq_temp.gettemp()  >= (delta_temperatura + temperatura_alvo)) and (liga_gel == False) :
        date_turn_on = datetime.datetime.now()
        liga_gel = True
        
        ## aqui ficarah o comando para ligar a geladeira
        liga_geladeira.liga_geladeira() 
        #print 'a geladeira foi ligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    if ( le_arq_temp.gettemp()  <= (delta_temperatura - temperatura_alvo)) and (liga_gel == True) :  
        liga_gel = False
        ### comando para desligar a geladeira
        liga_geladeira.desliga_geladeira()
        #print 'a geladeira foi desligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    if (date_turn_on+datetime.timedelta(seconds=10) < datetime.datetime.now()) and (liga_gel == True):
        liga_gel = False
        ### comando para desligar a geladeira
        liga_geladeira.desliga_geladeira()

        #print 'a geladeira foi desligada'
        #print 'liga_gel esta em : ',liga_gel
        #print '--------------------'
        #print datetime.datetime.now()
        
    #print datetime.datetime.now()    
    time.sleep(2) 






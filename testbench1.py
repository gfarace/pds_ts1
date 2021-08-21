#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21/8/2021

@author: Gisela Farace

Descripción:

En este primer trabajo comenzaremos por diseñar un generador de señales que utilizaremos en las primeras simulaciones que hagamos. La primer tarea consistirá en programar una función que genere señales senoidales y que permita parametrizar:

- la amplitud máxima de la senoidal (volts)
- su valor medio (volts)
- la frecuencia (Hz)
- la fase (radianes)
- la cantidad de muestras digitalizada por el ADC (# muestras)
- la frecuencia de muestreo del ADC.
es decir que la función que uds armen debería admitir se llamada de la siguiente manera

tt, xx = mi_funcion_sen( vmax = 1, dc = 0, ff = 1, ph=0, nn = N, fs = fs)
Recuerden que tanto xx como tt deben ser vectores de Nx1. Puede resultarte útil el módulo de visualización matplotlib.pyplot donde encontrarán todas las funciones de visualización estilo Matlab. Para usarlo:

import matplotlib.pyplot as plt
plt.plot(tt, xx)

"""

# Ejemplificaremos el uso de las herramientas que utilizaremoos frecuentemente 

# Importación de módulos
import numpy as np
#import scipy.signal as sig
import matplotlib as mpl
# la siguiente línea solo afecta en caso que lo quisiéramos correr desde la línea de comandos
mpl.use('Qt5Agg')

import matplotlib.pyplot as plt
import pdsmodulos as pds

#%% Separación de bloques de código para ordenar tu trabajo "#%%"

#%%  Inicialización

#%%  Generación de señales de prueba

#%%  Presentación de resultados


#%%  Inicialización de librerías

# Setup inline graphics
mpl.rcParams['figure.figsize'] = (10,10)

#%%  funcion que recibe los parametros para crear una senoidal
      
def mi_senoidal(vmax, dc, ff, ph, nn, fs):
    ts = 1/fs # tiempo de muestreo
    df = fs/nn # resolución espectral
    
    # grilla de sampleo temporal
    #empieza en 0, termina en (nn-1)*ts y tiene nn números
    #tt es de nn filas x 1 columna
    tt = np.linspace(0, (nn-1)*ts, nn).flatten()
    
    # grilla de sampleo frecuencial
    sen = vmax*np.sin(2*np.pi*ff*tt + ph)+dc
    
    return tt, sen
    #%% Presentación gráfica de los resultados
    
    plt.figure(1)
    line_hdls = plt.plot(tt, xx)
    plt.title('Señal senoidal')
    plt.xlabel('tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    #    plt.grid(which='both', axis='both')
    
    # presentar una leyenda para cada tipo de señal
    axes_hdl = plt.gca()
    
    # este tipo de sintaxis es *MUY* de Python
    plt.show()
#%% Comienzo de nuestro script
    ##########################
 

# Invocamos a nuestro testbench exclusivamente: 
      
tt,xx = mi_senoidal(vmax=1, dc=0, ff=1, ph=0, nn=1000, fs=100)
   


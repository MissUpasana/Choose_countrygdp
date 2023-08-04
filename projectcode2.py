# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:00:47 2022

@author: Upasna_Ayush
"""

import matplotlib.pyplot as plt

Year=[1982,1992,2002,2012,2014,2016,2018,2019]

Country_Dict={
    1:'India',
    2:'US',
    3:'UK',
    4:'Japan',
    5:'Sub-Saharan African Region',
    6:'Srilanka',
    7:'Afganisthan',
    8:'United Arab Emirates'
    }


GNI_Dict={
     'India':[290,340,460,1480,1560,1680,2010,2120,],
     'US':[14220,25680,37310,52780,55880,57130,6490,65970],
     'UK':[10660,21480,29180,41940,44670,43460,42410,43460],
     'Japan':[10550,30540,34780,49470,43970,37820,41100,41450],
     'Sub-Saharan African Region':[730.130,620.999,583.503,1709.908,1183.175,1579.792,1540.740,1588.855],
     'Srilanka':[310,550,840,3360,3640,3180,4040,4010],
     'Afganisthan':[0,0,0,630,630,550,510,520],
     'United Arab Emirates':[10550,21480,30940,39220,44370,39220,41470,43450]
     }
   

GDP_Dict={
    'India':[20.715,288.882,518.938,1832,2039,2295,2701,2871],
    'US':[3344,6520,10936,16197,17572,18745,20167,2143],
    'UK':[515049,1180,1784,2719,3087,2723,2901,2898],
    'Japan':[1135,3909,4183,6272,4879,5004,5037,5197],
    'Sub-Saharan African Region':[342.182,337.902,441.129,1667,18351563,1540,1588.858,1555],
    'Srilanka':[4796,9703,16.573,79.556,79.563,82.410,87.963,83.991],
    'Afganisthan':[0,04.055,19.907,20.479,18.117,18.053,18.799],
    'United Arab Emirates':[46.623,54.239,109.846,374.591,403.137,357.047,422.215,417.216]
    }

def Run():
    i=int(input("Enter the Country choice: "))
    c=Country_Dict[i]
    print('Country you chose is ',c)
    j=int(input("Enter 1 for GDP or 2 for GNI or 3 for both GDP & GNI: "))
    if j==1:
        plt.plot(GDP_Dict[c],Year)
        plt.xlabel('GDP_billions')
        plt.ylabel('Year')
        q='GDP of '+ c
        plt.title(q)
        plt.show()
    elif j==2:
        plt.plot(GNI_Dict[c],Year)
        plt.xlabel('GNI($)')
        plt.ylabel('Year')
        p='GNI of '+ c
        plt.title(p)
        plt.show()
    else:
       plt.plot(GDP_Dict[c],Year)
       plt.plot(GNI_Dict[c],Year)
       t='GNI '+'GDP '+ c
       plt.title(t)
       plt.show()
           
       
Run()



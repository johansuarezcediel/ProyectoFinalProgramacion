# -*- coding: utf-8 -*-

import math 

def calcular_movimiento(angulo,coef_roza,masa1):
    valor=angulo*math.pi/180
    datos=[]
    subdatos=[]
    subiendo="subiendo"
    bajando="bajando"
    masa2=0
    booleanoprueba=True
    valor2=masa1*((math.sin(valor))-(coef_roza*math.cos(valor)))
    
    while booleanoprueba:
        if masa2<valor:
            subdatos.append(masa2)
            subdatos.append(subiendo)
        else:
            subdatos.append(masa2)
            subdatos.append(bajando)      
        datos.append(subdatos)
        subdatos=[]
        if masa2>valor2:
            booleanoprueba=False
        masa2+=0.5
    return datos
            
            

    
def calcular_angulo(coef_roza,masa1,masa2):
    resp=-1
    valor=10
    valorfinal=0
    
    for i in range (75):
        valorfinal=round(masa1*9.8*(coef_roza*math.cos(math.radians(i+valor))-math.sin(math.radians(i+valor)))+masa2*9.8)
        if valorfinal==0:
             resp=i+valor
             break
    return resp


class main:
    angulo=0
    coef_razo=0
    masa1=0
    print(calcular_movimiento(55,0.15,6))
    print(calcular_angulo(0.15,6,4.5))
    
    

                                                   
#Generar pares forma normal
"""def generarpares(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num=num+1
    return milista
print(generarpares(10))"""

#Generar pares tipo generador yield
"""def generarpares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvepares=generarpares(10)
for i in devuelvepares:
    print (i)"""

#Devuelve  tres primeros tres terminos del generador 
"""def generarpares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvepares=generarpares(10)
print (next(devuelvepares))
print("aca va mas codigo")
print (next(devuelvepares))
print("aca va mas codigo")
print (next(devuelvepares))"""
# Generador yield from para acceder a los subelementos de un elemento
"""def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
       # for subelemento in elemento:
            yield from elemento
ciudades_devueltas=devuelve_ciudades("madrid","colombia","franacia","peru")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))"""











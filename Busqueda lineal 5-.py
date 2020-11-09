def busquedalineal(x,y):
    encontrar=False
    posicion=0
    while posicion<len(y) and not encontrar:
        if y[posicion]==x:
            encontrar=True
        posicion= posicion+1
    return encontrar        
estados=['Coahuila',
         'Nuevo Leon',
         'Tamaulipas',
         'Chihuahua',
         'Sonora']

buscar=input('Estado a buscar: ')
busqueda=busquedalineal(buscar,estados)
if busqueda:
    data={}
    
    data['Coahuila']=[]
    data['Coahuila'].append({'Muertes':15645,
                             'Recuperados':7852,
                            'Hospitalizados':180})
    data['Nuevo Leon']=[]
    data['Nuevo Leon'].append({'Muertes':15,
                             'Recuperados':782,
                            'Hospitalizados':10})
    for c in data[buscar]:
        print('Muertes:',c['Muertes'])
        print('Recuperados:',c['Recuperados'])
        print('Hospitalizados:',c['Hospitalizados'])
else:
    print('No encontrado')
    

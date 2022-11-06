import os

os.system('cls')

class Coordenadas:
    def __init__(self):
        self.cox, self.coy = [int(x) for x in input('Coordenada de origem: ').split()] 

        #Vai guardar as coordenadas e seus quadrantes correspondentes.
        resultados = []

        #armazena os resultados euclidianos e sua coordenadas
        euclidianos = {}

        n = int(input('\nQuantas coordenadas serão inseridas? '))

        #Vai definir o quadrantes das N coordenadas que foram inseridas.
        for i in range(n):
            x, y = [int(x) for x in input().split()]

            if x == self.cox or y == self.coy:
                result = 'Coordenada ({},{}): Linha de Origem'.format(x,y)
            elif x > 0 and y > 0:
                result = 'Coordenada ({},{}): Primeiro Quadrante'.format(x,y)
            elif x < 0 and y > 0:
                result = 'Coordenada ({},{}): Segundo Quadrante'.format(x,y)
            elif x < 0 and y < 0: 
                result = 'Coordenada ({},{}): Terceiro Quadrante'.format(x,y)
            else: 
                result = 'Coordenada ({},{}): Quarto Quadrante'.format(x,y)
            
            #pitagoras
            euclid = float(((((x - self.cox)**2) + ((y - self.coy)**2)) **0.5))

            resultados.append(result)
            
            #Armazena os maiores e menores valores, junto com sua chave, que é sua própria coordenada
            euclidianos[str('({},{})'.format(x,y))] = euclid

        #Pega o maior e menor valor, juntamente com suas chaves
        min_key = min(euclidianos, key=euclidianos.get)
        min_value = min(euclidianos.values())

        max_value = max(euclidianos.values())
        max_key = max(euclidianos, key=euclidianos.get)

        os.system('cls')

        print('Coordenada de origem({},{})\n'.format(self.cox,self.coy))

        for r in resultados:
            print('{}'.format(r))

        print(f"Ponto mais próximo: {min_key}, distancia: {min_value:.2f}")
        print(f"Ponto mais distante: {max_key}, distancia: {max_value:.2f}")
    

Coordenadas()

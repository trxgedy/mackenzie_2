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
                result = f'Coordenada ({x},{y}): Linha de Origem'
            elif x > 0 and y > 0:
                result = f'Coordenada ({x},{y}): Primeiro Quadrante'
            elif x < 0 and y > 0:
                result = f'Coordenada ({x},{y}): Segundo Quadrante'
            elif x < 0 and y < 0: 
                result = f'Coordenada ({x},{y}): Terceiro Quadrante'
            else: 
                result = f'Coordenada ({x},{y}): Quarto Quadrante'
            
            #pitagoras
            euclid = float(((((x - self.cox)**2) + ((y - self.coy)**2)) **0.5))

            resultados.append(result)
            
            #Armazena os valores euclidianos, junto com sua chave, que é sua própria coordenada
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

'''
Input:
1 -3

8

#copiar todos as coords e colar de uma vez só

5 4
2 3
-4 3
-3 1
-2 -1
-5 -3
4 -3
2 -4

'''

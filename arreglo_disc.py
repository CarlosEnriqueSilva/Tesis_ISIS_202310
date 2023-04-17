import config


class Arreglo():
    '''
    Clase que representa un arreglo
    '''

    def __init__(self):
        '''
        Inicializacion del arreglo. Crea un arreglo vacio

        Returns:
            -

        '''
        self.estructura = []

    def addNode_byValue(self, infoNodo):
        '''
        Añade un nodo al arreglo, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        self.estructura.append(infoNodo)

    def addNode_byValueFirst(self, infoNodo):
        '''
        Añade un nodo al arreglo, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        print('Metodo arreglo')
        self.estructura.insert(0,infoNodo)
        print(self.estructura)

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo al arreglo.
            Si el nodo no existe se retorna False

            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            False si el nodo no pertenece a la lista, True si el nodo se elimina de la lista

        '''
        for i in range(len(self.estructura)):
            if self.estructura[i] == infoNodo:
                del self.estructura[i]
                return True

        return False

    def getNodeValues(self):
        '''
        Da todos los elementos de la lista en el orden que se tienen

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''
        return self.estructura

    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no al arreglo

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece a la lista enlazada, False si no pertenece

        '''
        for elem in self.estructura:
            if elem == infoNodo:
                return True

        return False

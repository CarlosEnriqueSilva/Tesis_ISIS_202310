import config


class LinearProbing():
    '''
    Clase que representa una tabla hash linear probing
    '''

    def __init__(self, size):
        '''
        Inicializacion de la tabla hash linear probing. Crea una tabla hash linear probing vacia

        Returns:
            -

        '''
        self.size = size
        self.umbral = 0.7
        self.factor = 0
        self.cantLlaves = 0
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return abs(hash(key)) % self.size

    def addNode_byValue(self, key, value):
        '''
        Añade un nodo a la tabla hash linear probing, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia

        Args:
            infoNodo: Información del nodo para añadir a la lista

        Returns:
            -

        '''
        self.cantLlaves = self.cantLlaves + 1
        self.factor = self.cantLlaves / self.size

        

        index = self.hash_function(key)
        count = 0
        while self.keys[index] is not None and count <= self.size:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
            count += 1
        self.keys[index] = key
        self.values[index] = value

    def deleteNode_byValue(self, key):
        '''
        Elimina un nodo a la tabla hash linear probing.
            Si el nodo no existe se retorna False

            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.

        Args:
            infoNodo: Información del nodo que se va a eliminar

        Returns:
            False si el nodo no pertenece a la lista, True si el nodo se elimina de la lista

        '''
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def getNodeValues(self):
        '''
        Da todos los elementos de la tabla de hash en el orden que se tienen

        Args:
            -

        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''
        return self.keys

    def isNodeValue(self, key):
        '''
        Informa si un nodo pertenece o no a la tabla hash linear probing

        Args:
            infoNodo: Valor del nodo que se busca

        Returns:
            True si el nodo pertenece a la tabla de hash, False si no pertenece

        '''
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.size
        return False

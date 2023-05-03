import config
from DISClib.ADT import list as lt

class listaEnlazada():
    '''
    Clase que representa una Lista Enlazada
    '''
    def __init__(self, type):
        '''
        Inicializacion de la lista enlazada. Crea una lista enlazada vacia del tipo especificado
        
        Args:
            type: 1 si la lista es sencilla, 2 si la lista es doble

        Returns:
            -
            
        '''
        
        TODO

        return ""
    
    def addNode_byValue(self, infoNodo):
        '''
        Añade un nodo a la lista enlazada, el nodo se añade al final de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia
        
        Args:
            infoNodo: Información del nodo para añadir a la lista
        
        Returns:
            -
            
        '''
        
        TODO

        return ""

    def addFirstNode_byValue(self, infoNodo):
        '''
        Añade un nodo al arreglo, el nodo se añade al inicio de la lista.
        Si el nodo ya se encuentra en la lista, se añade una nueva instancia
        
        Args:
            infoNodo: Información del nodo para añadir a la lista
        
        Returns:
            -
            
        '''

        TODO

        return ""


    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un nodo de la lista enlazada.
            Si el nodo no existe se retorna False
            
            Si hay mas de un nodo con el valor indicado, solo se elimina una instancia.
        
        Args:
            infoNodo: Información del nodo que se va a eliminar
        
        Returns:
            False si el nodo no pertenece a la lista, True si el nodo se elimina de la lista
            
        '''

        TODO

        return ""
    
    def getNodeValues(self):
        '''
        Da todos los elementos de la lista en el orden que se tienen, iniciando por el primero
        
        Args:
            -
        
        Returns:
            Lista (python) con todos los valores de los nodos, en el orden del primero al ultimo

        '''
        lst = list()
        iter = lt.iterator(self.estructura)
        for i in iter:
            lst.append(i)
        return lst
    
    def isNodeValue(self, infoNodo):
        '''
        Informa si un nodo pertenece o no a la lista enlazada
        
        Args:
            infoNodo: Valor del nodo que se busca
        
        Returns:
            True si el nodo pertenece a la lista enlazada, False si no pertenece
            
        '''

        TODO

        return ""
    
    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve los valores de los nodos que son adyacentes a un nodo dado. En el caso de la lista enlazada sencilla, 
        el adyacente de un nodo es el siguiente, y en el caso de una lista enlazada doble, los adyacentes son
        el siguiente y el anterior
        
        Args:
            infoNodo: Información del nodo del que se buscan los adyacentes
        
        Returns:
            Lista (python) con los valores de los nodos adyacentes al nodo dado. Si no tiene adyacentes se retorna una lista vacia
            
        '''
        
        TODO

        return ""
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
        #Modelo de datos de la Estructura de Datos Arreglo
        self.estructura = []     
            # self.estructura es la variable que contendra los elementos en el arreglo
            # inicialmente vacia
            # Esta variable se puede modificar/actualizar en cada funcion de la Estructura de Datos


    def size(self):
        '''
        Retorna el numero de elementos en el arreglo
        Returns:
            Numero de elementos en el arreglo
        '''
        #TODO consultar la variable self.estructura
        return 0


    def addNode_byValue(self, infoNodo):
        '''
        Añade un elemento al FINAL arreglo.
        Si el elemento ya se encuentra en el arreglo, se añade una nueva ocurrencia

        Args:
            infoNodo: Información del elemento para añadir al arreglo

        Returns:
            -
        '''
        #TODO actualizar la variable self.estructura
        pass

    def addNode_byValueFirst(self, infoNodo):
        '''
        Añade un elemento al PRINCIPIO del arreglo.
        Si el elemento ya se encuentra en el arreglo, se añade una nueva ocurrecia

        Args:
            infoNodo: Información del elemento para añadir al arreglo

        Returns:
            -
        '''
        #TODO actualizar la variable self.estructura
        pass

    def deleteNode_byValue(self, infoNodo):
        '''
        Elimina un elemento al arreglo.
            Si hay mas de un elemento con el valor indicado, SOLO se elimina la primera ocurrencia.

        Args:
            infoNodo: Información del elemento que se va a eliminar

        Returns:
            True si el elemento se encontro y se elimino, False si el elemento NO se encontro.

        '''
        #TODO actualizar la variable self.estructura
        return False

    def getNodeValues(self):
        '''
        Retorna todos los elementos del arreglo en el orden del primero al ultimo

        Args:
            -

        Returns:
            Lista (python) con todos los elementos en el orden que aparecen

        '''
        # consulta de la variable self.estructura
        lst = []
        for elem in self.estructura:   
            lst.append(elem)
        return lst

    def isNodeValue(self, infoNodo):
        '''
        Informa si un elemento pertenece o no al arreglo

        Args:
            infoNodo: Valor del elemento que se busca

        Returns:
            True si el elemento pertenece al arreglo, False si no pertenece

        '''
        #TODO consultar la variable self.estructura
        return False

    def findAdjacentNode(self, infoNodo):
        '''
        Devuelve los elementos que son adyacentes a un elemento dado. 
        Los adyacentes son el anterior (si existe) y el siguiente (si existe) al elemento dado.

        Args:
            infoNodo: Información del elemento del que se buscan los adyacentes

        Returns:
            Lista (Python) con los elementos adyacentes al elemento dado. 
            Si el elemento NO esta en el arreglo o el elemento NO tiene adyacentes se retorna una lista vacia

        '''
        #TODO consultar la variable self.estructura
        lst = list()

        return lst
    
def comparefunction(elem_1, elem_2):
    '''
    Función de comparación entre dos elementos. Si son del mismo tipo de dato se comparan directamente, 
    de lo contrario se transforman ambos elementos a String y se realiza la comparación

    Args:
        elem_1: Elemento 1. 
        elem_2: Elemento 2.

    Returns:
        -1: Si el elemento 1 es menor al elemento 2
        0: Si el elemento 1 es igual al elemento 2
        1: Si el elemento 1 es mayor al elemento 2
    '''
    elem1C = elem_1
    elem2C = elem_2

    if type(elem_1) != type(elem_2):
        elem1C = str(elem_1)
        elem2C = str(elem_2)
    if elem1C > elem2C:
        return 1
    elif elem1C < elem2C:
        return -1
    return 0


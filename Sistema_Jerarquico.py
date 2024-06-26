class Sistema_Jerarquico:
    """
    Esta clase representa un sistema estelar jerárquico compuesto por múltiples estrellas.
    
    Atributos:
    estrellas: Una lista que contiene objetos de la clase Estrella.
    """
    def __init__(self, estrellas):
        """
        Esta función inicializa una nueva instancia de la clase Sistema_Jerarquico con la lista de estrellas.
        
        Parámetros:
        estrellas: Una lista de objetos de la clase Estrella que representan las estrellas en el sistema.
        """
        #Busco un sistema con dos o más estrellas
        if len(estrellas) < 2: 
            #uso raise porque es una excepción única
            raise ValueError("No es un sistema jerárquico") 
        self.estrellas = estrellas

    def orden_segun_masa(self):
        """
        Esta función ordena la lista de estrellas de acuerdo a su masa.
        
        Retorna:
        Una lista de estrellas ordenada por masa estelar.
        """
        return sorted(self.estrellas, key=lambda estrella: estrella.masa)
    
    def nombres_ordenados(self):
        """
        Esta función genera los nombres de las estrellas, seguidos de letras del alfabeto ordenadas.
        
        Retorna:
        Una cadena de texto que contiene los nombres de las estrellas seguidos de letras del alfabeto ordenadas.
        """
        return sorted(self.estrellas, key=lambda x: x[-1])
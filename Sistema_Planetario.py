class Sistema_Planetario:
    """
    Esta clase representa un sistema planetario.
    
    Atributos:
    planetas: Lista de objetos de la clase Planeta que conforman el sistema planetario.
    """
    def __init__(self, planetas):
        """
        Esta función inicializa una nueva instancia de la clase Sistema_Planetario con los planetas dados.
        
        Parámetros:
        planetas: Lista de objetos de la clase Planeta que conforman el sistema planetario.
        """
        self.planetas = planetas

    def numero_de_planetas(self):
        """
        Esta función devuelve el número de planetas en el sistema planetario.
        
        Retorna:
        El número de planetas en el sistema planetario.
        """
        return len(self.planetas) #Empleo len para que me devuelva del tipo entero

    def lista_orden_segun_radio(self):
        """
        Esta función devuelve la lista de planetas ordenada según su radio semi mayor de la órbita (a).
        
        Retorna:
        Una lista de objetos de la clase Planeta ordenados según su radio semi mayor de la órbita.
        """
        #La función sorted() es para ordenar y devolver una lista
        planetas_ordenados = sorted(self.planetas, key=lambda planeta: planeta.a )
        return planetas_ordenados
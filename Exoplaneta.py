class Exoplaneta(Planeta):
    """
    Esta es una clase que representa un exoplaneta, la clase hereda de la clase Planeta.
    
    Atributos:
    (Todos los atributos de la clase Planeta)
    metodo_primer_descubrimiento: El método de primer descubrimiento del exoplaneta.
    similar_a_tatooine: Indica si el exoplaneta es similar a Tatooine.
    """
    def __init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron, metodo_primer_descubrimiento, sim_tatooine):
        """
        Esta función inicializa una nueva instancia de la clase Exoplaneta con los atributos dados.
        
        Parámetros:
        estrella_anfitriona: La estrella anfitriona del exoplaneta.
        masa_planetaria: La masa del exoplaneta.
        radio: El radio del exoplaneta.
        a: El radio semi mayor de la órbita del exoplaneta.
        inclinacion: La inclinación de la órbita del exoplaneta.
        excentricidad: La excentricidad de la órbita del exoplaneta.
        argumento_periastron: El argumento del periastron del exoplaneta.
        metodo_primer_descubrimiento: El método de primer descubrimiento del exoplaneta ("imagen directa", "velocidad radial" o "tránsito").
        similar_a_tatooine: Indica si el exoplaneta es similar a Tatooine. Por defecto, False.
        """
        Planeta.__init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron)
        self.metodo_primer_descubrimiento = metodo_primer_descubrimiento
        self.sim_tatooine = sim_tatooine

    def primer_descubrimiento(self):
        """
        Esta función devuelve el método de primer descubrimiento del exoplaneta.
        
        Retorna:
        El método de primer descubrimiento del exoplaneta ("imagen directa", "velocidad radial" o "tránsito").
        """
        return self.metodo_primer_descubrimiento

    def similar_tatooine(self):
        """
        Esta función determina si el exoplaneta es similar a Tatooine.
        
        Retorna:
        True si el exoplaneta es similar a Tatooine, False si no.
        """
        if self.metodo_primer_descubrimiento == "Tránsito":
            b = self._a * np.cos(self._inclinacion) / ((1 - self._excentricidad**2) * (self._estrella_anfitriona._radio * (1 + self._excentricidad * np.sin(self._argumento_periastron))))
            return 0 < b < 1
        else:
            return self.sim_tatooine
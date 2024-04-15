import numpy as np


class Specious:
    """
    describe the growth and the number of specimen
    Parameters
    ----------
    number_of_specimen: int
        initial number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense
    Attributes
    ----------
    num: int
        number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense
    Methods
    -------
    stochastic_natural_growth
        random increase in the number of the specimen for one generation due to growth rate only

    """
    def __init__(self, number_of_specimen, growth_rate):
        self.num = number_of_specimen
        self.growth_rate = growth_rate

    def stochastic_natural_growth(self):
        """
        random increase in the number of the specimen for one generation due to growth rate only
        """
        return np.random.binomial(n=self.num, p=abs(self.growth_rate))*np.sign(self.growth_rate)


class Predator(Specious):
    """
    describes the growth, the number of predator specimen and the impact in the reproduction from prey
    Parameters
    ----------
    number_of_specimen: int
        initial number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense
    reproduction_per_prey: float
        The number of predators in each generation per prey
    Attributes
    ----------
    num: int
        number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense (negative for predators)
    reproduction_per_prey: float
        The number of predators in each generation per prey
    """
    def __init__(self, number_of_specimen, growth_rate, reproduction_per_prey):
        super().__init__(number_of_specimen, growth_rate)
        self.reproduction_per_prey = reproduction_per_prey


class Prey(Specious):
    """
    describe the growth and the number of specimen of the prey
    This is the same as Specious but given different name for clarification
    Parameters
    ----------
    number_of_specimen: int
        initial number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense
    Attributes
    ----------
    num: int
        number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense

    """
    def __init__(self,number_of_specimen, growth_rate):
        super().__init__(number_of_specimen, growth_rate)


class Predator_2_prey(Specious):
    """
    describes the growth, the number of predator specimen and the impact in the reproduction from prey
    Parameters
    ----------
    number_of_specimen: int
        initial number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense
    reproduction_per_prey: float
        The number of predators in each generation per prey
    Attributes
    ----------
    num: int
        number of the specimen in the specious
    growth_rate: float
        the growth rate in the exponential sense (negative for predators)
    reproduction_per_prey: float
        The number of predators in each generation per prey
    """
    def __init__(self, number_of_specimen, growth_rate, reproduction_per_prey_1, reproduction_per_prey_2):
        super().__init__(number_of_specimen, growth_rate)
        self.reproduction_per_prey_1 = reproduction_per_prey_1
        self.reproduction_per_prey_2 = reproduction_per_prey_2

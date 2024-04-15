import numpy as np
from scipy.integrate import RK45
from .specious import Prey, Predator, Predator_2_prey


def lotka_volterra_evolution_numerical(prey: Prey, predator: Predator, predator_prey_interaction, time):
    """ 
    numerical solution for lotke voltra for prey and predetor in number of generation
    """

    def population_dt(t, population):
        delta_prey_population_dt = population[0] * prey.growth_rate - predator_prey_interaction * population[0] * \
                                   population[
                                       1]
        delta_predator_population_dt = population[
                                           1] * predator.growth_rate + predator.reproduction_per_prey * predator_prey_interaction * \
                                       population[0] * population[1]
        return np.array([delta_prey_population_dt, delta_predator_population_dt])

    solution = RK45(fun=population_dt, t0=0, y0=[prey.num, predator.num], t_bound=time, rtol=1e-7, atol=1e-9)

    # collect data
    time_values = []
    prey_values = []
    predator_values = []
    for i in range(1000):
        # get solution step state
        solution.step()
        time_values.append(solution.t)
        prey_values.append(solution.y[0])
        predator_values.append(solution.y[1])
        if time_values[-1] == time:
            return time_values, prey_values, predator_values
    return time_values, prey_values, predator_values


def two_preys_lotka_volterra_evolution_numerical(prey_1: Prey, prey_2: Prey,
                                                 predator: Predator_2_prey,
                                                 predator_prey_1_interaction, predator_prey_2_interaction,
                                                 time, solution_steps):
    """
    numerical solution for lotke voltra for prey and predetor in number of generation
    """

    def population_dt(t, population):
        delta_prey_1_population_dt = population[0] * prey_1.growth_rate - \
                                     predator_prey_1_interaction * population[0] * population[2]
        delta_prey_2_population_dt = population[1] * prey_2.growth_rate - \
                                     predator_prey_2_interaction * population[1] * population[2]
        delta_predator_population_dt = population[2] * predator.growth_rate + \
                                       predator.reproduction_per_prey_1 * predator_prey_1_interaction * population[0] * \
                                       population[2] + \
                                       predator.reproduction_per_prey_2 * predator_prey_2_interaction * population[0] * \
                                       population[2]

        return np.array([delta_prey_1_population_dt, delta_prey_2_population_dt, delta_predator_population_dt])

    solution = RK45(fun=population_dt, t0=0, y0=[prey_1.num, prey_2.num, predator.num], t_bound=time, rtol=1e-7,
                    atol=1e-9)

    # collect data
    time_values = []
    prey_1_values = []
    prey_2_values = []
    predator_values = []
    for i in range(solution_steps):
        # get solution step state
        solution.step()
        time_values.append(solution.t)
        prey_1_values.append(solution.y[0])
        prey_2_values.append(solution.y[1])
        predator_values.append(solution.y[2])
        if time_values[-1] == time:
            return time_values, prey_1_values, prey_2_values, predator_values
    return time_values, prey_1_values, prey_2_values, predator_values

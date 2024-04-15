import numpy as np
import pandas as pd
from .specious import Prey, Predator, Predator_2_prey


def lotka_volterra_evolution_mc(prey: Prey, predator: Predator, predator_prey_interaction, maximal_time):
    """
    solution for lotke voltra for prey and predetor in number of generation

    """

    time = 0
    time_record = []
    prey_record = []
    predator_record = []

    while time < maximal_time and prey.num > 0 and predator.num > 0:

        ### time for interaction ###

        mft = prey.num * prey.growth_rate + predator.num * abs(
            predator.growth_rate) + prey.num * predator.num * predator_prey_interaction
        # random time step
        time_step = np.random.exponential(scale=1 / mft, size=1)[0]
        time = time + time_step

        ### cross sections definition ###
        chi_prey_growth = prey.num * prey.growth_rate / mft
        chi_predator_growth = predator.num * abs(predator.growth_rate) / mft
        chi_interaction = prey.num * predator.num * predator_prey_interaction / mft
        #        print(f' pery: {chi_prey_growth}, predator: {chi_predator_growth}, interaction: {chi_interaction}')

        # propagation of growth and decay in one time step
        r = np.random.uniform(size=1)[0]
        if r < chi_prey_growth:
            # prey growth
            prey.num = prey.num + 1
        elif chi_prey_growth <= r < (chi_prey_growth + chi_predator_growth):
            # predator decay
            predator.num = predator.num - 1
        else:
            # interaction
            prey.num = prey.num - 1
            predator.num = predator.num + predator.reproduction_per_prey

        ### record ###
        time_record.append(time)
        prey_record.append(prey.num)
        predator_record.append(predator.num)

    return pd.DataFrame({'time': time_record, 'prey': prey_record, 'predator': predator_record})


def two_preys_lotka_volterra_evolution_mc(prey_1: Prey, prey_2: Prey,
                                          predator: Predator_2_prey,
                                          predator_prey_1_interaction, predator_prey_2_interaction,
                                          maximal_time):
    """
    scotchastic solution for lotke voltra for 2 prey and 1 predetor in number of generation
    the solution method used is monte carlo

    """

    time = 0
    time_1_record = []
    prey_1_record = []
    time_2_record = []
    prey_2_record = []
    time_total_prey_record = []
    total_prey_record = []
    predator_record = []

    while time < maximal_time and (prey_1.num > 0 or prey_2.num > 0) and predator.num > 0:

        ### time for interaction ###
        mft = prey_1.num * prey_1.growth_rate + prey_2.num * prey_2.growth_rate + \
              predator.num * abs(predator.growth_rate) + \
              prey_1.num * predator.num * predator_prey_1_interaction + prey_2.num * predator.num * predator_prey_2_interaction
        # random time step
        time_step = np.random.exponential(scale=1 / mft, size=1)[0]
        time = time + time_step

        ### cross sections definition ###
        chi_prey_1_growth = prey_1.num * prey_1.growth_rate / mft
        chi_prey_2_growth = prey_2.num * prey_2.growth_rate / mft
        chi_predator_growth = predator.num * abs(predator.growth_rate) / mft
        chi_interaction_1 = prey_1.num * predator.num * predator_prey_1_interaction / mft
        chi_interaction_2 = prey_2.num * predator.num * predator_prey_2_interaction / mft

        chi_total_growth = chi_prey_1_growth + chi_prey_2_growth + chi_predator_growth
        # propagation of growth and decay in one time step
        r = np.random.uniform(size=1)[0]

        if r <= chi_prey_1_growth:
            # prey 1 growth
            prey_1.num = prey_1.num + 1# if prey_1.num<300 else prey_1.num
        elif chi_prey_1_growth < r <= (chi_prey_1_growth + chi_prey_2_growth):
            # prey 2 growth
            prey_2.num = prey_2.num + 1# if prey_2.num<300 else prey_2.num
        elif (chi_prey_1_growth + chi_prey_2_growth) < r <= chi_total_growth:
            # predator decay
            predator.num = predator.num - 1
        elif chi_total_growth < r <= (chi_total_growth + chi_interaction_1):
            # interaction 1
            prey_1.num = prey_1.num - 1
            predator.num = predator.num + predator.reproduction_per_prey_1
        else:
            # interaction 2
            prey_2.num = prey_2.num - 1
            predator.num = predator.num + predator.reproduction_per_prey_2

        ### record ###
        if prey_1.num > 0:
            time_1_record.append(time)
            prey_1_record.append(prey_1.num)
        if prey_2.num > 0:
            time_2_record.append(time)
            prey_2_record.append(prey_2.num)
        time_total_prey_record.append(time)
        total_prey_record.append(prey_2.num + prey_1.num)
        predator_record.append(predator.num)

    return pd.DataFrame({'time': time_1_record, 'prey': prey_1_record, 'predator': predator_record[0:len(time_1_record)]}), \
        pd.DataFrame({'time': time_2_record, 'prey': prey_2_record, 'predator': predator_record[0:len(time_2_record)]}), \
        pd.DataFrame({'time': time_total_prey_record,
                      'prey': total_prey_record,
                      'predator': predator_record[0:len(time_total_prey_record)]})

import matplotlib.pyplot as plt

def predator_prey_model(rabbit_growth_rate, rabbit_death_rate, wolf_growth_rate, wolf_death_rate, 
                        initial_rabbit_population, initial_wolf_population, time_period, scenario_title):
    rabbit_population = [initial_rabbit_population]
    wolf_population = [initial_wolf_population]

    for t in range(time_period):
        current_rabbit_population = rabbit_population[-1]
        current_wolf_population = wolf_population[-1]
        
        rabbit_population_new = current_rabbit_population + \
                                (current_rabbit_population * rabbit_growth_rate) - \
                                (current_rabbit_population * rabbit_death_rate * current_wolf_population)
        wolf_population_new = current_wolf_population + \
                              (current_wolf_population * wolf_growth_rate * current_rabbit_population) - \
                              (current_wolf_population * wolf_death_rate)
        
        rabbit_population.append(rabbit_population_new)
        wolf_population.append(wolf_population_new)

    plt.figure(figsize=(10, 6))
    plt.plot(rabbit_population, label="Rabbits")
    plt.plot(wolf_population, label="Wolves")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title(scenario_title)
    plt.legend()
    plt.grid(True)
    plt.show()

predator_prey_model(rabbit_growth_rate=0.05, rabbit_death_rate=0.005,
                    wolf_growth_rate=0.003, wolf_death_rate=0.07,
                    initial_rabbit_population=40, initial_wolf_population=40,
                    time_period=200, scenario_title="Rabbit and Wolf Population Stability Over Time")

predator_prey_model(rabbit_growth_rate=0.02, rabbit_death_rate=0.005,
                    wolf_growth_rate=0.003, wolf_death_rate=0.07,
                    initial_rabbit_population=40, initial_wolf_population=40,
                    time_period=200, scenario_title="Decreased Rabbit Growth Rate")

predator_prey_model(rabbit_growth_rate=0.05, rabbit_death_rate=0.005,
                    wolf_growth_rate=0.003, wolf_death_rate=0.1,
                    initial_rabbit_population=40, initial_wolf_population=40,
                    time_period=200, scenario_title="Increased Wolf Death Rate")

predator_prey_model(rabbit_growth_rate=0.05, rabbit_death_rate=0.002,
                    wolf_growth_rate=0.003, wolf_death_rate=0.07,
                    initial_rabbit_population=40, initial_wolf_population=40,
                    time_period=200, scenario_title="Reduced Wolf Predation")
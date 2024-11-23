import matplotlib.pyplot as plt

rabbit_growth_rate = 0.1
rabbit_death_rate = 0.01
wolf_growth_rate = 0.005
wolf_death_rate = 0.1
time_period = 200

rabbit_population = [40]
wolf_population = [15]

for t in range(time_period):
    current_rabbit_population = rabbit_population[-1]
    current_wolf_population = wolf_population[-1]
    
    next_rabbit_population = current_rabbit_population + (current_rabbit_population * rabbit_growth_rate) - (current_rabbit_population * rabbit_death_rate * current_wolf_population)
    next_wolf_population = current_wolf_population + (current_wolf_population * wolf_growth_rate * current_rabbit_population) - (current_wolf_population * wolf_death_rate)
    
    rabbit_population.append(next_rabbit_population)
    wolf_population.append(next_wolf_population)

plt.figure(figsize=(10, 6))
plt.plot(rabbit_population, label="Rabbits")
plt.plot(wolf_population, label="Wolves")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Rabbit and Wolf Population Over Time")
plt.legend()
plt.grid(True)
plt.show()
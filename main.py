import random
import math
import numpy as np


def sphere_function(x):
    """Function for sphere"""
    return sum(xi ** 2 for xi in x)



def get_neighbors(current, step_size=0.1):
    x, y = current
    return [
        (x + step_size, y),
        (x - step_size, y),
        (x, y + step_size),
        (x, y - step_size)
    ]
# def hill_climbing(starting_point, max_iterations, step_size=0.1):

# epsilon=1e-6

def hill_climbing(func: callable, bounds, iterations=1000, epsilon=0.2):
    """Hill Climbing algorithm"""
    # current_point = bounds
    b1, b2 = bounds
    for i in np.arange(b1[0], b1[1], epsilon):
        for j in np.arange(b2[0], b2[1], epsilon):
            current_point = [i, j]
            current_value = func(current_point)

            for _ in range(iterations):
                neighbors = get_neighbors(current_point, epsilon)

                # Пошук найкращого сусіда
                next_point = None
                next_value = -np.inf

                for neighbor in neighbors:
                    value = func([*neighbor])
                    if value < next_value:
                        next_point = neighbor
                        next_value = value

            # Якщо не вдається знайти кращого сусіда — зупиняємось
            if next_value >= current_value:
                break

            # Переходимо до кращого сусіда
            current_point, current_value = next_point, next_value

    return [*current_point], current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    """Random Local Search algorithm"""


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    """Simulated Annealing algorithm"""





def main():
    """Main function"""
    bounds = [(-5, 5), (-5, 5)]
    print(sphere_function([-5, -5]))
    # Виконання алгоритмів
    # cur_x, cur_y = bounds
    # b1, b2 = bounds
    # # print(b1, b2)
    # for i in range(int(b1[0]), b1[1], 1):
    #     for j in range(b2[0], b2[1], 1):
    #         print(i, j)
    # print("x", cur_x, "y", cur_y)
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    # print("\nRandom Local Search:")
    # rls_solution, rls_value = random_local_search(sphere_function, bounds)
    # print("Розв'язок:", rls_solution, "Значення:", rls_value)

    # print("\nSimulated Annealing:")
    # sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    # print("Розв'язок:", sa_solution, "Значення:", sa_value)


if __name__ == "__main__":
    main()

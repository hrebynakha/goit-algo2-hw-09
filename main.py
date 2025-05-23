import numpy as np
import random
from graphs import plot_hill_climbing_path

def sphere_function(x):
    """Function for sphere"""
    return sum(xi ** 2 for xi in x)


def get_neighbors(current, bounds, step_size=0.1):
    x, y = current
    new_neighbors = np.array([
        (x + step_size, y),           # right
        (x - step_size, y),           # left
        (x, y + step_size),           # up
        (x, y - step_size),           # down
        (x + step_size, y + step_size),   # right-up
        (x + step_size, y - step_size),   # right-down
        (x - step_size, y + step_size),   # left-up
        (x - step_size, y - step_size),   # left-down
    ])

    lower_bounds = np.array([b[0] for b in bounds])
    upper_bounds = np.array([b[1] for b in bounds])
    clipped_neighbors = np.clip(new_neighbors, lower_bounds, upper_bounds)

    return clipped_neighbors


def hill_climbing(func: callable, bounds, iterations=1000, epsilon=1e-6):
    """Hill Climbing algorithm"""
    x_start = np.array([np.random.uniform(low, high) for (low, high) in bounds])
    current_point = x_start
    current_value = func(current_point)
    history = [current_point.copy()] 
    for i in range(iterations):
        next_point, next_value, neighbors  = None, np.inf, get_neighbors(current_point, bounds)
        for neighbor in neighbors:
            value = func(neighbor)
            if value < next_value:
                next_point, next_value = neighbor, value


        if abs(next_value - current_value) < epsilon:
            break
    
        if next_value > current_value:
            # found local minimum
            break
        
        history.append(current_point.copy())

        current_point, current_value = next_point, next_value

    return current_point, current_value, history


def get_random_neighbor(current, bounds,step_size=0.1):
    x, y = current
    new_neighbors = np.array(
        (x + random.uniform(-step_size, step_size), y + random.uniform(-step_size, step_size))
    )

    lower_bounds = np.array([b[0] for b in bounds])
    upper_bounds = np.array([b[1] for b in bounds])
    clipped_neighbors = np.clip(new_neighbors, lower_bounds, upper_bounds)

    return clipped_neighbors

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    """Random Local Search algorithm"""

    # current_point = starting_point
    # current_value = objective_function(*current_point)
    x_start = np.array([np.random.uniform(low, high) for (low, high) in bounds])
    print("X start", x_start)
    current_point = x_start
    current_value = func(current_point)
    history = [current_point.copy()] 

    for _ in range(iterations):
        new_point = get_random_neighbor(current_point, bounds)
        new_value = func(new_point)
        if new_value < current_value:
            current_point, current_value = new_point, new_value
            history.append(current_point.copy())
        
        if abs(new_value - current_value) < epsilon:
            print("Current value", current_value)
            print("New value", new_value)
            print("Break")
            # break
        

    return current_point, current_value, history


# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    """Simulated Annealing algorithm"""





def main():
    """Main function"""
    bounds = [(-5, 5), (-5, 5)]
    print(sphere_function([-5, -5]))
    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value, hc_history = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value, rls_history = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    # print("\nSimulated Annealing:")
    # sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    # print("Розв'язок:", sa_solution, "Значення:", sa_value)
     
    print("\nHill Climbing Visualization:")
    plot_hill_climbing_path(sphere_function, bounds, hc_history, rls_history)

if __name__ == "__main__":
    main()

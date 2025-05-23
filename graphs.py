import numpy as np
import matplotlib.pyplot as plt

def plot_hill_climbing_path(func, bounds, history_hc, history_rls):
    x = np.linspace(bounds[0][0], bounds[0][1], 100)
    y = np.linspace(bounds[1][0], bounds[1][1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func([X, Y])

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label='f(x, y)')

    history_hc = np.array(history_hc)
    history_rls = np.array(history_rls)
    plt.plot(history_hc[:, 0], history_hc[:, 1], color='red', marker='o', markersize=3, linewidth=1.5)
    plt.scatter(history_hc[0, 0], history_hc[0, 1], color='white', label='Start', edgecolors='black')
    plt.scatter(history_hc[-1, 0], history_hc[-1, 1], color='black', label='End')

    plt.plot(history_rls[:, 0], history_rls[:, 1], color='blue', marker='>', markersize=3, linewidth=1.5)
    plt.scatter(history_rls[0, 0], history_rls[0, 1], color='white',edgecolors='black')
    plt.scatter(history_rls[-1, 0], history_rls[-1, 1], color='black')

    plt.title('Hill Climbing Path and Random Local Search Path')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
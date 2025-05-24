"""Graphs module"""

import numpy as np
import matplotlib.pyplot as plt


def show_path(func: callable, bounds, history_hc, history_rls, history_sa):
    """Plot path of Hill Climbing, Random Local Search and Simulated Annealing"""
    x = np.linspace(bounds[0][0], bounds[0][1], 100)
    y = np.linspace(bounds[1][0], bounds[1][1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func([X, Y])

    plt.contourf(X, Y, Z, levels=50, cmap="viridis")
    plt.colorbar(label="f(x, y)")

    def add_history_to_plot(history, color, marker, label):
        history = np.array(history)
        plt.plot(
            history[:, 0],
            history[:, 1],
            color=color,
            marker=marker,
            markersize=3,
            linewidth=1.5,
            label=label,
        )
        plt.scatter(
            history[0, 0],
            history[0, 1],
            edgecolors="black",
        )
        plt.scatter(history[0, 0], history[0, 1], color="white", edgecolors="black")
        plt.scatter(history[-1, 0], history[-1, 1], color="black")
        return history

    history_hc = add_history_to_plot(history_hc, "red", "o", "Hill Climbing")
    history_rls = add_history_to_plot(history_rls, "blue", ">", "Random Local Search")
    history_sa = add_history_to_plot(history_sa, "green", "^", "Simulated Annealing")

    plt.title(
        "Hill Climbing Path and Random Local Search Path and Simulated Annealing Path"
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

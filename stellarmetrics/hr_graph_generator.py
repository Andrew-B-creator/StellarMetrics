import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def generate_hr_graph(data, catalog_type):
    plt.figure(figsize=(10,6))
    plt.scatter(data["temperature"], data["luminosity"], s = 2, alpha = 0.9)
    plt.yscale("log")
    plt.gca().invert_xaxis()
    plt.grid(True)
    plt.xlabel("Effective Temperature (K)")
    plt.ylabel("Luminosity")
    title = f"{catalog_type.capitalize()} Hertzsprung-Russell Diagram"
    plt.title(title)

    filename = f"{catalog_type.lower()}_hr_diagram.png"
    plt.savefig(filename)
    plt.close()

    print(f"Hertzsprung-Russell diagram saved as {filename}")
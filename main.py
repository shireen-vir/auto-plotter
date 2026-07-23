class AutoPlotter:
    """
    A simple data science tool for automatically generating plots.
    
    Attributes:
        data (list): The input data to be plotted.
        
    Methods:
        plot_data: Generates a plot based on the input data.
    """

    def __init__(self, data):
        self.data = data

    def plot_data(self):
        import matplotlib.pyplot as plt
        plt.plot(self.data)
        plt.show()


def main():
    import random
    data = [random.randint(1, 100) for _ in range(10)]
    plotter = AutoPlotter(data)
    print("Auto-Plotter Tool")
    print("--------------------")
    print("Generating plot for the following data: ")
    print(plotter.data)
    plotter.plot_data()


if __name__ == "__main__":
    main()
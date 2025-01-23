def plot_data(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title('Data Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

def create_histogram(data, bins=10):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, alpha=0.7, color='blue')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def generate_scatter_plot(x, y):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, color='red')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()
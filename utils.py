import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    """
    Main function for the auto-plotter data science tool.

    This tool automatically generates a variety of plots for a given dataset.
    """
    # Load sample dataset
    data = pd.read_csv('sample_data.csv')

    # Display first few rows of the dataset
    print("Dataset Preview:")
    print(data.head())

    # Generate histograms for numerical columns
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    for column in numerical_columns:
        plt.figure(figsize=(10,6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.show()

    # Generate scatter plots for pairs of numerical columns
    for i in range(len(numerical_columns)):
        for j in range(i+1, len(numerical_columns)):
            column1 = numerical_columns[i]
            column2 = numerical_columns[j]
            plt.figure(figsize=(10,6))
            sns.scatterplot(x=data[column1], y=data[column2])
            plt.title(f'Scatter Plot of {column1} vs {column2}')
            plt.show()

if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate donut dataset
def generate_donut_dataset(num_samples, radius_inner, radius_outer, noise_std=0.05):
    # np.random.seed(42) # Seed for reproducibility

    # Generate random angles between 0 and 2π
    theta = np.random.uniform(0, 2*np.pi, num_samples)

    # Generate points for inner circle
    x_inner = radius_inner * np.cos(theta)
    y_inner = radius_inner * np.sin(theta)

    # Generate points for outer circle
    x_outer = radius_outer * np.cos(theta)
    y_outer = radius_outer * np.sin(theta)

    # Combine inner and outer circles with noise
    x = np.concatenate([x_inner, x_outer]) + np.random.normal(0, noise_std, 2*num_samples)
    y = np.concatenate([y_inner, y_outer]) + np.random.normal(0, noise_std, 2*num_samples)

    # Create DataFrame with quadratic features
    df = pd.DataFrame({'x': x, 'y': y, 'x^2': x**2, 'y^2': y**2, 'xy': x*y, 'label': np.concatenate([np.zeros(num_samples), np.ones(num_samples)])})

    return df

# Generate donut dataset with 500 samples, inner radius=2, outer radius=5
donut_df = generate_donut_dataset(500, 2, 5)

# Plot the donut dataset
plt.scatter(donut_df['x'], donut_df['y'], c=donut_df['label'], cmap='viridis', edgecolors='k', marker='o', alpha=0.7)
plt.title('Donut Dataset with Quadratic Features')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Save the dataset to CSV without header row nor index column
donut_df.to_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\donut_dataset.csv', header=False, index=False)

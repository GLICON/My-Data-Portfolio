import pandas as pd

# Load the dataset
df = pd.read_csv('WineQT.csv')

# Define the quality categories
high_quality = df[df['quality'] >= 7]
standard_quality = df[(df['quality'] >= 5) & (df['quality'] <= 6)]

# Key chemical features
features = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

# Compute means for high-quality wines
high_means = high_quality[features].mean().round(2)

# Compute means for standard wines
standard_means = standard_quality[features].mean().round(2)

# Create a comparison DataFrame
comparison = pd.DataFrame({
    'High-Quality Mean (>=7)': high_means,
    'Standard Mean (5-6)': standard_means
})

# Add sample sizes
print(f"High-Quality samples: {len(high_quality)}")
print(f"Standard samples: {len(standard_quality)}")
print("\nChemical Profiles Comparison:")
print(comparison)

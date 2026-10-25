# Weighted Mean Calculator
Lx=[1, 2, 3, 4, 5]  # x
Lf=[0.1, 0.2, 0.3, 0.2, 0.2]  # f

# Calculate the weighted mean
weighted_mean = sum(x * f for x, f in zip(Lx, Lf)) / sum(Lf)
print("Weighted Mean:", weighted_mean)
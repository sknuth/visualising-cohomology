import matplotlib.pyplot as plt

# Define cohomology groups for CP^2
cohomology_groups = ["H⁰ ≅ ℤ", "H¹ ≅ 0", "H² ≅ ℤ", "H³ ≅ 0", "H⁴ ≅ ℤ", "Hⁿ ≅ 0 (n ≥ 5)"]

# Create a diagram to represent the cohomology groups
plt.figure(figsize=(10, 4))  
plt.bar(cohomology_groups, [1, 0, 1, 0, 1, 0])  # Bar heights representing dimensions
plt.title("Cohomology Groups of CP² (Complex Projective Space)")
plt.xlabel("Cohomology Group")
plt.ylabel("Dimension") 
plt.show()
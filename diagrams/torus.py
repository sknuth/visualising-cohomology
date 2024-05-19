import matplotlib.pyplot as plt

# Define cohomology groups
cohomology_groups = ["H⁰ ≅ ℤ", "H¹ ≅ ℤ²", "H² ≅ ℤ", "Hⁿ ≅ 0 (n ≥ 3)"]

# Create a simple diagram
plt.figure(figsize=(8, 4))  
plt.bar(cohomology_groups, [1, 2, 1, 0]) # Bar heights representing dimensions
plt.title("Cohomology Groups of the Torus (T²)")
plt.xlabel("Cohomology Group")
plt.ylabel("Dimension") 
plt.show()

import matplotlib.pyplot as plt

# Define cohomology groups (replace with actual group structure if needed)
cohomology_groups = ["H⁰ ≅ ℤ", "H¹ ≅ 0", "H² ≅ ℤ", "Hⁿ ≅ 0 (n ≥ 3)"]

# Create a simple diagram
plt.figure(figsize=(8, 4))  # Adjust figure size as needed
plt.bar(cohomology_groups, [1, 0, 1, 0])  # Bar heights representing group structure
plt.title("Cohomology Groups of the Sphere (S²)")
plt.xlabel("Cohomology Group")
plt.ylabel("Dimension")  # Or use a more appropriate label if needed
plt.show()

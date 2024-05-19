import matplotlib.pyplot as plt

# Define cohomology groups (with simplified representation)
cohomology_groups = ["H⁰ ≅ ℤ", "H¹ ≅ ℤ⊕ℤ/2ℤ", "H² ≅ 0", "Hⁿ ≅ 0 (n ≥ 3)"]

# Create a simple diagram
plt.figure(figsize=(8, 4)) 
plt.bar(cohomology_groups, [1, 2, 0, 0])  # Bar heights (simplified representation)
plt.title("Cohomology Groups of the Klein Bottle")
plt.xlabel("Cohomology Group")
plt.ylabel("Dimension") 
plt.show()

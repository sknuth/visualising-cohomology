import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph to represent the ring structure
G = nx.DiGraph()

# Add nodes for generators
G.add_node("σ₁₁")
G.add_node("σ₂")

# Add edges for multiplication (simplified)
G.add_edge("σ₁₁", "σ₂", label="* σ₁₁")  # σ₁₁ * σ₁₁ = σ₂
# No edge from σ₂ to anything since σ₂ * σ₁₁ = σ₂ * σ₂ = 0

# Define positions for nodes for visual clarity
pos = {"σ₁₁": (0, 0), "σ₂": (1, 0)}

# Draw the graph with labels
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Simplified Representation of H*(Gr(2,4); ℤ)")
plt.show()
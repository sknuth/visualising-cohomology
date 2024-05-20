# visualising-cohomology

This repository provides visualizations and diagrams to illustrate the concept of cohomology in algebraic topology. We explore the cohomology of various spaces, including:

- **Lower Dimensions:** The sphere (S²), the torus (T²), and the Klein bottle.
- **Higher Dimensions:** Complex projective spaces (CPⁿ), starting with CP².

## Introduction

Cohomology is a powerful tool in algebraic topology that assigns algebraic invariants (groups) to topological spaces. These groups, called cohomology groups, capture information about the "holes" and other topological features of the space. 

This repository aims to provide a more intuitive understanding of cohomology through visualizations and diagrams.

## Prerequisites

To fully grasp the concepts presented here, some familiarity with the following topics is helpful:

* **Basic Topology:** Concepts like topological spaces, continuous maps, and homeomorphisms.
* **Group Theory:**  Basic understanding of groups, homomorphisms, and isomorphisms.

## Spectral Sequences (higher-dimensions/serre_spectral_sequence.py)

The `serre_spectral_sequence.py` script provides a highly simplified visualization of the Serre spectral sequence for the Hopf fibration, a way of breaking down the 2-sphere (S²) using a fibration with base space CP¹ and fibers S¹. The code uses dictionaries to represent the grid-like pages of the spectral sequence and symbolically simulates the differentials that refine the calculations on each page. Keep in mind that this is a conceptual illustration and does not capture the full complexity of spectral sequence computations, which involve intricate algebra and analysis of differentials. 

## Grassmannians and Schubert Calculus (higher-dimensions/gr24.py)

The `gr24.py` script explores the cohomology ring of the Grassmannian Gr(2,4), the space of 2-dimensional planes in 4-dimensional space. The script uses the `networkx` library to create a simplified visualization of the ring structure, highlighting some key generators and their multiplication relations, which are determined by the intersection of Schubert cells. This visualization is a simplified representation, as the full cohomology ring is more complex and requires a deeper dive into Schubert calculus for complete understanding.

## Repository Structure

* **visualizations/:**  Contains Python scripts for generating 3D visualizations of the sphere, torus, and Klein bottle.
* **diagrams/:** Contains Python scripts for creating diagrams that represent the cohomology groups of each space.
* **higher-dimensions/:**  Contains scripts related to the cohomology of higher-dimensional spaces.
* **requirements.txt:** Lists the Python libraries required to run the scripts.

## Instructions

1. **Clone the repository:** `git clone https://github.com/your-username/cohomology-examples.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the Python scripts:** Navigate to the respective directory (`visualizations/`, `diagrams/`, or `higher-dimensions/`) and run the scripts using `python script_name.py`.

## Explanation of Visualizations and Diagrams

**Visualizations:**
- The visualizations provide a 3D representation of the sphere, torus, and Klein bottle, helping to understand their shapes and spatial properties.

**Diagrams:**
- The diagrams represent the cohomology groups of each space.  
- They highlight the structure of these groups and how they differ between the spaces, reflecting the topological differences. 

**Higher-Dimensional Examples:**
- Visualizing spaces directly in higher dimensions is challenging. The `higher-dimensions/` directory uses diagrams to represent the cohomology groups of examples like complex projective spaces.

## Contributing

Feel free to contribute to this repository by adding more examples, improving visualizations, or expanding the explanations. 
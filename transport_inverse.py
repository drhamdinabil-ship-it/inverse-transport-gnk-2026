"""transport_inverse.py

Reproducible implementation of the regularized Gauss-Newton-Kantorovich
algorithm for the 1D-1V inverse transport problem.

This file accompanies the paper:
    Hamdi, N. A Regularized Gauss-Newton-Kantorovich Algorithm for
    Inverse Transport Problems with Digital Twin Applications. 2026.

The full source code is in the accompanying Colab notebook.
Run the notebook cells to regenerate all results (table1.json,
statistical.json, discretization.json, adjoint.json, figure1.png).

Requirements: Python >= 3.9, numpy, matplotlib
"""

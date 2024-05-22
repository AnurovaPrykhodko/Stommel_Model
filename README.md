# Stommel Model (bachelor thesis project):

Two-box model of ocean basins

Program to solve non-homogeneous ordinary differential equations with the Runge-Kutta 5(4) method. The variables are salinity difference, freshwater supply and time.
Functions to plot variables such as salinity difference, flow strength and freshwater supply as time.

Implements scipy, numpy, and matplotlib.

## List of content:
**figures** 
figures from plotting

**stommel_model**

- __init__.py: Stommel model 

- main.py: Runs Stommel model for each case and plots solutions of the salinity difference, flow and freshwater supply. 

- R_functions.py: functions for the freshwater supply

- Plotting.py: functions to plot solutions and combine the plots

- regime.py: plotting regimes of solutions to differential equation

- solving_ODE.py: functions to convert between dimensional and non-dimensional parameters, and function for solving the differential equation.

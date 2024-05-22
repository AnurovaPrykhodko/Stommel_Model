import matplotlib.pyplot as plt
import numpy as np

"""
Plots derivative of salinity difference as a function of salinity difference, for R=0 and R=1/8.
Marks zero crossings for R=1/8.
Shows different regimes of flow and steady state solutions.
"""

def func(deltaS, R):
    return -deltaS * abs(1 - deltaS) + R

#Interval of salinity difference to plot
deltaS = np.linspace(0, 1.25, 1000)

#Find zero crossings for R = 1/8
zero_crossings = np.where(np.diff(np.sign(func(deltaS, 1/8))) != 0)[0]

# Plotting
plt.style.use("ggplot")
plt.rcParams['xtick.color'] = 'dimgray'
plt.rcParams['ytick.color'] = 'dimgray'
plt.rcParams['axes.labelcolor'] = 'black'
plt.plot(deltaS, func(deltaS, 0), label="R = 0")
plt.plot(deltaS, func(deltaS, 1/8), label="R = 1/8", color="tab:blue")
plt.scatter(deltaS[zero_crossings], func(deltaS, 1/8)[zero_crossings], marker='o',
            label='Zero Crossings (A,B,C)', color="tab:blue")

# Annotate zero crossings
annotations = ['A', 'B', 'C']
for i, idx in enumerate(zero_crossings):
    plt.text(deltaS[idx]- 0.03, func(deltaS, 1/8)[idx], annotations[i], fontsize=12,
             color='black', ha='right', va='bottom')

plt.axhline(0, color='black', linewidth=0.8, linestyle="--", label="dΔS*/dt* = 0")
plt.legend(edgecolor='dimgray', loc='best',  bbox_to_anchor=(0.4, 0.7))
plt.xlabel("Non-dimensional salinity difference ΔS*")
plt.ylabel("Non-dimensional derivative dΔS*/dt*")
plt.show()

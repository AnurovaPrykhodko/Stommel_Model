import matplotlib.pyplot as plt

# Functions for plotting

def plot_parameters(parameters):
    """Given parameters (dictionary), plot legend box with parameters."""
    text = 'Parameters:\n\n'             #create text of parameters
    for parameter, value in parameters.items():
        if parameter == 'R_function':
            text += f'R_function: {value[0]}' + '\n'
        elif parameter == 'Noise':
            if value[0]:
                text += f'Noise: Yes' + '\n'
            elif not value[0]:
                text += f'Noise: No' + '\n'
        else:
            text += f'{parameter}: {value[0]} {value[1]}' + '\n'

    props = dict(boxstyle='round', facecolor='whitesmoke', edgecolor='black', linewidth=0.7)
    ax = plt.gca()
    ax.text(1.06, 0.99, text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)
    plt.subplots_adjust(right=0.67)

def plot_t_variable(t, variable, labelstart='labelstart', labelend='labelend', xlabel='xlabel', ylabel='ylabel'):
    """Plots variable as a function of time."""
    plt.plot(t, variable, label = labelstart + labelend)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def plot_M_t(solved, labelstart='M(t)'):
    """Plots M = |1- deltaS_nd| as a function of time."""
    plt.plot(solved.t, abs(1 - solved.y[0]), label = labelstart)
    plt.xlabel("Time t* (non-dimensional)")
    plt.ylabel("Flow M* or Freshwater Supply R (non-dimensional)")
    plt.legend()


def plot_R_t(solved, R_function, R_const, *args):
    """Plots R as a function of time. Note that noise is not included."""
    plt.plot(solved.t, R_function(solved.t, R_const, *args), label=f'R(t)')
    plt.legend()
    plt.xlabel("Time (non-dim)")
    plt.ylabel("R (non-dim)")

def combine(*plots, parameters, threshold = False, thresholdvalues = [], thresholdlabel='tresholdlabel'):
    """Takes in saved plots, initial parameters and thresholds for solutions.
    Combines plots into one, together with a box of their parameters and marked thresholds. """

    fig, ax = plt.subplots()

    # Plot each axis object stored in the list onto the single figure
    for axis in plots:
        lines = axis[0].get_lines()  # Get the lines from each axis
        for line in lines:
            line_data = line.get_data()  # Get the x and y data from the line
            ax.plot(line_data[0], line_data[1], label=line.get_label())  # Plot the data directly onto the new axis
    ax.set_xlabel(plots[0][0].get_xlabel())
    ax.set_ylabel(plots[0][0].get_ylabel())
    ax.set_title(plots[0][0].get_title())
    plot_parameters(parameters)

    if threshold:
        i = 1
        for value in thresholdvalues:
            if i == 1:
                ax.axhline(value, linestyle='--', color = 'grey', label=thresholdlabel)
                i += 1
            else:
                ax.axhline(value, linestyle='--', color='grey')

    ax.legend(edgecolor='dimgray')
    plt.show()
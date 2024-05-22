import solving_ODE
import plotting
import R_functions
import matplotlib.pyplot as plt

def run(*args, R_function, t=10*365*24*3600, n_tstep=1000, deltaS_start=0,
        S_A=35*10**(-3), Beta=0.8*10**3, Kappa=10**7, deltarho_t=1.1, F_0=0.1*10**6, V=10**15,
        noise=False, std=0, std_label='0', function_type='function type'):
    """
    From given parameters, initial condition and function for the freshwater supply, runs model.
    Returns saved plots and their parameters.
    Variables in SI-units.
    ----------------------------------

    Arguments:

    args: argument(s) for R_function
    R_function: function for freshwater supply
    t: total time (seconds)
    n_tstep: number of time steps
    deltaS_start: initial salinity difference
    S_A: salinity in warmer box
    Beta: haline expansion coefficient
    Kappa: proportionality constant
    deltarho_t: thermal density difference
    F_0: initial freshwater supply
    V: volume of each box
    noise: add noise as normal distribution (boolean)
    std: standard deviation for added noise
    std_label: Label for standard deviation (e.g. as number*R)
    function_type: write the type of function for plotting
    """

    #calculating non-dimensional constants
    R_const, deltaS_start_nd, t_nd = solving_ODE.get_nondim(S_A, Beta, Kappa, deltarho_t, F_0, deltaS_start, t, V)

    #solving ODE
    solved = solving_ODE.ODE_solver(t_nd, n_tstep, deltaS_start_nd, R_const, R_function, noise, std,*args)
    solved_dim = solving_ODE.get_dim(solved, Beta, Kappa, deltarho_t, V)

    #plotting
    parameters = {'S_A':(S_A*10**3,'‰'), 'Beta':(Beta*10**-3,'kgm⁻³/‰'), 'Kappa':(Kappa/10**7,'10⁷ kg/s'),
                  'deltarho_t':(deltarho_t,'kgm⁻³'), 'F_0':(F_0/10**6,'Sv'), 'deltaS_start':(deltaS_start*10**3,'‰'),
                  'R_const':(format(R_const, '.3f'),' '), 'R_function':(function_type,None), 'Noise':(noise,None)}

    plots_deltaS_t = []
    plots_M_t = []
    plots_deltaS_dim_t = []
    plots_M_dim_t = []
    plots_R_t = []

    plt.style.use("ggplot")
    plt.rcParams['xtick.color'] = 'dimgray'
    plt.rcParams['ytick.color'] = 'dimgray'
    plt.rcParams['axes.labelcolor'] = 'black'

    #Plot R(t)
    fig0, ax0 = plt.subplots()
    plotting.plot_R_t(solved, R_function, R_const, *args)
    plots_R_t.append(ax0)

    #Plot delta_S(T)
    fig1, ax1 = plt.subplots()
    plotting.plot_t_variable(solved.t, solved.y[0], xlabel='Time t* (Non-Dimensional)', ylabel='Salinity Difference ΔS* (Non-Dimensional)')
    plots_deltaS_t.append(ax1)

    #Plot M_*(t)
    fig2, ax2 = plt.subplots()
    plotting.plot_M_t(solved, labelstart='M*(t)')
    plots_M_t.append(ax2)

    #Plot delta_S_dim(t)
    fig3, ax3 = plt.subplots()
    plotting.plot_t_variable(solved_dim[0], solved_dim[1], labelstart='ΔS(t), σ = ', labelend=std_label, xlabel='Time t (Years)',
                             ylabel='Salinity Difference ΔS (‰)')
    plots_deltaS_dim_t.append(ax3)

    # Plot M(t)
    fig4, ax4 = plt.subplots()
    plotting.plot_t_variable(solved_dim[0], solved_dim[2], labelstart='M(t), σ = ', labelend=std_label, xlabel='Time t (Years)',
                             ylabel='Flow M (Sv)')
    plots_M_dim_t.append(ax4)

    plt.close('all')   # Close plots to release resources

    plots = [plots_deltaS_t, plots_M_t, plots_R_t, plots_deltaS_dim_t, plots_M_dim_t]

    return plots, parameters

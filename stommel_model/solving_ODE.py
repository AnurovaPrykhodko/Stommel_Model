import numpy as np
from scipy.integrate import solve_ivp

# Functions for solving ODE
def get_nondim(S_A, Beta, Kappa, deltarho_t, F_0, deltaS_start, t, V):
    """
    From parameters, return non-dimensional constants.
    R_const: Freshwater supply
    deltaS_start_nd: non-dimensional initial salinity difference
    t_nd: non-dimensional timescale
    """
    R_const = (S_A*Beta*F_0)/(Kappa*deltarho_t**2)
    deltaS_start_nd = Beta*deltaS_start/deltarho_t
    t_nd=t*Kappa*deltarho_t/V
    return R_const, deltaS_start_nd, t_nd

def get_dim(solved, Beta, Kappa, deltarho_t, V):
    """Takin in solution solved, returns list solved_dim with variables as dimensional."""

    #content in solved_dim = [t, delta_S, M]
    #units in solved_dim = [years, g/kg, Sv]
    solved_dim = [solved.t * V/(Kappa*deltarho_t*365*24*3600), solved.y[0]*deltarho_t/Beta*10**3,
                  Kappa * deltarho_t * abs(1 - solved.y[0]) /10**6]
    return solved_dim

def ODE_solver(t_nd, n_tstep, deltaS_start_nd, R_const, R_function, noise, std, *args):
    """
    Solve ODE on non-dimensional form
    d(deltaS_nd)/dt = -deltaS_nd * |1 - deltaS_nd| + R_function,
    where R_function is a function of time.
    Runge-Kutta method of order 5(4).
    """

    t_points = np.linspace(0, t_nd, n_tstep)

    if not noise:
        def RHS(t, deltaS_nd, R_function, R_const, *args):
            """Right hand side of ODE."""
            return -deltaS_nd * abs(1 - deltaS_nd) + R_function(t, R_const, *args)
    else:
        def RHS(t, deltaS_nd, R_function, R_const, *args):
            """Right hand side of ODE, with noise."""
            random_noise = np.random.normal(scale=std)
            return -deltaS_nd * abs(1 - deltaS_nd) + R_function(t, R_const, *args) + random_noise

    solved = solve_ivp(RHS, (0, t_nd), np.array([deltaS_start_nd]),  t_eval=t_points,
                       args=(R_function, R_const, *args))

    return solved
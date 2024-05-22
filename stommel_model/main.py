import stommel_model
import R_functions as Rfunc
import plotting

"""
Runs Stommel model for each case, that is, solves differential equation from given parameters
and each case of function for the right hand side. Program returns list of saved plots and used 
parameters, which are then combined into desired plots.

Content of saved plots : plots = [plots_deltaS_t, plots_M_t, plots_R_t, plots_deltaS_dim_t, plots_M_dim_t]
"""

"Constant freshwater supple with and without added noise."
#Function R_linear = R_const + 0*t
#without noise
plots_const_1, parameters = stommel_model.run(0, R_function=Rfunc.R_linear, noise=False, t=60*365*24*3600, n_tstep=1000)

#with noise
plots_const_2, parameters = stommel_model.run(0, R_function=Rfunc.R_linear, noise=True, t=60*365*24*3600, n_tstep=1000,
                                              std=0.05 * 0.23140495867768596, std_label='0.05*R')
plots_const_3, parameters = stommel_model.run(0, R_function=Rfunc.R_linear, noise=True, t=60*365*24*3600, n_tstep=1000,
                                              function_type='Constant', std= 0.5 * 0.23140495867768596, std_label='0.5*R')

#plot delta_S_dim(t)
plotting.combine(plots_const_1[3], plots_const_2[3], plots_const_3[3], parameters=parameters, threshold=True,
                 thresholdvalues=[0.5], thresholdlabel='Thermally driven steady state')

#plot M_dim(t)
plotting.combine(plots_const_1[4], plots_const_2[4], plots_const_3[4], parameters=parameters, threshold=True,
                 thresholdvalues=[7], thresholdlabel='Thermally driven steady state')

"At first constant freshwater supply, then a sudden increase during a certain time. With and without added noise."
#Function: for  t < 10.40688 and t > 11.447568  R_sudden = R_const
#          for  10.40688 < t < 11.447568        R_sudden = 0.6 Sv

#without noise
plots_sudden_1, parameters = stommel_model.run(0.6, 10.40688, 11.447568, R_function=Rfunc.R_sudden, noise=False,
                                               t=60*365*24*3600, n_tstep=500)

#with noise
plots_sudden_2, parameters = stommel_model.run(0.6, 10.40688, 11.447568, R_function=Rfunc.R_sudden, noise=True, t=60*365*24*3600,
                                               n_tstep=500, std=0.05 * 0.23140495867768596, std_label='0.05*R_const')
plots_sudden_3, parameters = stommel_model.run(0.6, 10.40688, 11.447568, R_function=Rfunc.R_sudden, noise=True, t=60*365*24*3600,
                                               n_tstep=500, std=0.5 * 0.23140495867768596, std_label='0.5*R_const', function_type='Sudden')

#plot

#plot delta_S_dim(t)
plotting.combine(plots_sudden_1[3], plots_sudden_2[3], plots_sudden_3[3], parameters=parameters, threshold=True,
                 thresholdvalues=[0.5, 0.875, 1.6415210951546093], thresholdlabel='Threshold Values for R = 0.23')

#plot M_dim(t)
plotting.combine(plots_sudden_1[4], plots_sudden_2[4], plots_sudden_3[4], parameters=parameters, threshold=True,
                 thresholdvalues=[7, 4, 2.1321], thresholdlabel='Threshold Values for R = 0.23')


"Oscillating freshwater supply, no noise. "
#function R_oscillating = 1/2 * np.sin(0.01*t) + R_const

plots_1, parameters = stommel_model.run(1/2, 0.01, R_function=Rfunc.R_oscillating, noise=False, t=5000*365*24*3600,
                                        function_type='Oscillating', n_tstep=300)


#plotting M(t) without noise dim

plotting.combine(plots_1[4], parameters=parameters)

#plotting non dim M and R
plotting.combine(plots_1[1], plots_1[2], parameters=parameters)

#plotting delta S(t) dim
plotting.combine(plots_1[3], parameters=parameters)






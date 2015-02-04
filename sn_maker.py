'''
Tenerife
Supernova generator

'''
import numpy as n


def sn_ia(t,par):
	'''
	Supernova Type Ia functional form
	Contardo et al. 2000, A&A, 359, 876
	'''
	f0 = par[0]
	gamma = par[1]
	t0 = par[2]		# time zero
	g0 = par[3]		# amplitude of peak
	sig0 = par[4]	# width
	tau = par[5]
	theta = par[6]

	f1 = f0 + gamma*(t - t0) + g0*n.exp(-(t-t0)**2/(2.0*sig0**2))
	f2 = 1.0 - n.exp((tau - t)/theta) 
	return f1/f2

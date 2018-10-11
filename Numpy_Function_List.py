import numpy as np

x = 1.0								#define a float
y = 2.0								#define a second float

#trigonometry
print(np.sin(x))					#sin(x)
print(np.cos(x))					#cos(x)
print(np.tan(x))					#tan(x)
print(np.arcsin(x))					#arcsin(x)
print(np.arccos(x))					#arccos(x)
print(np.arctan(x))					#arctan(x)
print(np.arctan2(x,y))				#arctan(x/y)
print(np.rad2deg(x))				#convert deg. to rad.

#hyperbolic functions
print(np.sinh(x))					#sinh(x)
print(np.cosh(x))					#cosh(x)
print(np.tanh(x))					#tanh(x)
print(np.arcsinh(x))				#arcsinh(x)
print(np.arccosh(x))				#arccosh(x)
print(np.arctanh(x))				#arctanh(x)

#exponents and logarithms
print(np.exp(x))					#e^x
print(np.log(x))					#ln(x)
print(np.log10(x))					#log_10(x)
print(np.log2(x))					#log_2(x)

#min/max/misc
print(np.fabs(x))					#absolute value of x
print(np.fmin(x,y))					#min of x and y
print(np.fmax(x,y))					#max of x and y

#populate arrays
n = 100								#define an int
z = np.arange(n,dtype=float)		#get an array [0.0, n-1]
z *= 2.0*np.pi/float(n-1)			#z = [0, 2*pi]
sin_z = np.sin(z)					#get an array sin(z)

#interpolation
print(np.interp(0.75,z,sin_z))		#interpolate sin(0.75)
print(np.sin(0.75))
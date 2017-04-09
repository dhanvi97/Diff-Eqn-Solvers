import numpy as np
import sympy as sp
import mpmath as mp
#from sympy.functions import Abs
import matplotlib.pyplot as plt


if __name__ == "__main__":
	a = 0.0
	b = 5.0
	x , y = sp.symbols("x y")
	f = x - 1
	g = sp.lambdify([x , y], f)
	x_0 = 0.0
	y_0 = 0.0
	h = 0.01
	nodes = [(x_0+i*h) for i in range(0,(int)(b/h),1)]
	y_val = [y_0]
	for i in xrange(0,(int)(b/h)-1,1):
		#print(h*g(nodes[i],y_val[-1]))
		f_val = y_val[-1] + h*g(nodes[i],y_val[-1])
		y_val.append(f_val)
	plt.plot(nodes, (int)(b/h)*[0], 'b-')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.plot(nodes, y_val, 'r-')
	plt.show()
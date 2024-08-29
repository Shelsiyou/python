#1.
import numpy as np
import matplotlib.pyplot as plt
# #задание 1
# a,b,c=1,10,1000 
# d=(np.log((np.e*(1/(np.sin(a)+1)))/(5/4+1/(a**15)))/np.log(1+(a**2)))
# n=(np.log((np.e*(1/(np.sin(b)+1)))/(5/4+1/(b**15)))/np.log(1+(b**2)))
# m=(np.log((np.e*(1/(np.sin(c)+1)))/(5/4+1/(c**15)))/np.log(1+(c**2)))
# print("x=1",d,"x=10",n,"x=1000",m)

# #Задание 2 y(x) = x*x - x - 6
# x = np.arange(-5, 5.01, 0.01)
# plt.plot(x, x**2 - x - 6, x, x-x)
# plt.show()
# # x= -2, 3

# Задание 3
# x = np.arange(-5, 5.01, 0.01)
# plt.plot(x, (np.log((x**2+1)*(np.exp(-(x**(0.5)/10))))/np.log(1+np.tan(1/(1+np.sin(x)**2)))) )
# plt.show()

# Задание 4
# x = np.arange(-100, 100, 1)
# plt.plot(x, eval(input()))
# with plt.xkcd():
#     plt.title('котенок-поваренок')
#     plt.xlabel('миу миу')
#     plt.ylabel('мяу мяу')
# plt.grid(True)
# plt.show()

# Задание 5
# x = [1, 3, 5, 7, 11]
# y = [0.5, 0.6, 0.3, 0.9, 0.38]
# plt.errorbar(x, y, xerr=0.01, yerr=0.01)
# p, v = np.polyfit(x, y, deg=1, cov=True)
# p_f = np.poly1d(p)
# z = p_f([1, 2, 3, 4, 5])
# plt.title(r'миоооо')
# plt.plot(x, eval('y'))
# plt.show()

fjdfjsfj


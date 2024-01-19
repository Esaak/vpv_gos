import numpy as np



#Particles constants
e = 1.6 * 1e-19 # Кл
m = 8*1e-28 # kg

m_co2 = 7.3*1e-26 # kg
dt = 10**(-8) # c
dh = 1  # м
eps = 0.2
particle_numbers = 50
#Planet constants
R = 6 * 1e6 # м
g = 9.8 * 0.84 # м/с^2
Po = 1e7 # Па
T = 773 # K
N = 10**8

n = []

R = 4 * 1e4
#atmosphere_height = R  # м
atmosphere_height = 4 * 1e4  # м
y_lim = np.array([0.1, 0.7], dtype=float) * atmosphere_height + R # м

#Physics constants
c = 3*1e8 # м / с
alpha = 1.2*1e-28
k = 1.38*1e-23 # Дж/К
h_ = 6.58*1e-16 # эВ * с
coef_reflection = 0.3


w0 = 3/2. * k * T / (h_ * e)

# def atmosphere_height_find():
#     delta_n = 0.00001
#     return max(- k*T * np.log(delta_n * k * T/(4* np.pi * alpha * Po))/(m * g), R)
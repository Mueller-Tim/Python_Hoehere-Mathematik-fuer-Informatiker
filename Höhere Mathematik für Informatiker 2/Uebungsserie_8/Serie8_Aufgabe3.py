import numpy as np


REFERENCE_MASS = 5.972e24  # Earth mass in kg


radius_km = np.array([0., 800., 1200., 1400., 2000., 3000., 3400., 3600., 4000., 5000., 5500., 6370.])
density_kgm3 = np.array([13000., 12900., 12700, 12000., 11650., 10600., 9900., 5500., 5300., 4750., 4500., 3300.])


def spherical_shell_surface_area(radius, density):
    radius_m = radius * 1000
    return density * 4.0 * np.pi * radius_m**2


def muellti3_S8_Aufg3a(x, y):
    ##radius_m = radius * 1000
    ##return np.trapz(values, x=radius_m)
    x_a = x.copy()
    y_a = y.copy()
    n = x.size

    Tf_neq = 0
    for i in range(0, n-1):
        Tf_neq += ((y_a[i] + y_a[i+1]) / 2 * (x_a[i+1] - x_a[i]))
    return Tf_neq

##a)
surface_areas = spherical_shell_surface_area(radius_km, density_kgm3)
total_mass = muellti3_S8_Aufg3a(radius_km, surface_areas)
print(f"Calculated mass using trapezoidal rule: {total_mass} kg")


##b)
absolute_error = np.abs(total_mass - REFERENCE_MASS)
relative_error = absolute_error / REFERENCE_MASS

print(f"Absolute error: {absolute_error}")
print(f"Relative error: {relative_error}")




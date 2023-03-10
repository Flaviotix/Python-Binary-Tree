from math import pi


def cube(x):
    return x ** 3


def volumeSphere(r):
    return 4 / 3 * pi * cube(r)


rayon = 5
volume = volumeSphere(rayon)
print("Le volume d'une sphère de rayon", rayon, "est", volume)

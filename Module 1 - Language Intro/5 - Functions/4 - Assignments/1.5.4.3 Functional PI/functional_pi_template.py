import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    a = 1
    b = 1 / (math.sqrt(2))
    p = 1
    t = 1 / 4

    for i in range(1,10):
        a_new = (a + b) / 2
        b_new = math.sqrt(a * b)
        p_new = 2 * p
        t = t - p * math.pow(a_new - a, 2)

        a = a_new
        b = b_new
        p = p_new

        i += 1

    # change this so an actual value is returned
    return (math.pow(a+b,2)) / (4 * t)


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")

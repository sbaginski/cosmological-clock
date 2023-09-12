import math


def divide_safely(a: float, b: float) -> float:
    if b == 0:
        return math.inf
    elif b == math.inf:
        return 0
    else:
        return a / b


def calculate_simpsons_rule(a: float, b: float, f: callable) -> float:
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))


def integrate(a: float, b: float, f: callable, n: int = 10) -> float:
    interval_length = (b - a) / n
    result = 0
    left = a
    right = left + interval_length
    while right <= b:
        result += calculate_simpsons_rule(left, right, f)
        left += interval_length
        right += interval_length
    result += calculate_simpsons_rule(left, b, f)
    return result


if __name__ == '__main__':
    H_0 = 70
    Omega_r = 0
    Omega_m = 0.3
    Omega_Lambda = 0.7
    Omega = Omega_r + Omega_m + Omega_Lambda

    def f(x):
        return divide_safely(
            1,
            (H_0 * (divide_safely(Omega_r, x**2) 
                    + divide_safely(Omega_m, x) 
                    + Omega_Lambda * x**2 
                    + (1 - Omega))**(1 / 2))
        )

    z = int(input('redshift: '))
    a = 1 / (1 + z)
    print(f'{integrate(0, a, f, 1000000) * 3.086e19 * 1e-9 / (3600 * 24 * 365)} Gyr')
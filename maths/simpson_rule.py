"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of suming 'Equally Spaced Abscissas'

method 2:
"Simpson Rule"

"""


def method_2(boundary, steps):
    # "Simpson Rule"
    # int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 3.0) * f(a)
    for cnt, i in enumerate(x_i, start=2):
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i)
    y += (h / 3.0) * f(b)
    return y


def make_points(a, b, h):
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


def f(x):  # enter your function here
    return (x - 0) * (x - 0)


def main():
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # define number of steps or resolution
    boundary = [a, b]  # define boundary of integration
    y = method_2(boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    main()

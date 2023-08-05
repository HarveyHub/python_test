from matplotlib import pyplot as plt
import numpy as np
import matplotlib

matplotlib.use("TkAgg")


def plt_settings():
    plt.axis("equal")
    plt.legend()
    plt.grid()


def teardown_module():
    plt_settings()
    plt.show()


xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)


def test_sin():
    ys = np.sin(xs)

    plt.plot(xs, ys, "b-", label="sin")


def test_cos():
    ys = np.cos(xs)
    plt.plot(xs, ys, "r-", label="cos")

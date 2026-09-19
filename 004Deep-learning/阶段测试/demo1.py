import numpy as np
import matplotlib.pyplot as plt

# 一个简单的二维损失函数
# 最优点在 (0, 0)
def loss(x, y):
    return x**2 + 10 * y**2


# 梯度
def gradient(x, y):
    return 2 * x, 20 * y


def train_sgd(steps=100, lr=0.03):
    x, y = -4.0, 4.0
    path = [(x, y)]

    for _ in range(steps):
        gx, gy = gradient(x, y)

        x -= lr * gx
        y -= lr * gy

        path.append((x, y))

    return np.array(path)


def train_rmsprop(steps=100, lr=0.3, beta=0.9, eps=1e-8):
    x, y = -4.0, 4.0

    vx, vy = 0.0, 0.0

    path = [(x, y)]

    for _ in range(steps):
        gx, gy = gradient(x, y)

        # RMSProp：指数移动平均
        vx = beta * vx + (1 - beta) * gx**2
        vy = beta * vy + (1 - beta) * gy**2

        # RMSProp：自适应调整步长
        x -= lr * gx / (np.sqrt(vx) + eps)
        y -= lr * gy / (np.sqrt(vy) + eps)

        path.append((x, y))

    return np.array(path)


sgd_path = train_sgd()
rms_path = train_rmsprop()


# 绘制损失函数等高线
x = np.linspace(-4.5, 4.5, 300)
y = np.linspace(-4.5, 4.5, 300)

X, Y = np.meshgrid(x, y)

Z = loss(X, Y)

plt.figure(figsize=(8, 6))

plt.contour(X, Y, Z, levels=20)

plt.plot(
    sgd_path[:, 0],
    sgd_path[:, 1],
    marker="o",
    markersize=2,
    label="SGD"
)

plt.plot(
    rms_path[:, 0],
    rms_path[:, 1],
    marker="o",
    markersize=2,
    label="RMSProp"
)

plt.scatter(0, 0, marker="*", s=200, label="Minimum")

plt.xlabel("x")
plt.ylabel("y")
plt.title("SGD vs RMSProp")

plt.legend()
plt.grid()

plt.show()
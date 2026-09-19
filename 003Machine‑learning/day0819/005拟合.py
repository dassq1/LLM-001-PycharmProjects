# ===================== 准备数据 导入库 =====================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression  # 线性回归模型
from sklearn.preprocessing import PolynomialFeatures  # 多项式特征生成器
from sklearn.model_selection import train_test_split  # 划分数据集
from sklearn.metrics import mean_squared_error  # 导入均方误差

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置matplotlib中文字体
plt.rcParams["axes.unicode_minus"] = False

# ===================== 生成数据 =====================
# 在-π ~ π之间生成300个点，reshape转为二维 (样本数,特征数)
x = np.linspace(-np.pi, np.pi, num=300).reshape(-1, 1)
print("x.shape:", x.shape)

np.random.seed(42)  # 设置随机种子，保证每次运行结果一致
y = np.sin(x) + np.random.uniform(-0.8, 0.8, 300).reshape(-1, 1)
print("y.shape:", y.shape)

# ===================== 创建1行3列画布，画原始散点 =====================
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
axs[0].scatter(x, y)
axs[1].scatter(x, y)
axs[2].scatter(x, y)

# ===================== 数据集划分：训练集、测试集 =====================
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
print("train_x.shape, test_x.shape:", train_x.shape, test_x.shape)
print("train_y.shape, test_y.shape:", train_y.shape, test_y.shape)

# ===================== 1、欠拟合：普通线性回归 =====================
# 定义模型
model = LinearRegression()
# 训练模型
model.fit(train_x, train_y)
print("W系数, b偏置：", model.coef_, model.intercept_)  # W 和 b

# 模型评估（看损失值，均方误差MSE）
train_loss = mean_squared_error(train_y, model.predict(train_x))
test_loss = mean_squared_error(test_y, model.predict(test_x))
print(f"欠拟合：train误差:{train_loss}, test误差:{test_loss}")

# 绘制拟合曲线
axs[0].plot(x, model.predict(x), c='r')
axs[0].text(-3, 1.3, f"测试集均方误差:{test_loss:.4f}")
axs[0].text(-3, 1, f"训练集均方误差:{train_loss:.4f}")


score = model.score(test_x, test_y)  # R^2决定系数
print(f"欠拟合 测试集 R^2 :{score}")

# ===================== 2、恰好拟合：5次多项式 =====================
# 特征工程，生成5次多项式特征
poly5 = PolynomialFeatures(degree=5)
train_x2 = poly5.fit_transform(train_x)  # fit学习转换规则，transform转换训练集
test_x2 = poly5.transform(test_x)         # 测试集只transform，不要fit
print("poly5转换后 train_x2.shape, test_x2.shape：", train_x2.shape, test_x2.shape)

# 训练模型
model.fit(train_x2, train_y)
print("poly5 W系数, b偏置：", model.coef_, model.intercept_)

# 模型评估
train_loss = mean_squared_error(train_y, model.predict(train_x2))
test_loss = mean_squared_error(test_y, model.predict(test_x2))
print(f"恰好拟合:训练误差{train_loss},测试误差:{test_loss}")

# 绘制曲线：注意全部x也要做多项式转换
axs[1].plot(x, model.predict(poly5.transform(x)), c='r')
axs[1].text(-3, 1.3, f"测试集均方误差：{test_loss:.4f}")
axs[1].text(-3, 1, f"训练集均方误差：{train_loss:.4f}")

score = model.score(test_x2, test_y)
print(f"恰好拟合 测试集R^2：{score}")

# ===================== 3、过拟合：20次高次多项式 =====================
poly20 = PolynomialFeatures(degree=20)
train_x3 = poly20.fit_transform(train_x)
test_x3 = poly20.transform(test_x)
print("poly20转换后 train_x3.shape, test_x3.shape：", train_x3.shape, test_x3.shape)

# 训练模型
model.fit(train_x3, train_y)
print("poly20 W系数, b偏置：", model.coef_, model.intercept_)

# 模型评估 看损失
train_loss = mean_squared_error(train_y, model.predict(train_x3))
test_loss = mean_squared_error(test_y, model.predict(test_x3))
print(f"过拟合的训练误差:{train_loss},测试误差{test_loss}")

# 绘制曲线
axs[2].plot(x, model.predict(poly20.transform(x)), c='r')
axs[2].text(-3, 1.3, f"测试集均方误差:{test_loss:.4f}")
axs[2].text(-3, 1, f"训练集均方误差:{train_loss:.4f}")


score = model.score(test_x3, test_y)
print(f"过拟合 测试集R^2：{score}")

# 绘图全部写完之后，显示图片
plt.show()
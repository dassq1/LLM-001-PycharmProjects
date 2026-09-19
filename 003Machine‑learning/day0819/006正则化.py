import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge  # 线性回归模型 和 拉索回归 和 岭回归
from sklearn.preprocessing import PolynomialFeatures  # 构建多项式特征
from sklearn.model_selection import train_test_split  # 划分数据集: 训练集 测试集
from sklearn.metrics import mean_squared_error  # 均方误差损失函数(自己看)

# plt显示中文
plt.rcParams["font.sans-serif"] = ["KaiTi"]   # windows 系统
# 不使用unicode的 -号
plt.rcParams["axes.unicode_minus"] = False

# 1. 读取数据(生成数据: 特征和标签)
x = np.linspace(-np.pi, np.pi, 300).reshape(-1, 1)
y = np.sin(x) + np.random.uniform(-0.5, 0.5, 300).reshape(-1, 1)

#  散点图
fig, axs = plt.subplots(2, 3, figsize=(15, 8))
axs[0, 0].scatter(x, y)
axs[0, 1].scatter(x, y)
axs[0, 2].scatter(x, y)
# 2. 数据清洗(略)

# 3. 划分数据集: 训练集 测试集
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
print(train_x.shape, test_x.shape)
# 4. 定义模式: 线性回归模型
model = LinearRegression()

# 过拟合
# 特征工程
poly20 = PolynomialFeatures(degree=20)  # 构建多项式特征
train_x = poly20.fit_transform(train_x)  # 训练集都是fit_transform
test_x = poly20.transform(test_x)  # 测试集都是transform
print(train_x.shape, test_x.shape)

# 5. 训练模型
model.fit(train_x, train_y)
print(model.coef_, model.intercept_)  # 参数和截距
# 6. 模型评估  (看损失值)
test_loss = mean_squared_error(test_y, model.predict(test_x))
print(f"过拟合: 测试误差: {test_loss}")
# 7. 绘制曲线
axs[0, 0].plot(x, model.predict(poly20.transform(x)), c='r')
axs[0, 0].text(-3, 1, f"测试集均方误差：{test_loss:.4f}")
axs[1, 0].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))

#  Lasso 回归 L1
model = Lasso(alpha=0.009)  # alpha 正则话强度
model.fit(train_x, train_y)
test_loss = mean_squared_error(test_y, model.predict(test_x))
print(model.coef_, model.intercept_)
print(f"Lasso: 测试误差: {test_loss}")

axs[0, 1].plot(x, model.predict(poly20.transform(x)), c='r')
axs[0, 1].text(-3, 1, f"测试集均方误差：{test_loss:.4f}")
axs[1, 1].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))

#  Ridge 回归 L2
model = Ridge(alpha=0.009)  # alpha 正则话强度
model.fit(train_x, train_y)
test_loss = mean_squared_error(test_y, model.predict(test_x))
print(model.coef_, model.intercept_)
print(f"Ridge: 测试误差: {test_loss}")

axs[0, 2].plot(x, model.predict(poly20.transform(x)), c='r')
axs[0, 2].text(-3, 1, f"测试集均方误差：{test_loss:.4f}")
axs[1, 2].bar(np.arange(len(model.coef_.reshape(-1))), model.coef_.reshape(-1))
plt.show()
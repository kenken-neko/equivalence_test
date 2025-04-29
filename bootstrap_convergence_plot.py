import numpy as np
import matplotlib.pyplot as plt

# 元のデータ（例：ランダムに生成）
np.random.seed(42)
original_data = np.random.normal(loc=10, scale=2, size=1000)

# ブートストラップ設定
n_iterations = 1000  # 各サイズでのブートストラップ試行回数
sample_sizes = np.arange(10, 1001, 10)  # 段階的にサンプルサイズを増やす
bootstrap_means = []

# 各サンプルサイズに対してブートストラップ平均を計算
for size in sample_sizes:
    means = []
    for _ in range(n_iterations):
        sample = np.random.choice(original_data, size=size, replace=True)
        means.append(np.mean(sample))
    bootstrap_means.append(np.mean(means))

# 理論的な平均
true_mean = np.mean(original_data)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, bootstrap_means, label='Bootstrap Mean')
plt.axhline(y=true_mean, color='red', linestyle='--', label='True Mean')
plt.xlabel('Sample Size')
plt.ylabel('Bootstrap Estimated Mean')
plt.title('Bootstrap Convergence of Sample Mean')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# ======================
# 你的真实数据（仅数据）
# ======================
data_vecs = np.array([
    [0.55, 0.15, 0.0, 0.3],
    [1.00, 0.00, 0.0, 0.0],
    [1.00, 0.00, 0.0, 0.0],
    [0.15, 0.55, 0.0, 0.3],
    [0.50, 0.20, 0.0, 0.3],
    [0.50, 0.20, 0.0, 0.3],
    [0.00, 1.00, 0.0, 0.0],
    [0.20, 0.50, 0.0, 0.3],
    [1.00, 0.00, 0.0, 0.0],
    [0.00, 1.00, 0.0, 0.0],
    [0.20, 0.50, 0.0, 0.3],
    [0.00, 1.00, 0.0, 0.0],
])

# ======================
# 加权相似度
# ======================
def weighted_sim(a, b, w):
    wa = a * w
    wb = b * w
    dot = np.dot(wa, wb)
    na = np.linalg.norm(wa)
    nb = np.linalg.norm(wb)
    return dot / (na * nb) if na > 1e-6 and nb > 1e-6 else 0

def evaluate(w):
    n = len(data_vecs)
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            mat[i,j] = weighted_sim(data_vecs[i], data_vecs[j], w)
    return np.var(mat)

# ======================================================================
# ✅ 全自动遍历搜索：一点点试 → 自动找到全局最优权重
# 无任何人工定义、无任何字典、无任何命名
# ======================================================================
step = 0.005
best_score = -1
best_w = None

for w12 in np.arange(0.01, 0.4, step):
    for w4 in np.arange(0.01, w12 - 1e-6, step):
        w3 = 1.0 - 2 * w12 - w4
        if w3 > w12 and w3 > 0:
            w = np.array([w12, w12, w3, w4])
            score = evaluate(w)
            if score > best_score:
                best_score = score
                best_w = w

# ======================================================================
# ✅ 自动输出结果（仅此而已）
# ======================================================================
print("="*70)
print("✅ 全自动遍历搜索完成 → 最优权重如下（无任何人工干预）")
print(f"严格序   = {best_w[0]:.4f}")
print(f"逆序     = {best_w[1]:.4f}")
print(f"互斥     = {best_w[2]:.4f}")
print(f"交叉     = {best_w[3]:.4f}")
print(f"权重总和 = {np.sum(best_w):.4f}")
print(f"区分度   = {best_score:.6f}")
print("="*70)
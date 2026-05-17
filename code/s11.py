import numpy as np

# ======================
# 1. 你的真实数据（来自截图）
# 维度顺序：[严格序, 逆序, 互斥, 交叉]
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
# 2. 加权余弦相似度（论文核心公式）
# ======================
def weighted_cosine_similarity(a, b, weights):
    wa = a * weights
    wb = b * weights
    dot_product = np.dot(wa, wb)
    norm_a = np.linalg.norm(wa)
    norm_b = np.linalg.norm(wb)
    if norm_a < 1e-8 or norm_b < 1e-8:
        return 0.0
    return dot_product / (norm_a * norm_b)


# ======================
# 3. 基于加权相似度计算区分度（评分函数）
# ======================
def evaluate_weight(weights):
    n = len(data_vecs)
    sim_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sim_matrix[i, j] = weighted_cosine_similarity(data_vecs[i], data_vecs[j], weights)
    return np.var(sim_matrix)  # 方差越大，区分能力越强


# ======================
# 4. 全自动遍历搜索（step=0.05）
# 约束：
# 互斥 > 严格序 = 逆序 > 交叉
# 权重和 = 1
# ======================
step = 0.05  # 已改成 0.05
best_score = -1
best_weights = None

# 严格序 = 逆序
for w_strict_inv in np.arange(0.05, 0.4, step):
    # 交叉必须 < 严格序
    for w_cross in np.arange(0.01, w_strict_inv - 1e-6, step):
        # 自动计算互斥权重
        w_excl = 1.0 - w_strict_inv - w_strict_inv - w_cross

        # 约束过滤
        if w_excl <= w_strict_inv or w_excl < 0:
            continue

        # 合法权重组合
        w = np.array([w_strict_inv, w_strict_inv, w_excl, w_cross])

        # 基于加权相似度评分
        score = evaluate_weight(w)

        # 记录最优
        if score > best_score:
            best_score = score
            best_weights = w

# ======================
# 5. 输出最终结果
# ======================
w_s, w_i, w_e, w_c = best_weights

print("=" * 70)
print("✅ 权重确定实验结果（数据驱动 + 加权相似度优化）")
print("=" * 70)
print(f"严格序权重 = {w_s:.4f}")
print(f"逆序权重   = {w_i:.4f}")
print(f"互斥权重   = {w_e:.4f}")
print(f"交叉权重   = {w_c:.4f}")
print(f"权重总和   = {np.sum(best_weights):.4f}")
print("=" * 70)
print("约束校验（全部必须为 True）：")
print(f"互斥 > 严格序    : {w_e > w_s}")
print(f"严格序 = 逆序    : {abs(w_s - w_i) < 1e-6}")
print(f"严格序 > 交叉    : {w_s > w_c}")
print(f"权重和为 1       : {abs(np.sum(best_weights) - 1) < 1e-6}")
print("=" * 70)
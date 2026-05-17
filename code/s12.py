import numpy as np
import matplotlib.pyplot as plt

# ======================
# 你的真实数据
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
# 加权余弦相似度
# ======================
def weighted_cosine_similarity(a, b, weights):
    wa = a * weights
    wb = b * weights
    dot = np.dot(wa, wb)
    na = np.linalg.norm(wa)
    nb = np.linalg.norm(wb)
    return dot / (na * nb) if na > 1e-8 and nb > 1e-8 else 0.0

def evaluate(weights):
    n = len(data_vecs)
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            mat[i,j] = weighted_cosine_similarity(data_vecs[i], data_vecs[j], weights)
    return np.var(mat)

# ======================
# 自动寻优（step=0.05）
# ======================
step = 0.05
best_score = -1
best_w = None

for w12 in np.arange(0.05, 0.4, step):
    for w4 in np.arange(0.01, w12-1e-6, step):
        w3 = 1 - 2*w12 - w4
        if w3 > w12 and w3 > 0:
            w = np.array([w12, w12, w3, w4])
            s = evaluate(w)
            if s > best_score:
                best_score = s
                best_w = w

# ======================
# 输出最优权重
# ======================
print("="*60)
print("最优权重（自动计算）")
print(f"严格序: {best_w[0]:.2f}")
print(f"逆序  : {best_w[1]:.2f}")
print(f"互斥  : {best_w[2]:.2f}")
print(f"交叉  : {best_w[3]:.2f}")
print(f"总和  : {sum(best_w):.2f}")
print("="*60)

# ======================
# ✅ 自动绘制敏感性分析图（你论文里的 图X）
# ======================
candidates = [
    np.array([0.20,0.20,0.50,0.10]),
    np.array([0.25,0.25,0.40,0.10]),
    best_w,
    np.array([0.30,0.30,0.35,0.05]),
    np.array([0.25,0.25,0.30,0.20]),
]
scores = [evaluate(w) for w in candidates]
labels = ["组合1","组合2","最优权重","组合4","组合5"]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(8,4))
plt.bar(labels, scores, color=['g','b','r','b','g'])
plt.title("权重敏感性分析")
plt.ylabel("相似度区分度")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
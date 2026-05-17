import numpy as np

# 定义密码矩阵A
A = np.array([[1, 2, 3,],
              [1, 1, 2],
              [0, 1, 2]])
# 计算A的逆矩阵
A_inv = np.linalg.inv(A)

# 定义接收到的矩阵C
C = np.array([[45, 74, 30, 40],
              [33, 47, 19, 25],
              [24, 32, 19, 16]])
# 计算解密后的矩阵
decrypted_matrix = np.dot(A_inv, C)
print(decrypted_matrix)

def matrix_num_to_letter(decrypted_matrix):
    result = []
    for row in decrypted_matrix:
        new_row = []
        for num in row:
            num_rounded = int(round(num))  # 强制取整
            letter = ''
            if num_rounded == 0:
                letter = ' '
            elif 1 <= num_rounded <= 26:
                letter = chr(num_rounded + 64)
            else:
                letter = '?'  # 处理越界值
            new_row.append(letter)
        result.append(new_row)
    return np.array(result)
print(matrix_num_to_letter(decrypted_matrix))

import numpy as np

# 定义矩阵 M
M = np.array([
    [0.4, 0.6, 0.5, 0.7],
    [0.7, 1.0, 0.95, 0.9],
    [0.2, 0.5, 0.6, 0.4]
])

# 定义矩阵 N
N = np.array([
    [10000, 11000, 10000, 9500],
    [7000, 7500, 8000, 6500],
    [11000, 9000, 10500, 9500],
    [9000, 10000, 9500, 10500]
])

# 计算矩阵乘积 MN
MN = np.dot(M, N)

print(MN)





import numpy as np
import pandas as pd


def compare_matrices(matrix_a, matrix_b):
    """比较两个矩阵的对应元素，生成比较矩阵"""
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("两个矩阵的形状必须相同")
    result = np.where(matrix_a == matrix_b, 1, 0)
    np.fill_diagonal(result, 0)
    return result


def generate_weight_matrix(operations, similarity_scores):
    """生成自定义权重矩阵"""
    n = len(operations)
    weight_matrix = np.zeros((n, n))
    for i, op_i in enumerate(operations):
        for j, op_j in enumerate(operations):
            if i != j:
                weight_matrix[i, j] = (similarity_scores[op_i] + similarity_scores[op_j]) / 2
    return pd.DataFrame(weight_matrix, index=operations, columns=operations)


def calculate_weighted_sum(comparison_matrix, weight_matrix):
    """计算比较矩阵的加权和"""
    if isinstance(weight_matrix, pd.DataFrame):
        weight_matrix = weight_matrix.values
    if weight_matrix.shape != comparison_matrix.shape:
        raise ValueError("权重矩阵与比较矩阵形状不匹配")
    return np.sum(comparison_matrix * weight_matrix)


def calculate_similarity_score(weighted_sum, operations):
    """计算0-1区间的相似性得分"""
    n = len(operations)
    max_sum = n * (n - 1)
    return weighted_sum / max_sum if max_sum != 0 else 0


def process_workflow_comparison(matrix_a, matrix_b, weight_matrix):
    """整合工作流程比较流程"""
    comparison_matrix = compare_matrices(matrix_a, matrix_b)
    weighted_sum = calculate_weighted_sum(comparison_matrix, weight_matrix)
    operations = list(weight_matrix.index)
    similarity_score = calculate_similarity_score(weighted_sum, operations)
    return {
        'comparison_matrix': comparison_matrix,
        'weight_matrix': weight_matrix,
        'weighted_sum': weighted_sum,
        'similarity_score': similarity_score
    }


def filter_high_similarity_pairs(results, threshold=0.8):
    """筛选相似性得分大于阈值的结果"""
    return [r for r in results if r['similarity_score'] > threshold]


if __name__ == "__main__":
    operations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    matrix_dict = {
        'matrix_1': np.array([['-', 1, 1, 1, 1, 1, 1],
                             [2, '-', 1, 1, 1, 1, 1],
                             [2, 2, '-', 1, 1, 1, 1],
                             [2, 2, 2, '-', 1, 1, 1],
                             [2, 2, 2, 2, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_2': np.array([['-', 2, 1, 1, 1, 1, 1],
                             [1, '-', 1, 1, 1, 1, 1],
                             [2, 2, '-', 1, 1, 1, 1],
                             [2, 2, 2, '-', 1, 1, 1],
                             [2, 2, 2, 2, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_3': np.array([['-', 4, 1, 1, 4, 1, 1],
                             [4, '-', 4, 4, 1, 1, 1],
                             [2, 4, '-', 1, 4, 1, 1],
                             [2, 4, 2, '-', 4, 1, 1],
                             [4, 2, 4, 4, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_4': np.array([['-', 1, 1, 1, 1, 1, 1],
                             [2, '-', 1, 1, 1, 1, 1],
                             [2, 2, '-', 1, 2, 1, 1],
                             [2, 2, 2, '-', 2, 1, 1],
                             [2, 2, 1, 1, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_5': np.array([['-', 1, 1, 1, 1, 1, 1],
                             [2, '-', 2, 2, 1, 1, 1],
                             [2, 1, '-', 1, 1, 1, 1],
                             [2, 1, 2, '-', 1, 1, 1],
                             [2, 2, 2, 2, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_6': np.array([['-', 2, 1, 1, 2, 1, 1],
                             [1, '-', 1, 1, 1, 1, 1],
                             [2, 2, '-', 1, 2, 1, 1],
                             [2, 2, 2, '-', 2, 1, 1],
                             [1, 2, 1, 1, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object),
        'matrix_7': np.array([['-', 1, 1, 1, 1, 1, 1],
                             [2, '-', 1, 1, 1, 1, 1],
                             [2, 2, '-', 1, 4, 1, 1],
                             [2, 2, 2, '-', 4, 1, 1],
                             [2, 2, 4, 4, '-', 1, 1],
                             [2, 2, 2, 2, 2, '-', 1],
                             [2, 2, 2, 2, 2, 2, '-']], dtype=object)

    }
    all_results = []

    # 场景1-1-3：默认权重矩阵（D的相似性为0）
    print("场景1-1-3：使用默认权重矩阵")
    default_scores = {op: 0 if op == 'D' else 1 for op in operations}
    weight_matrix1_1_3 = generate_weight_matrix(operations, default_scores)
    result1_1_3 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_3'], weight_matrix1_1_3)
    result1_1_3.update({'matrix_pair': ('matrix_1', 'matrix_3'), 'scenario': '场景1-1-3'})
    all_results.append(result1_1_3)
    print(f"\n权重矩阵:\n{weight_matrix1_1_3.round(2)}\n相似性得分: {result1_1_3['similarity_score']:.2f}")

    # 场景1-1-1：自定义权重矩阵（A=2/3, D=0）
    print("\n场景1-1-1：使用自定义权重矩阵")
    custom_scores1_1_1 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_1_1 = generate_weight_matrix(operations, custom_scores1_1_1)
    result1_1_1 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_1'], weight_matrix1_1_1)
    result1_1_1.update({'matrix_pair': ('matrix_1', 'matrix_1'), 'scenario': '场景1-1-1'})
    all_results.append(result1_1_1)
    print(f"\n权重矩阵:\n{weight_matrix1_1_1.round(2)}\n相似性得分: {result1_1_1['similarity_score']:.2f}")

    # 场景1-1-2：自定义权重矩阵（A=3/7, C=1/3）
    print("\n场景1-1-2：使用自定义权重矩阵")
    custom_scores1_1_2 = {'A': 3/7, 'B': 1, 'C': 1/3, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_1_2 = generate_weight_matrix(operations, custom_scores1_1_2)
    result1_1_2 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_2'], weight_matrix1_1_2)
    result1_1_2.update({'matrix_pair': ('matrix_1', 'matrix_2'), 'scenario': '场景1-1-2'})
    all_results.append(result1_1_2)
    print(f"\n权重矩阵:\n{weight_matrix1_1_2.round(2)}\n相似性得分: {result1_1_2['similarity_score']:.2f}")

    # 场景1-1-4：自定义权重矩阵（A=1/4, C=1/3, F=1/3）
    print("\n场景1-1-4：使用自定义权重矩阵")
    custom_scores1_1_4 = {'A': 1/4, 'B': 1, 'C': 1/3, 'D': 1, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix1_1_4 = generate_weight_matrix(operations, custom_scores1_1_4)
    result1_1_4 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_4'], weight_matrix1_1_4)
    result1_1_4.update({'matrix_pair': ('matrix_1', 'matrix_4'), 'scenario': '场景1-1-4'})
    all_results.append(result1_1_4)
    print(f"\n权重矩阵:\n{weight_matrix1_1_4.round(2)}\n相似性得分: {result1_1_4['similarity_score']:.2f}")

    # 场景12-3-7：自定义权重矩阵
    print("\n场景12-3-7：使用自定义权重矩阵")
    custom_scores12_3_7 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix12_3_7 = generate_weight_matrix(operations, custom_scores12_3_7)
    result12_3_7 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_7'], weight_matrix12_3_7)
    result12_3_7.update({'matrix_pair': ('matrix_3', 'matrix_7'), 'scenario': '场景12-3-7'})
    all_results.append(result12_3_7)
    print(f"\n权重矩阵:\n{weight_matrix12_3_7.round(2)}\n相似性得分: {result12_3_7['similarity_score']:.2f}")

    # 场景12-3-11-7：自定义权重矩阵
    print("\n场景12-3-11-7：使用自定义权重矩阵")
    custom_scores12_3_11_7 = {'A': 1/9, 'B': 1/3, 'C': 1/3, 'D': 0, 'E': 0, 'F': 2/3, 'G': 1}
    weight_matrix12_3_11_7 = generate_weight_matrix(operations, custom_scores12_3_11_7)
    result12_3_11_7 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_7'], weight_matrix12_3_11_7)
    result12_3_11_7.update({'matrix_pair': ('matrix_3', 'matrix_7'), 'scenario': '场景12-3-11-7'})
    all_results.append(result12_3_11_7)
    print(f"\n权重矩阵:\n{weight_matrix12_3_11_7.round(2)}\n相似性得分: {result12_3_11_7['similarity_score']:.2f}")

    # 场景12-3-11-1：自定义权重矩阵
    print("\n场景12-3-11-1：使用自定义权重矩阵")
    custom_scores12_3_11_1 = {'A': 3/7, 'B': 1 / 3, 'C': 1 / 3, 'D': 0, 'E': 0, 'F': 1 / 3, 'G': 1}
    weight_matrix12_3_11_1 = generate_weight_matrix(operations, custom_scores12_3_11_1)
    result12_3_11_1 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_1'], weight_matrix12_3_11_1)
    result12_3_11_1.update({'matrix_pair': ('matrix_3', 'matrix_1'), 'scenario': '场景12-3-11-1'})
    all_results.append(result12_3_11_1)
    print(f"\n权重矩阵:\n{weight_matrix12_3_11_1.round(2)}\n相似性得分: {result12_3_11_1['similarity_score']:.2f}")

    # 场景12-3-10-3：自定义权重矩阵
    print("\n场景12-3-10-3：使用自定义权重矩阵")
    custom_scores12_3_10_3 = {'A': 2/3, 'B': 0, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix12_3_10_3 = generate_weight_matrix(operations, custom_scores12_3_10_3)
    result12_3_10_3 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_3'], weight_matrix12_3_10_3)
    result12_3_10_3.update({'matrix_pair': ('matrix_3', 'matrix_3'), 'scenario': '场景12-3-10-3'})
    all_results.append(result12_3_10_3)
    print(f"\n权重矩阵:\n{weight_matrix12_3_10_3.round(2)}\n相似性得分: {result12_3_10_3['similarity_score']:.2f}")

    # 场景1-1-3-3：自定义权重矩阵
    print("\n场景1-1-3-3：使用自定义权重矩阵")
    custom_scores1_1_3_3 = {'A': 1/4, 'B': 1, 'C': 1, 'D': 1 / 3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_1_3_3 = generate_weight_matrix(operations, custom_scores1_1_3_3)
    result1_1_3_3 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_3'], weight_matrix1_1_3_3)
    result1_1_3_3.update({'matrix_pair': ('matrix_1', 'matrix_3'), 'scenario': '场景1-1-3-3'})
    all_results.append(result1_1_3_3)
    print(f"\n权重矩阵:\n{weight_matrix1_1_3_3.round(2)}\n相似性得分: {result1_1_3_3['similarity_score']:.2f}")

    # 场景1-1-3-6：自定义权重矩阵
    print("\n场景1-1-3-6：使用自定义权重矩阵")
    custom_scores1_1_3_6 = {'A': 2/ 3, 'B': 1, 'C': 1, 'D': 1 / 3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_1_3_6 = generate_weight_matrix(operations, custom_scores1_1_3_6)
    result1_1_3_6 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_6'], weight_matrix1_1_3_3)
    result1_1_3_6.update({'matrix_pair': ('matrix_1', 'matrix_6'), 'scenario': '场景1-1-3-6'})
    all_results.append(result1_1_3_6)
    print(f"\n权重矩阵:\n{weight_matrix1_1_3_3.round(2)}\n相似性得分: {result1_1_3_6['similarity_score']:.2f}")



    # 输出高相似性矩阵对
    high_similarity = filter_high_similarity_pairs(all_results)
    if high_similarity:
        print("\n\n相似性得分大于0.8的矩阵对:")
        for pair in high_similarity:
            print(f"{pair['scenario']}: {pair['matrix_pair'][0]}, {pair['matrix_pair'][1]} "
                  f"(相似性得分: {pair['similarity_score']:.2f})")
    else:
        print("\n\n没有相似性得分大于0.8的矩阵对")

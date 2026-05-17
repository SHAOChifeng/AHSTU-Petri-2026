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

    # 场景1_1：权重矩阵（A=2/3, D=0）
    print("\n场景2：权重矩阵")
    scores1_1 = {'A': 2 / 3, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_1 = generate_weight_matrix(operations, scores1_1)
    result1_1 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_1'], weight_matrix1_1)
    result1_1.update({'matrix_pair': ('matrix_1', 'matrix_1'), 'scenario': '场景1_1'})
    all_results.append(result1_1)
    print(f"\n权重矩阵:\n{weight_matrix1_1.round(2)}\n相似性得分: {result1_1['similarity_score']:.2f}")

    # 场景1_2：权重矩阵（D的相似性为0）
    print("场景1_2：权重矩阵")
    scores1_2 = {op: 0 if op == 'D' else 1 for op in operations}
    weight_matrix1_2 = generate_weight_matrix(operations, scores1_2)
    result1_2 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_3'], weight_matrix1_2)
    result1_2.update({'matrix_pair': ('matrix_1', 'matrix_3'), 'scenario': '场景1_2'})
    all_results.append(result1_2)
    print(f"\n权重矩阵:\n{weight_matrix1_2.round(2)}\n相似性得分: {result1_2['similarity_score']:.2f}")

    # 场景1_3：权重矩阵（A=3/7, C=1/3）
    print("\n场景1_3：权重矩阵")
    scores1_3 = {'A': 3/7, 'B': 1, 'C': 1/3, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix1_3 = generate_weight_matrix(operations, scores1_3)
    result1_3 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_2'], weight_matrix1_3)
    result1_3.update({'matrix_pair': ('matrix_1', 'matrix_2'), 'scenario': '场景1_3'})
    all_results.append(result1_3)
    print(f"\n权重矩阵:\n{weight_matrix1_3.round(2)}\n相似性得分: {result1_3['similarity_score']:.2f}")

    # 场景1_4：权重矩阵（A=1/4, D=1/3,F=1/3）
    print("\n场景1_4：权重矩阵")
    scores1_4 = {'A': 1/4, 'B': 1, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix1_4 = generate_weight_matrix(operations, scores1_4)
    result1_4 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_4'], weight_matrix1_4)
    result1_4.update({'matrix_pair': ('matrix_1', 'matrix_4'), 'scenario': '场景1_4'})
    all_results.append(result1_4)
    print(f"\n权重矩阵:\n{weight_matrix1_4.round(2)}\n相似性得分: {result1_4['similarity_score']:.2f}")

    # 场景2_1：权重矩阵（A=2/3, D=0）
    print("\n场景2_1：权重矩阵")
    scores2_1 = {'A': 2 / 3, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix2_1 = generate_weight_matrix(operations, scores2_1)
    result2_1 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_7'], weight_matrix2_1)
    result2_1.update({'matrix_pair': ('matrix_2', 'matrix_7'), 'scenario': '场景2_1'})
    all_results.append(result2_1)
    print(f"\n权重矩阵:\n{weight_matrix2_1.round(2)}\n相似性得分: {result2_1['similarity_score']:.2f}")

    # 场景2_2：权重矩阵（ D=1/3）
    print("\n场景2_2：权重矩阵")
    scores2_2 = {'A': 1, 'B': 1, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix2_2 = generate_weight_matrix(operations, scores2_2)
    result2_2 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_4'], weight_matrix2_2)
    result2_2.update({'matrix_pair': ('matrix_2', 'matrix_4'), 'scenario': '场景2_2'})
    all_results.append(result2_2)
    print(f"\n权重矩阵:\n{weight_matrix2_2.round(2)}\n相似性得分: {result2_2['similarity_score']:.2f}")

    # 场景2_3：权重矩阵（ ）
    print("\n场景2_3：权重矩阵")
    scores2_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix2_3 = generate_weight_matrix(operations, scores2_3)
    result2_3 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_5'], weight_matrix2_3)
    result2_3.update({'matrix_pair': ('matrix_2', 'matrix_5'), 'scenario': '场景2_3'})
    all_results.append(result2_3)
    print(f"\n权重矩阵:\n{weight_matrix2_3.round(2)}\n相似性得分: {result2_3['similarity_score']:.2f}")

    # 场景2_4：权重矩阵（A=2/3）
    print("\n场景2_4：权重矩阵")
    scores2_4 = {'A': 2 / 3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix2_4 = generate_weight_matrix(operations, scores2_4)
    result2_4 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_2'], weight_matrix2_4)
    result2_4.update({'matrix_pair': ('matrix_2', 'matrix_2'), 'scenario': '场景2_4'})
    all_results.append(result2_4)
    print(f"\n权重矩阵:\n{weight_matrix2_4.round(2)}\n相似性得分: {result2_4['similarity_score']:.2f}")

    # 场景3_1：权重矩阵（A=2/3, F=1/3）
    print("\n场景3_1：权重矩阵")
    scores3_1 = {'A': 2 / 3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix3_1 = generate_weight_matrix(operations, scores3_1)
    result3_1 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_3'], weight_matrix3_1)
    result3_1.update({'matrix_pair': ('matrix_3', 'matrix_3'), 'scenario': '场景3_1'})
    all_results.append(result3_1)
    print(f"\n权重矩阵:\n{weight_matrix3_1.round(2)}\n相似性得分: {result3_1['similarity_score']:.2f}")

    # 场景3_2：权重矩阵（A=3/7,D= 1/3）
    print("\n场景3_2：权重矩阵")
    scores3_2 = {'A': 3 / 7, 'B': 1, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix3_2 = generate_weight_matrix(operations, scores3_2)
    result3_2 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_6'], weight_matrix3_2)
    result3_2.update({'matrix_pair': ('matrix_3', 'matrix_6'), 'scenario': '场景3_2'})
    all_results.append(result3_2)
    print(f"\n权重矩阵:\n{weight_matrix3_2.round(2)}\n相似性得分: {result3_2['similarity_score']:.2f}")

    # 场景3_3：权重矩阵（A=2/3）
    print("\n场景3_3：权重矩阵")
    scores3_3 = {'A': 2 / 3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix3_3 = generate_weight_matrix(operations, scores3_3)
    result3_3 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_3'], weight_matrix3_3)
    result3_3.update({'matrix_pair': ('matrix_3', 'matrix_3'), 'scenario': '场景3_3'})
    all_results.append(result3_3)
    print(f"\n权重矩阵:\n{weight_matrix3_3.round(2)}\n相似性得分: {result3_3['similarity_score']:.2f}")

    # 场景3_4：权重矩阵（ ）
    print("\n场景3_4：权重矩阵")
    scores3_4 = {'A':1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix3_4 = generate_weight_matrix(operations, scores3_4)
    result3_4 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_5'], weight_matrix3_4)
    result3_4.update({'matrix_pair': ('matrix_3', 'matrix_5'), 'scenario': '场景3_4'})
    all_results.append(result3_4)
    print(f"\n权重矩阵:\n{weight_matrix3_4.round(2)}\n相似性得分: {result3_4['similarity_score']:.2f}")

    # 场景4_1：权重矩阵（A=2/3,D=0 ）
    print("\n场景4_1：权重矩阵")
    scores4_1 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix4_1 = generate_weight_matrix(operations, scores4_1)
    result4_1 = process_workflow_comparison(
        matrix_dict['matrix_4'], matrix_dict['matrix_4'], weight_matrix4_1)
    result4_1.update({'matrix_pair': ('matrix_4', 'matrix_4'), 'scenario': '场景4_1'})
    all_results.append(result4_1)
    print(f"\n权重矩阵:\n{weight_matrix4_1.round(2)}\n相似性得分: {result4_1['similarity_score']:.2f}")

    # 场景4_2：权重矩阵（ ）
    print("\n场景4_2：权重矩阵")
    scores4_2 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix4_2 = generate_weight_matrix(operations, scores4_2)
    result4_2 = process_workflow_comparison(
        matrix_dict['matrix_4'], matrix_dict['matrix_7'], weight_matrix4_2)
    result4_2.update({'matrix_pair': ('matrix_4', 'matrix_7'), 'scenario': '场景4_2'})
    all_results.append(result4_2)
    print(f"\n权重矩阵:\n{weight_matrix4_2.round(2)}\n相似性得分: {result4_2['similarity_score']:.2f}")

    # 场景4_3：权重矩阵（A=2/3,C=1/3,D=0,F=1/3）
    print("\n场景4_3：权重矩阵")
    scores4_3 = {'A': 2/3, 'B': 1, 'C': 1/3, 'D': 0, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix4_3 = generate_weight_matrix(operations, scores4_3)
    result4_3 = process_workflow_comparison(
        matrix_dict['matrix_4'], matrix_dict['matrix_1'], weight_matrix4_3)
    result4_3.update({'matrix_pair': ('matrix_4', 'matrix_1'), 'scenario': '场景4_3'})
    all_results.append(result4_3)
    print(f"\n权重矩阵:\n{weight_matrix4_3.round(2)}\n相似性得分: {result4_3['similarity_score']:.2f}")

    # 场景4_4：权重矩阵（ F=1/3,E=0）
    print("\n场景4_4：权重矩阵")
    scores4_4 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 1/3, 'G': 1}
    weight_matrix4_4 = generate_weight_matrix(operations, scores4_4)
    result4_4 = process_workflow_comparison(
        matrix_dict['matrix_4'], matrix_dict['matrix_1'], weight_matrix4_4)
    result4_4.update({'matrix_pair': ('matrix_4', 'matrix_1'), 'scenario': '场景4_4'})
    all_results.append(result4_4)
    print(f"\n权重矩阵:\n{weight_matrix4_4.round(2)}\n相似性得分: {result4_4['similarity_score']:.2f}")

    # 场景5_1：权重矩阵（A=3/7,C=1/3,B=0,F=2/3）
    print("\n场景5_1：权重矩阵")
    scores5_1 = {'A': 3 / 7, 'B': 0, 'C': 1 / 3, 'D': 1, 'E': 1, 'F': 2 / 3, 'G': 1}
    weight_matrix5_1 = generate_weight_matrix(operations, scores5_1)
    result5_1 = process_workflow_comparison(
        matrix_dict['matrix_5'], matrix_dict['matrix_5'], weight_matrix5_1)
    result5_1.update({'matrix_pair': ('matrix_5', 'matrix_5'), 'scenario': '场景5_1'})
    all_results.append(result5_1)
    print(f"\n权重矩阵:\n{weight_matrix5_1.round(2)}\n相似性得分: {result5_1['similarity_score']:.2f}")


    # 场景5_2：权重矩阵（A=2/3,D=0,E=0）
    print("\n场景5_2：权重矩阵")
    scores5_2 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 0, 'E': 0, 'F': 1, 'G': 1}
    weight_matrix5_2 = generate_weight_matrix(operations, scores5_2)
    result5_2 = process_workflow_comparison(
        matrix_dict['matrix_5'], matrix_dict['matrix_3'], weight_matrix5_2)
    result5_2.update({'matrix_pair': ('matrix_5', 'matrix_3'), 'scenario': '场景5_2'})
    all_results.append(result5_2)
    print(f"\n权重矩阵:\n{weight_matrix5_2.round(2)}\n相似性得分: {result5_2['similarity_score']:.2f}")

    # 场景5_3：权重矩阵（B=0,C=1/3,D=1/3）
    print("\n场景5_3：权重矩阵")
    scores5_3 = {'A':1, 'B': 0, 'C': 1 / 3, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix5_3 = generate_weight_matrix(operations, scores5_3)
    result5_3 = process_workflow_comparison(
        matrix_dict['matrix_5'], matrix_dict['matrix_6'], weight_matrix5_3)
    result5_3.update({'matrix_pair': ('matrix_5', 'matrix_6'), 'scenario': '场景5_3'})
    all_results.append(result5_3)
    print(f"\n权重矩阵:\n{weight_matrix5_3.round(2)}\n相似性得分: {result5_3['similarity_score']:.2f}")

    # 场景5_4：权重矩阵（）
    print("\n场景5_4：权重矩阵")
    scores5_4 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix5_4 = generate_weight_matrix(operations, scores5_4)
    result5_4 = process_workflow_comparison(
        matrix_dict['matrix_5'], matrix_dict['matrix_4'], weight_matrix5_4)
    result5_4.update({'matrix_pair': ('matrix_5', 'matrix_4'), 'scenario': '场景5_4'})
    all_results.append(result5_4)
    print(f"\n权重矩阵:\n{weight_matrix5_4.round(2)}\n相似性得分: {result5_4['similarity_score']:.2f}")

    # 场景6_1：权重矩阵（D=0）
    print("\n场景6_1：权重矩阵")
    scores6_1 = {'A': 1, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix6_1 = generate_weight_matrix(operations, scores6_1)
    result6_1 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_2'], weight_matrix6_1)
    result6_1.update({'matrix_pair': ('matrix_6', 'matrix_2'), 'scenario': '场景6_1'})
    all_results.append(result6_1)
    print(f"\n权重矩阵:\n{weight_matrix6_1.round(2)}\n相似性得分: {result6_1['similarity_score']:.2f}")

    # 场景6_2：权重矩阵（A=1/4,C=0,F=1/4）
    print("\n场景6_2：权重矩阵")
    scores6_2 = {'A': 1/4, 'B': 1, 'C': 0, 'D': 1, 'E': 1, 'F': 1/4, 'G': 1}
    weight_matrix6_2 = generate_weight_matrix(operations, scores6_2)
    result6_2 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_3'], weight_matrix6_2)
    result6_2.update({'matrix_pair': ('matrix_6', 'matrix_3'), 'scenario': '场景6_2'})
    all_results.append(result6_2)
    print(f"\n权重矩阵:\n{weight_matrix6_2.round(2)}\n相似性得分: {result6_2['similarity_score']:.2f}")

    # 场景6_3：权重矩阵（D=1/3）
    print("\n场景6_3：权重矩阵")
    scores6_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix6_3 = generate_weight_matrix(operations, scores6_3)
    result6_3 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_4'], weight_matrix6_3)
    result6_3.update({'matrix_pair': ('matrix_6', 'matrix_4'), 'scenario': '场景6_3'})
    all_results.append(result6_3)
    print(f"\n权重矩阵:\n{weight_matrix6_3.round(2)}\n相似性得分: {result6_3['similarity_score']:.2f}")

    # 场景6_4：权重矩阵（A=2/3）
    print("\n场景6_4：权重矩阵")
    scores6_4 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix6_4 = generate_weight_matrix(operations, scores6_4)
    result6_4 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_6'], weight_matrix6_4)
    result6_4.update({'matrix_pair': ('matrix_6', 'matrix_6'), 'scenario': '场景6_4'})
    all_results.append(result6_4)
    print(f"\n权重矩阵:\n{weight_matrix6_4.round(2)}\n相似性得分: {result6_4['similarity_score']:.2f}")

    # 场景7_1：权重矩阵（A=1/4,E=0,F=1/4）
    print("\n场景7_1：权重矩阵")
    scores7_1 = {'A': 1 / 4, 'B': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 1/4, 'G': 1}
    weight_matrix7_1 = generate_weight_matrix(operations, scores7_1)
    result7_1 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_1'], weight_matrix7_1)
    result7_1.update({'matrix_pair': ('matrix_7', 'matrix_1'), 'scenario': '场景7_1'})
    all_results.append(result7_1)
    print(f"\n权重矩阵:\n{weight_matrix7_1.round(2)}\n相似性得分: {result7_1['similarity_score']:.2f}")

    # 场景7_2：权重矩阵（C=1/3）
    print("\n场景7_2：权重矩阵")
    scores7_2 = {'A': 1, 'B': 1, 'C': 1/3, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix7_2 = generate_weight_matrix(operations, scores7_2)
    result7_2 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_4'], weight_matrix7_2)
    result7_2.update({'matrix_pair': ('matrix_7', 'matrix_4'), 'scenario': '场景7_2'})
    all_results.append(result7_2)
    print(f"\n权重矩阵:\n{weight_matrix7_2.round(2)}\n相似性得分: {result7_2['similarity_score']:.2f}")

    # 场景7_3：权重矩阵（A=3/7,B=0）
    print("\n场景7_3：权重矩阵")
    scores7_3 = {'A': 3 / 7, 'B': 0, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix7_3 = generate_weight_matrix(operations, scores7_3)
    result7_3 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_5'], weight_matrix7_3)
    result7_3.update({'matrix_pair': ('matrix_7', 'matrix_5'), 'scenario': '场景7_3'})
    all_results.append(result7_3)
    print(f"\n权重矩阵:\n{weight_matrix7_3.round(2)}\n相似性得分: {result7_3['similarity_score']:.2f}")

    # 场景7_4：权重矩阵（A=3/7,D=0）
    print("\n场景7_4：权重矩阵")
    scores7_4 = {'A': 3 / 7, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix7_4 = generate_weight_matrix(operations, scores7_4)
    result7_4 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_7'], weight_matrix7_4)
    result7_4.update({'matrix_pair': ('matrix_7', 'matrix_7'), 'scenario': '场景7_4'})
    all_results.append(result7_4)
    print(f"\n权重矩阵:\n{weight_matrix7_4.round(2)}\n相似性得分: {result7_4['similarity_score']:.2f}")

    # 场景8_1：权重矩阵（A=2/3,B=0,F=1/3）
    print("\n场景8_1：权重矩阵")
    scores8_1 = {'A': 2 / 3, 'B': 0, 'C': 1, 'D': 1, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix8_1 = generate_weight_matrix(operations, scores8_1)
    result8_1 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_2'], weight_matrix8_1)
    result8_1.update({'matrix_pair': ('matrix_1', 'matrix_2'), 'scenario': '场景8_1'})
    all_results.append(result8_1)
    print(f"\n权重矩阵:\n{weight_matrix8_1.round(2)}\n相似性得分: {result8_1['similarity_score']:.2f}")

    # 场景8_2：权重矩阵（A=3/7,C=0）
    print("\n场景8_2：权重矩阵")
    scores8_2 = {'A': 3 / 7, 'B': 1, 'C': 0, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix8_2 = generate_weight_matrix(operations, scores8_2)
    result8_2 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_4'], weight_matrix8_2)
    result8_2.update({'matrix_pair': ('matrix_1', 'matrix_4'), 'scenario': '场景8_2'})
    all_results.append(result8_2)
    print(f"\n权重矩阵:\n{weight_matrix8_2.round(2)}\n相似性得分: {result8_2['similarity_score']:.2f}")

    # 场景8_3：权重矩阵（ ）
    print("\n场景8_3：权重矩阵")
    scores8_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix8_3 = generate_weight_matrix(operations, scores8_3)
    result8_3 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_5'], weight_matrix8_3)
    result8_3.update({'matrix_pair': ('matrix_1', 'matrix_5'), 'scenario': '场景8_3'})
    all_results.append(result8_3)
    print(f"\n权重矩阵:\n{weight_matrix8_3.round(2)}\n相似性得分: {result8_3['similarity_score']:.2f}")

    # 场景8_4：权重矩阵（A=3/7,D=1/3,F=1/4）
    print("\n场景8_4：权重矩阵")
    scores8_4 = {'A': 3 / 7, 'B': 1, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1/4, 'G': 1}
    weight_matrix8_4 = generate_weight_matrix(operations, scores8_4)
    result8_4 = process_workflow_comparison(
        matrix_dict['matrix_1'], matrix_dict['matrix_6'], weight_matrix8_4)
    result8_4.update({'matrix_pair': ('matrix_1', 'matrix_6'), 'scenario': '场景8_4'})
    all_results.append(result8_4)
    print(f"\n权重矩阵:\n{weight_matrix8_4.round(2)}\n相似性得分: {result8_4['similarity_score']:.2f}")

    # 场景9_1：权重矩阵（D=1/3,E=0）
    print("\n场景9_1：权重矩阵")
    scores9_1 = {'A': 1, 'B': 1, 'C': 1, 'D': 1 / 3, 'E': 0, 'F': 1, 'G': 1}
    weight_matrix9_1 = generate_weight_matrix(operations, scores9_1)
    result9_1 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_1'], weight_matrix9_1)
    result9_1.update({'matrix_pair': ('matrix_6', 'matrix_1'), 'scenario': '场景9_1'})
    all_results.append(result9_1)
    print(f"\n权重矩阵:\n{weight_matrix9_1.round(2)}\n相似性得分: {result9_1['similarity_score']:.2f}")

    # 场景9_2：权重矩阵（A=2/3,C=0,F=1/4）
    print("\n场景9_2：权重矩阵")
    scores9_2 = {'A': 2/3, 'B': 1, 'C': 0, 'D': 1, 'E': 1, 'F': 1/4, 'G': 1}
    weight_matrix9_2 = generate_weight_matrix(operations, scores9_2)
    result9_2 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_7'], weight_matrix9_2)
    result8_4.update({'matrix_pair': ('matrix_6', 'matrix_7'), 'scenario': '场景9_2'})
    all_results.append(result9_2)
    print(f"\n权重矩阵:\n{weight_matrix9_2.round(2)}\n相似性得分: {result9_2['similarity_score']:.2f}")

    # 场景9_3：权重矩阵（F=1/3）
    print("\n场景9_3：权重矩阵")
    scores9_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1 / 3, 'G': 1}
    weight_matrix9_3 = generate_weight_matrix(operations, scores9_3)
    result9_3 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_2'], weight_matrix9_3)
    result9_3.update({'matrix_pair': ('matrix_6', 'matrix_2'), 'scenario': '场景9_3'})
    all_results.append(result9_3)
    print(f"\n权重矩阵:\n{weight_matrix9_3.round(2)}\n相似性得分: {result9_3['similarity_score']:.2f}")

    # 场景9_4：权重矩阵（B=0,E=0,F=1/3）
    print("\n场景9_4：权重矩阵")
    scores9_4 = {'A': 1, 'B': 0, 'C': 1, 'D': 1, 'E': 0, 'F': 1/3, 'G': 1}
    weight_matrix9_4 = generate_weight_matrix(operations, scores9_4)
    result9_4 = process_workflow_comparison(
        matrix_dict['matrix_6'], matrix_dict['matrix_5'], weight_matrix9_4)
    result9_4.update({'matrix_pair': ('matrix_6', 'matrix_5'), 'scenario': '场景9_4'})
    all_results.append(result9_4)
    print(f"\n权重矩阵:\n{weight_matrix9_4.round(2)}\n相似性得分: {result9_4['similarity_score']:.2f}")

    # 场景10_1：权重矩阵（A=0.11,B=0,C=0,F=1/3）
    print("\n场景10_1：权重矩阵")
    scores10_1 = {'A': 0.11, 'B': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 1 / 3, 'G': 1}
    weight_matrix10_1 = generate_weight_matrix(operations, scores10_1)
    result10_1 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_1'], weight_matrix10_1)
    result10_1.update({'matrix_pair': ('matrix_2', 'matrix_1'), 'scenario': '场景10_1'})
    all_results.append(result10_1)
    print(f"\n权重矩阵:\n{weight_matrix10_1.round(2)}\n相似性得分: {result10_1['similarity_score']:.2f}")

    # 场景10_2：权重矩阵（B=1/3）
    print("\n场景10_2：权重矩阵")
    scores10_2 = {'A': 1, 'B': 1/3, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix10_2 = generate_weight_matrix(operations, scores10_2)
    result10_2 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_5'], weight_matrix10_2)
    result10_2.update({'matrix_pair': ('matrix_2', 'matrix_5'), 'scenario': '场景10_2'})
    all_results.append(result10_2)
    print(f"\n权重矩阵:\n{weight_matrix10_2.round(2)}\n相似性得分: {result10_2['similarity_score']:.2f}")

    # 场景10_3：权重矩阵（B=1/3）
    print("\n场景10_3：权重矩阵")
    scores10_3 = {'A': 1, 'B': 1/3, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix10_3 = generate_weight_matrix(operations, scores10_3)
    result10_3 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_6'], weight_matrix10_3)
    result10_3.update({'matrix_pair': ('matrix_2', 'matrix_6'), 'scenario': '场景10_3'})
    all_results.append(result10_3)
    print(f"\n权重矩阵:\n{weight_matrix10_3.round(2)}\n相似性得分: {result10_3['similarity_score']:.2f}")

    # 场景10_4：权重矩阵（B=1/3,A=2/3）
    print("\n场景10_4：权重矩阵")
    scores10_4 = {'A': 2/3, 'B': 1/3, 'C': 1, 'D': 1, 'E': 1, 'F':1, 'G': 1}
    weight_matrix10_4 = generate_weight_matrix(operations, scores10_4)
    result10_4 = process_workflow_comparison(
        matrix_dict['matrix_2'], matrix_dict['matrix_3'], weight_matrix10_4)
    result10_4.update({'matrix_pair': ('matrix_2', 'matrix_3'), 'scenario': '场景10_4'})
    all_results.append(result10_4)
    print(f"\n权重矩阵:\n{weight_matrix10_4.round(2)}\n相似性得分: {result10_4['similarity_score']:.2f}")

    # 场景11_1：权重矩阵（A=1/4,D=0,F=1/4）
    print("\n场景10_4：权重矩阵")
    scores11_1 = {'A': 1/4, 'B': 1, 'C': 1, 'D': 0, 'E': 1, 'F': 1/4, 'G': 1}
    weight_matrix11_1 = generate_weight_matrix(operations, scores11_1)
    result11_1 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_1'], weight_matrix11_1)
    result11_1.update({'matrix_pair': ('matrix_7', 'matrix_1'), 'scenario': '场景11_1'})
    all_results.append(result11_1)
    print(f"\n权重矩阵:\n{weight_matrix11_1.round(2)}\n相似性得分: {result11_1['similarity_score']:.2f}")

    # 场景11_2：权重矩阵（B=1/3,A=2/3）
    print("\n场景11_2：权重矩阵")
    scores11_2 = {'A': 2 / 3, 'B': 1 / 3, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix11_2 = generate_weight_matrix(operations, scores11_2)
    result11_2 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_2'], weight_matrix11_2)
    result11_2.update({'matrix_pair': ('matrix_7', 'matrix_2'), 'scenario': '场景11_2'})
    all_results.append(result11_2)
    print(f"\n权重矩阵:\n{weight_matrix11_2.round(2)}\n相似性得分: {result11_2['similarity_score']:.2f}")

    # 场景11_3：权重矩阵（F=2/3）
    print("\n场景11_3：权重矩阵")
    scores11_3 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 2/3, 'G': 1}
    weight_matrix11_3 = generate_weight_matrix(operations, scores11_3)
    result11_3 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_1'], weight_matrix11_3)
    result11_3.update({'matrix_pair': ('matrix_7', 'matrix_1'), 'scenario': '场景11_3'})
    all_results.append(result11_3)
    print(f"\n权重矩阵:\n{weight_matrix11_3.round(2)}\n相似性得分: {result11_3['similarity_score']:.2f}")

    # 场景11_4：权重矩阵（B=1/3,E=0）
    print("\n场景11_4：权重矩阵")
    scores11_4 = {'A': 1, 'B': 1 / 3, 'C': 1, 'D': 1, 'E': 0, 'F': 1, 'G': 1}
    weight_matrix11_4 = generate_weight_matrix(operations, scores11_4)
    result11_4 = process_workflow_comparison(
        matrix_dict['matrix_7'], matrix_dict['matrix_4'], weight_matrix11_4)
    result11_4.update({'matrix_pair': ('matrix_7', 'matrix_4'), 'scenario': '场景11_4'})
    all_results.append(result11_4)
    print(f"\n权重矩阵:\n{weight_matrix11_4.round(2)}\n相似性得分: {result11_4['similarity_score']:.2f}")

    # 场景12_1：权重矩阵（ ）
    print("\n场景12_1：权重矩阵")
    scores12_1 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix12_1 = generate_weight_matrix(operations, scores12_1)
    result12_1 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_7'], weight_matrix12_1)
    result12_1.update({'matrix_pair': ('matrix_3', 'matrix_7'), 'scenario': '场景12_1'})
    all_results.append(result12_1)
    print(f"\n权重矩阵:\n{weight_matrix12_1.round(2)}\n相似性得分: {result12_1['similarity_score']:.2f}")

    # 场景12_2：权重矩阵（B=1/3,D=1/3,A=1/4）
    print("\n场景12_2：权重矩阵")
    scores12_2 = {'A': 1/4, 'B': 1 / 3, 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix12_2 = generate_weight_matrix(operations, scores12_2)
    result12_2 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_1'], weight_matrix12_2)
    result12_2.update({'matrix_pair': ('matrix_3', 'matrix_1'), 'scenario': '场景12_2'})
    all_results.append(result12_2)
    print(f"\n权重矩阵:\n{weight_matrix12_2.round(2)}\n相似性得分: {result12_2['similarity_score']:.2f}")

    # 场景12_3：权重矩阵（B=1/3）
    print("\n场景12_3：权重矩阵")
    scores12_3 = {'A': 1, 'B': 1 / 3, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
    weight_matrix12_3 = generate_weight_matrix(operations, scores12_3)
    result12_3 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_5'], weight_matrix12_3)
    result12_3.update({'matrix_pair': ('matrix_3', 'matrix_5'), 'scenario': '场景12_3'})
    all_results.append(result12_3)
    print(f"\n权重矩阵:\n{weight_matrix12_3.round(2)}\n相似性得分: {result12_3['similarity_score']:.2f}")

    # 场景12_4：权重矩阵（B=1/3,F=1/3）
    print("\n场景12_4：权重矩阵")
    scores12_4 = {'A': 1, 'B': 1 / 3, 'C': 1, 'D': 1, 'E': 1, 'F': 1/3, 'G': 1}
    weight_matrix12_4 = generate_weight_matrix(operations, scores12_4)
    result12_4 = process_workflow_comparison(
        matrix_dict['matrix_3'], matrix_dict['matrix_2'], weight_matrix12_4)
    result12_4.update({'matrix_pair': ('matrix_3', 'matrix_2'), 'scenario': '场景12_4'})
    all_results.append(result12_4)
    print(f"\n权重矩阵:\n{weight_matrix12_4.round(2)}\n相似性得分: {result12_4['similarity_score']:.2f}")









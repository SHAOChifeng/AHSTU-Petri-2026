import numpy as np
import pandas as pd


def compare_matrices(matrix_a, matrix_b):
    """比较两个矩阵的对应元素，生成比较矩阵"""
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("两个矩阵的形状必须相同")

    result = np.where(matrix_a == matrix_b, 1, 0)
    np.fill_diagonal(result, 0)
    return result


def generate_weight_matrix(operations, special_op='D'):
    """
    生成基于操作相似性的权重矩阵

    参数:
    operations (list): 操作名称列表，例如 ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    special_op (str): 特殊操作名称，默认是 'D'，其相似性得分为0
    """
    # 定义操作的相似性得分（special_op为0，其余为1）
    similarity_scores = {op: 0 if op == special_op else 1 for op in operations}

    n = len(operations)
    weight_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                op_i = operations[i]
                op_j = operations[j]
                weight_matrix[i, j] = (similarity_scores[op_i] + similarity_scores[op_j]) / 2

    return pd.DataFrame(weight_matrix, index=operations, columns=operations)


def calculate_weighted_sum(comparison_matrix, weight_matrix):
    """计算比较矩阵的加权和"""
    if weight_matrix.shape != comparison_matrix.shape:
        raise ValueError("权重矩阵的形状必须与比较矩阵相同")

    return np.sum(comparison_matrix * weight_matrix)


def calculate_similarity_score(weighted_sum, max_possible_sum):
    """计算最终相似性得分（0-100%）"""
    if max_possible_sum == 0:
        return 0  # 避免除以零
    return (weighted_sum / max_possible_sum) * 100


# 主函数：整合所有流程
def process_workflow_comparison(matrix_a, matrix_b, operations, special_op='D'):
    """
    整合工作流程比较的完整流程

    参数:
    matrix_a, matrix_b (np.array): 要比较的两个矩阵
    operations (list): 操作名称列表
    special_op (str): 特殊操作名称

    返回:
    dict: 包含所有中间结果和最终得分的字典
    """
    # 1. 比较矩阵
    comparison_matrix = compare_matrices(matrix_a, matrix_b)

    # 2. 生成权重矩阵
    weight_df = generate_weight_matrix(operations, special_op)
    weight_matrix = weight_df.values  # 转换为numpy数组用于计算

    # 3. 计算加权和
    weighted_sum = calculate_weighted_sum(comparison_matrix, weight_matrix)

    # 4. 计算最终相似性得分
    similarity_score =weighted_sum/42

    return {
        'comparison_matrix': comparison_matrix,
        'weight_matrix_df': weight_df,
        'weighted_sum': weighted_sum,
        'similarity_score': similarity_score
    }


# 示例使用
if __name__ == "__main__":
    # 定义操作列表
    operations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    # 创建示例矩阵（7x7，对应7个操作）
    matrix_1 = np.array([['-', 1, 1, 1, 1, 1, 1],
                    [2, '-', 1, 1, 1, 1, 1],
                    [2, 2, '-', 1, 1, 1, 1],
                    [2, 2, 2, '-', 1, 1, 1],
                    [2, 2, 2, 2, '-', 1, 1],
                    [2, 2, 2, 2, 2, '-', 1],
                    [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    matrix_3 = np.array([['-', 4, 1, 1, 4, 1, 1],
                    [4, '-', 4, 4, 1, 1, 1],
                    [2, 4, '-', 1, 4, 1, 1],
                    [2, 4, 2, '-', 4, 1, 1],
                    [4, 2, 4, 4, '-', 1, 1],
                    [2, 2, 2, 2, 2, '-', 1],
                    [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    # 处理工作流程比较
    result1_3 = process_workflow_comparison(matrix_1, matrix_3, operations)

    # 打印结果
    print("矩阵 1:")
    print(matrix_1)
    print("\n矩阵 3:")
    print(matrix_3)
    print("\n比较矩阵:")
    print(result1_3['comparison_matrix'])
    print("\n权重矩阵:")
    print(result1_3['weight_matrix_df'].round(2))
    print(f"\n加权和: {result1_3['weighted_sum']:.2f}")
    print(f"最终相似性得分: {result1_3['similarity_score']:.2f}")

    matrix_1 = np.array([['-', 1, 1, 1, 1, 1, 1],
                         [2, '-', 1, 1, 1, 1, 1],
                         [2, 2, '-', 1, 1, 1, 1],
                         [2, 2, 2, '-', 1, 1, 1],
                         [2, 2, 2, 2, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    matrix_2 = np.array([['-', 2, 1, 1, 1, 1, 1],
                         [1, '-', 1, 1, 1, 1, 1],
                         [2, 2, '-', 1, 1, 1, 1],
                         [2, 2, 2, '-', 1, 1, 1],
                         [2, 2, 2, 2, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    matrix_3 = np.array([['-', 4, 1, 1, 4, 1, 1],
                         [4, '-', 4, 4, 1, 1, 1],
                         [2, 4, '-', 1, 4, 1, 1],
                         [2, 4, 2, '-', 4, 1, 1],
                         [4, 2, 4, 4, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    matrix_5 = np.array([['-', 1, 1, 1, 1, 1, 1],
                         [2, '-', 2, 2, 1, 1, 1],
                         [2, 1, '-', 1, 1, 1, 1],
                         [2, 1, 2, '-', 1, 1, 1],
                         [2, 2, 2, 2, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)

    matrix_7 = np.array([['-', 1, 1, 1, 1, 1, 1],
                         [2, '-', 1, 1, 1, 1, 1],
                         [2, 2, '-', 1, 4, 1, 1],
                         [2, 2, 2, '-', 4, 1, 1],
                         [2, 2, 4, 4, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)

    matrix_6 = np.array([['-', 2, 1, 1, 2, 1, 1],
                         [1, '-', 1, 1, 1, 1, 1],
                         [2, 2, '-', 1, 2, 1, 1],
                         [2, 2, 2, '-', 2, 1, 1],
                         [1, 2, 1, 1, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)
    matrix_4 = np.array([['-', 1, 1, 1, 1, 1, 1],
                         [2, '-', 1, 1, 1, 1, 1],
                         [2, 2, '-', 1, 2, 1, 1],
                         [2, 2, 2, '-', 2, 1, 1],
                         [2, 2, 1, 1, '-', 1, 1],
                         [2, 2, 2, 2, 2, '-', 1],
                         [2, 2, 2, 2, 2, 2, '-']], dtype=object)

    result1_5 = process_workflow_comparison(matrix_1, matrix_5, operations)
    # 打印结果

    print("\n比较矩阵:")
    print(result1_5['comparison_matrix'])



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

        # 场景1-5：自定义权重矩阵（参5-参1可选）
        print("\n场景1-5：使用自定义权重矩阵")
        custom_scores1_5 = {'A': 3/4, 'B': 1/3, 'C': 1, 'D':1, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix1_5 = generate_weight_matrix(operations, custom_scores1_5)
        result1_5 = process_workflow_comparison(
            matrix_dict['matrix_1'], matrix_dict['matrix_5'], weight_matrix1_5)
        result1_5.update({'matrix_pair': ('matrix_1', 'matrix_5'), 'scenario': '场景1-5'})
        all_results.append(result1_5)
        print(f"\n权重矩阵:\n{weight_matrix1_5.round(2)}\n相似性得分: {result1_5['similarity_score']:.2f}")

        # 场景1-5：自定义权重矩阵（参5-参1可选）
        print("\n场景1-5：使用自定义权重矩阵")
        custom_scores1_5 = {'A': 1, 'B': 1/3, 'C': 2/3, 'D':1, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix1_5 = generate_weight_matrix(operations, custom_scores1_5)
        result1_5 = process_workflow_comparison(
            matrix_dict['matrix_1'], matrix_dict['matrix_5'], weight_matrix1_5)
        result1_5.update({'matrix_pair': ('matrix_1', 'matrix_5'), 'scenario': '场景1-5'})
        all_results.append(result1_5)
        print(f"\n权重矩阵:\n{weight_matrix1_5.round(2)}\n相似性得分: {result1_5['similarity_score']:.2f}")

        # 场景1-5：自定义权重矩阵（参5-参1可选）
        print("\n场景1-5：使用自定义权重矩阵")
        custom_scores1_5 = {'A': 1, 'B': 1/3, 'C': 1, 'D':1, 'E': 1, 'F': 5/6, 'G': 1}
        weight_matrix1_5 = generate_weight_matrix(operations, custom_scores1_5)
        result1_5 = process_workflow_comparison(
            matrix_dict['matrix_1'], matrix_dict['matrix_5'], weight_matrix1_5)
        result1_5.update({'matrix_pair': ('matrix_1', 'matrix_5'), 'scenario': '场景1-5'})
        all_results.append(result1_5)
        print(f"\n权重矩阵:\n{weight_matrix1_5.round(2)}\n相似性得分: {result1_5['similarity_score']:.2f}")



        # 场景1-2：自定义权重矩阵（参1-参2可选）
        print("\n场景1-2：使用自定义权重矩阵")
        custom_scores1_2 = {'A': 1, 'B': 1, 'C': 1/3, 'D':2/3, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix1_2 = generate_weight_matrix(operations, custom_scores1_2)
        result1_2 = process_workflow_comparison(
            matrix_dict['matrix_1'], matrix_dict['matrix_2'], weight_matrix1_2)
        result1_2.update({'matrix_pair': ('matrix_1', 'matrix_2'), 'scenario': '场景1-2'})
        all_results.append(result1_2)
        print(f"\n权重矩阵:\n{weight_matrix1_2.round(2)}\n相似性得分: {result1_2['similarity_score']:.2f}")


        # 场景7-3：自定义权重矩阵（参7-参3可选）
        print("\n场景7-3：使用自定义权重矩阵")
        custom_scores7_3 = {'A': 1, 'B': 1, 'C': 1, 'D':1, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix7_3 = generate_weight_matrix(operations, custom_scores7_3)
        result7_3 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_3'], weight_matrix7_3)
        result7_3.update({'matrix_pair': ('matrix_7', 'matrix_3'), 'scenario': '场景7-3'})
        all_results.append(result7_3)
        print(f"\n权重矩阵:\n{weight_matrix7_3.round(2)}\n相似性得分: {result7_3['similarity_score']:.2f}")





        # 场景7-5：自定义权重矩阵（参7-参5可选）
        print("\n场景7-5：使用自定义权重矩阵")
        custom_scores7_5 = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix7_5 = generate_weight_matrix(operations, custom_scores7_5)
        result7_5 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_5'], weight_matrix7_5)
        result7_5.update({'matrix_pair': ('matrix_7', 'matrix_5'), 'scenario': '场景7-5'})
        all_results.append(result7_5)
        print(f"\n权重矩阵:\n{weight_matrix7_5.round(2)}\n相似性得分: {result7_5['similarity_score']:.2f}")


        # 场景7-7：自定义权重矩阵（参7-参7可选）
        print("\n场景7-7：使用自定义权重矩阵")
        custom_scores7_7 = {'A': 1, 'B': 1, 'C': 2/3, 'D': 2/3, 'E': 1/3, 'F': 1, 'G': 1}
        weight_matrix7_7 = generate_weight_matrix(operations, custom_scores7_7)
        result7_7 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_7'], weight_matrix7_7)
        result7_7.update({'matrix_pair': ('matrix_7', 'matrix_7'), 'scenario': '场景7-7'})
        all_results.append(result7_7)
        print(f"\n权重矩阵:\n{weight_matrix7_7.round(2)}\n相似性得分: {result7_7['similarity_score']:.2f}")

        # 场景7-1：自定义权重矩阵（参7-参1可选）
        print("\n场景7-1：使用自定义权重矩阵")
        custom_scores7_1 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 2/3, 'G': 1}
        weight_matrix7_1 = generate_weight_matrix(operations, custom_scores7_1)
        result7_1 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_1'], weight_matrix7_1)
        result7_1.update({'matrix_pair': ('matrix_7', 'matrix_1'), 'scenario': '场景7-1'})
        all_results.append(result7_1)
        print(f"\n权重矩阵:\n{weight_matrix7_1.round(2)}\n相似性得分: {result7_1['similarity_score']:.2f}")

        # 场景7-2：自定义权重矩阵（参7-参2可选）
        print("\n场景7-2：使用自定义权重矩阵")
        custom_scores7_2 = {'A': 2/3, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix7_2 = generate_weight_matrix(operations, custom_scores7_2)
        result7_2 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_2'], weight_matrix7_2)
        result7_2.update({'matrix_pair': ('matrix_7', 'matrix_2'), 'scenario': '场景7-2'})
        all_results.append(result7_2)
        print(f"\n权重矩阵:\n{weight_matrix7_2.round(2)}\n相似性得分: {result7_2['similarity_score']:.2f}")

        # 场景7-7：自定义权重矩阵（参7-参7可选）
        print("\n场景7-7：使用自定义权重矩阵")
        custom_scores7_7 = {'A': 1/4, 'B': 1 , 'C': 1, 'D': 1/3, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix7_7 = generate_weight_matrix(operations, custom_scores7_7)
        result7_7 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_7'], weight_matrix7_7)
        result7_7.update({'matrix_pair': ('matrix_7', 'matrix_7'), 'scenario': '场景7-7'})
        all_results.append(result7_7)
        print(f"\n权重矩阵:\n{weight_matrix7_7.round(2)}\n相似性得分: {result7_7['similarity_score']:.2f}")

        # 场景7-7：自定义权重矩阵（参7-参7可选）
        print("\n场景7-7：使用自定义权重矩阵")
        custom_scores7_7 = {'A': 2 / 3, 'B': 2 / 3, 'C': 1, 'D': 1 / 3, 'E': 1, 'F': 1, 'G': 1}
        weight_matrix7_7 = generate_weight_matrix(operations, custom_scores7_7)
        result7_7 = process_workflow_comparison(
            matrix_dict['matrix_7'], matrix_dict['matrix_7'], weight_matrix7_7)
        result7_7.update({'matrix_pair': ('matrix_7', 'matrix_7'), 'scenario': '场景7-7'})
        all_results.append(result7_7)
        print(f"\n权重矩阵:\n{weight_matrix7_7.round(2)}\n相似性得分: {result7_7['similarity_score']:.2f}")






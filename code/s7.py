def calculate_OPsimilarity(matrix1, matrix2, operations1, operations2):
    """
    计算两个制造流程操作轮廓相似性

    参数:
    matrix1, matrix2: 表示流程操作关系的二维列表
    operations1, operations2: 表示流程操作名称的列表

    返回:
    float: 操作关系相似性值
    """
    # 检查矩阵维度是否匹配
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])
    if n1 != m1 or n2 != m2 or n1 != n2:
        raise ValueError("矩阵必须是相同大小的方阵")

    # 计算操作并集
    operation_union = set(operations1).union(set(operations2))
    union_count = len(operation_union)

    # 计算分子：相同操作关系的数量
    same_count = 0
    for i in range(n1):
        for j in range(n1):
            if i != j:  # 忽略对角线
                if matrix1[i][j] == matrix2[i][j]:
                    same_count += 1

    # 计算分母：|A∪B| × (|A∪B| - 1)
    denominator = union_count * (union_count - 1) if union_count > 1 else 1

    # 返回相似性值
    return same_count / denominator if denominator != 0 else 0.0

# 示例用法（取消缩进，使其成为独立的代码块）
import numpy as np

if __name__ == "__main__":
    # 示例矩阵
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
    # 其他矩阵定义...（保持不变）

    # 示例操作列表
    operations_1 =operations_2 =operations_3=operations_4 =operations_5=operations_6 =operations_7= ["A", "B", "C", "D", "E", "F", "G"]

    # 计算相似性
    similarity1_1 = calculate_OPsimilarity(matrix_1, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性1-1: {similarity1_1:.2f}")

    similarity1_2 = calculate_OPsimilarity(matrix_1, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性1-2: {similarity1_2:.2f}")

    similarity1_3 = calculate_OPsimilarity(matrix_1, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性1-3: {similarity1_3:.2f}")

    similarity1_4 = calculate_OPsimilarity(matrix_1, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性1-4: {similarity1_4:.2f}")

    similarity2_1 = calculate_OPsimilarity(matrix_2, matrix_7, operations_1, operations_1)
    print(f"操作轮廓相似性2-1: {similarity2_1:.2f}")

    similarity2_2 = calculate_OPsimilarity(matrix_2, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性2-2: {similarity2_2:.2f}")

    similarity2_3 = calculate_OPsimilarity(matrix_2, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性2-3: {similarity2_3:.2f}")

    similarity2_4 = calculate_OPsimilarity(matrix_2, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性2-4: {similarity2_4:.2f}")

    similarity3_1 = calculate_OPsimilarity(matrix_3, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性3-1: {similarity3_1:.2f}")

    similarity3_2 = calculate_OPsimilarity(matrix_3, matrix_6, operations_1, operations_1)
    print(f"操作轮廓相似性3-2: {similarity3_2:.2f}")

    similarity3_3 = calculate_OPsimilarity(matrix_3, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性3-3: {similarity3_3:.2f}")

    similarity3_4 = calculate_OPsimilarity(matrix_3, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性3-4: {similarity3_4:.2f}")

    similarity4_1 = calculate_OPsimilarity(matrix_4, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性4-1: {similarity4_1:.2f}")

    similarity4_2 = calculate_OPsimilarity(matrix_4, matrix_7, operations_1, operations_1)
    print(f"操作轮廓相似性4-2: {similarity4_2:.2f}")

    similarity4_3 = calculate_OPsimilarity(matrix_4, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性4-3: {similarity4_3:.2f}")

    similarity4_4 = calculate_OPsimilarity(matrix_4, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性4-4: {similarity4_4:.2f}")

    similarity5_1 = calculate_OPsimilarity(matrix_5, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性5-1: {similarity5_1:.2f}")

    similarity5_2 = calculate_OPsimilarity(matrix_5, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性5-2: {similarity5_2:.2f}")

    similarity5_3 = calculate_OPsimilarity(matrix_5, matrix_6, operations_1, operations_1)
    print(f"操作轮廓相似性5-3: {similarity5_3:.2f}")

    similarity5_4 = calculate_OPsimilarity(matrix_5, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性5-4: {similarity5_4:.2f}")

    similarity6_1 = calculate_OPsimilarity(matrix_6, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性6-1: {similarity6_1:.2f}")

    similarity6_2 = calculate_OPsimilarity(matrix_6, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性6-2: {similarity6_2:.2f}")

    similarity6_3 = calculate_OPsimilarity(matrix_6, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性6-3: {similarity6_3:.2f}")

    similarity6_4 = calculate_OPsimilarity(matrix_6, matrix_6, operations_1, operations_1)
    print(f"操作轮廓相似性6-4: {similarity6_4:.2f}")

    similarity7_1 = calculate_OPsimilarity(matrix_7, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性7-1: {similarity7_1:.2f}")

    similarity7_2 = calculate_OPsimilarity(matrix_7, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性7-2: {similarity7_2:.2f}")

    similarity7_3 = calculate_OPsimilarity(matrix_7, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性7-3: {similarity7_3:.2f}")

    similarity7_4 = calculate_OPsimilarity(matrix_7, matrix_7, operations_1, operations_1)
    print(f"操作轮廓相似性7-4: {similarity7_4:.2f}")

    similarity8_1 = calculate_OPsimilarity(matrix_1, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性8-1: {similarity8_1:.2f}")

    similarity8_2 = calculate_OPsimilarity(matrix_1, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性8-2: {similarity8_2:.2f}")

    similarity8_3 = calculate_OPsimilarity(matrix_1, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性8-3: {similarity8_3:.2f}")

    similarity8_4 = calculate_OPsimilarity(matrix_1, matrix_6, operations_1, operations_1)
    print(f"操作轮廓相似性8-4: {similarity8_4:.2f}")

    similarity9_1 = calculate_OPsimilarity(matrix_6, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性9-1: {similarity9_1:.2f}")

    similarity9_2 = calculate_OPsimilarity(matrix_6, matrix_7, operations_1, operations_1)
    print(f"操作轮廓相似性9-2: {similarity9_2:.2f}")

    similarity9_3 = calculate_OPsimilarity(matrix_6, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性9-3: {similarity9_3:.2f}")

    similarity9_4 = calculate_OPsimilarity(matrix_6, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性9-4: {similarity9_4:.2f}")

    similarity10_1 = calculate_OPsimilarity(matrix_2, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性10-1: {similarity10_1:.2f}")

    similarity10_2 = calculate_OPsimilarity(matrix_2, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性10-2: {similarity10_2:.2f}")

    similarity10_3 = calculate_OPsimilarity(matrix_2, matrix_6, operations_1, operations_1)
    print(f"操作轮廓相似性10-3: {similarity10_3:.2f}")

    similarity10_4 = calculate_OPsimilarity(matrix_2, matrix_3, operations_1, operations_1)
    print(f"操作轮廓相似性10-4: {similarity10_4:.2f}")

    similarity11_1 = calculate_OPsimilarity(matrix_7, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性11-1: {similarity11_1:.2f}")

    similarity11_2 = calculate_OPsimilarity(matrix_7, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性11-2: {similarity11_2:.2f}")

    similarity11_3 = calculate_OPsimilarity(matrix_7, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性11-3: {similarity11_3:.2f}")

    similarity11_4 = calculate_OPsimilarity(matrix_7, matrix_4, operations_1, operations_1)
    print(f"操作轮廓相似性11-4: {similarity11_4:.2f}")

    similarity12_1 = calculate_OPsimilarity(matrix_3, matrix_7, operations_1, operations_1)
    print(f"操作轮廓相似性12-1: {similarity12_1:.2f}")

    similarity12_2 = calculate_OPsimilarity(matrix_3, matrix_1, operations_1, operations_1)
    print(f"操作轮廓相似性12-2: {similarity12_2:.2f}")

    similarity12_3 = calculate_OPsimilarity(matrix_3, matrix_5, operations_1, operations_1)
    print(f"操作轮廓相似性12-3: {similarity12_3:.2f}")

    similarity12_4 = calculate_OPsimilarity(matrix_3, matrix_2, operations_1, operations_1)
    print(f"操作轮廓相似性12-4: {similarity12_4:.2f}")
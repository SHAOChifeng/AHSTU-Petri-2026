import numpy as np


def calculate_separation(target_vector, all_vectors, coefficients, exclude_self=True):
    """
    计算指定向量的分离值
    :param target_vector: 目标向量键名（如'AE'）
    :param all_vectors: 包含所有向量的字典
    :param coefficients: 加权系数
    :param exclude_self: 是否排除目标向量本身（如计算AE时排除AE和EA）
    :return: 分离值及中间计算结果
    """
    prefix, suffix = target_vector[0], target_vector[1]  # 解析目标向量的前缀和后缀（如AE→前缀A，后缀E）
    other_prefix = suffix  # 另一组向量的前缀为目标后缀（如AE对应EA，即另一组前缀为E）

    # 构建A组向量（前缀为target_vector的前缀，排除目标向量本身）
    vectors_A = {
        k: v for k, v in all_vectors.items()
        if k.startswith(prefix) and k != target_vector and k[1] != suffix  # 排除目标向量和同后缀向量（如AE的同后缀向量不存在）
    }

    # 构建另一组向量（前缀为target_vector的后缀，排除对应的逆向量）
    vectors_other = {
        k: v for k, v in all_vectors.items()
        if k.startswith(other_prefix) and k != f"{suffix}{prefix}"  # 排除逆向量（如AE排除EA）
    }

    # 检查向量对数量是否一致（假设每组有5个向量，如A组排除AE后有AB、AC、AD、AF、AG共5个）
    if len(vectors_A) != len(vectors_other):
        raise ValueError("两组向量数量不一致，请检查数据")

    # 按后缀匹配向量对（如A组的AB对应E组的EB，AD对应ED等）
    suffixes = [k[1] for k in vectors_A.keys()]  # 获取A组向量的后缀（如B, C, D, F, G）
    vector_pairs = [
        (f"{prefix}{suf}", f"{other_prefix}{suf}") for suf in suffixes
    ]

    # 计算分子：所有匹配向量对的加权点积之和
    total_sum = 0
    print(f"\n=== 计算{target_vector}的分离值 ===")
    print("\n=== 匹配向量对及计算结果 ===")
    for a_key, o_key in vector_pairs:
        vec_a = all_vectors[a_key]
        vec_o = all_vectors[o_key]
        result = np.sum(vec_a * vec_o * coefficients)
        total_sum += result
        print(f"{a_key}与{o_key}: {result:.4f}")

    print(f"\n分子总和: {total_sum:.4f}")

    # 计算分母：A组和另一组的平方加权和乘积的平方根
    def sum_squared_weighted(vectors):
        return sum(np.sum(vec ** 2 * coefficients) for vec in vectors.values())

    total_sum_A = sum_squared_weighted(vectors_A)
    total_sum_other = sum_squared_weighted(vectors_other)

    print(f"\nA组平方加权和（排除{target_vector}）: {total_sum_A:.4f}")
    print(f"{other_prefix}组平方加权和（排除{suffix}{prefix}）: {total_sum_other:.4f}")

    sqrt_result = np.sqrt(total_sum_A * total_sum_other)
    final_result = total_sum / sqrt_result if sqrt_result != 0 else 0

    print(f"\n分母（平方根）: {sqrt_result:.4f}")
    print(f"\n最终分离值: {final_result:.4f}")
    return final_result


# ===================== 定义所有向量 =====================
all_vectors = {
    'AB': np.array([0.55, 0.15, 0, 0.3]),
    'AC': np.array([1, 0, 0, 0]),
    'AD': np.array([1, 0, 0, 0]),
    'AE': np.array([0.7, 0, 0, 0.3]),
    'AF': np.array([1, 0, 0, 0]),
    'AG': np.array([1, 0, 0, 0]),
    'BA': np.array([0.15, 0.55, 0, 0.3]),
    'BC': np.array([0.5, 0.2, 0, 0.3]),
    'BD': np.array([0.5, 0.2, 0, 0.3]),
    'BE': np.array([1, 0, 0, 0]),
    'BF': np.array([1, 0, 0, 0]),
    'BG': np.array([1, 0, 0, 0]),
    'CA': np.array([0, 1, 0, 0]),
    'CB': np.array([0.2, 0.5, 0, 0.3]),
    'CD': np.array([1, 0, 0, 0]),
    'CE': np.array([0.5, 0, 0, 0.5]),
    'CF': np.array([1, 0, 0, 0]),
    'CG': np.array([1, 0, 0, 0]),
    'DA': np.array([0, 1, 0, 0]),
    'DB': np.array([0.2, 0.5, 0, 0.3]),
    'DC': np.array([0, 1, 0, 0]),
    'DE': np.array([0.7, 0, 0, 0.3]),
    'DF': np.array([1, 0, 0, 0]),
    'DG': np.array([1, 0, 0, 0]),
    'EA': np.array([0, 0.7, 0, 0.3]),
    'EB': np.array([0, 1, 0, 0]),
    'EC': np.array([0, 0.5, 0, 0.5]),
    'ED': np.array([0, 0.7, 0, 0.3]),
    'EF': np.array([1, 0, 0, 0]),
    'EG': np.array([1, 0, 0, 0]),
    'FA': np.array([0, 1, 0, 0]),
    'FB': np.array([0, 1, 0, 0]),
    'FC': np.array([0, 1, 0, 0]),
    'FD': np.array([0, 1, 0, 0]),
    'FE': np.array([0, 1, 0, 0]),
    'FG': np.array([1, 0, 0, 0]),
    'GA': np.array([0, 1, 0, 0]),
    'GB': np.array([0, 1, 0, 0]),
    'GC': np.array([0, 1, 0, 0]),
    'GD': np.array([0, 1, 0, 0]),
    'GE': np.array([0, 1, 0, 0]),
    'GF': np.array([0, 1, 0, 0]),
}

coefficients = np.array([0.25, 0.25, 0.3, 0.2])

# ===================== 示例：计算AB的分离值 =====================
calculate_separation('AB', all_vectors, coefficients)
# ===================== 示例：计算AC的分离值 =====================
calculate_separation('AC', all_vectors, coefficients)
# ===================== 示例：计算AD的分离值 =====================
calculate_separation('AD', all_vectors, coefficients)
# ===================== 示例：计算AE的分离值 =====================
calculate_separation('AE', all_vectors, coefficients)
# ===================== 示例：计算AF的分离值 =====================
calculate_separation('AF', all_vectors, coefficients)
# ===================== 示例：计算AG的分离值 =====================
calculate_separation('AG', all_vectors, coefficients)
# ===================== 示例：计算BC的分离值 =====================
calculate_separation('BC', all_vectors, coefficients)
# ===================== 示例：计算BD的分离值 =====================
calculate_separation('BD', all_vectors, coefficients)
# ===================== 示例：计算BE的分离值 =====================
calculate_separation('BE', all_vectors, coefficients)
# ===================== 示例：计算BF的分离值 =====================
calculate_separation('BF', all_vectors, coefficients)
# ===================== 示例：计算BG的分离值 =====================
calculate_separation('BG', all_vectors, coefficients)
# ===================== 示例：计算CD的分离值 =====================
calculate_separation('CD', all_vectors, coefficients)
# ===================== 示例：计算CE的分离值 =====================
calculate_separation('CE', all_vectors, coefficients)
# ===================== 示例：计算CF的分离值 =====================
calculate_separation('CF', all_vectors, coefficients)
# ===================== 示例：计算CG的分离值 =====================
calculate_separation('CG', all_vectors, coefficients)
# ===================== 示例：计算DE的分离值 =====================
calculate_separation('DE', all_vectors, coefficients)
# ===================== 示例：计算DF的分离值 =====================
calculate_separation('DF', all_vectors, coefficients)
# ===================== 示例：计算DG的分离值 =====================
calculate_separation('DG', all_vectors, coefficients)
# ===================== 示例：计算EF的分离值 =====================
calculate_separation('EF', all_vectors, coefficients)
# ===================== 示例：计算EG的分离值 =====================
calculate_separation('EG', all_vectors, coefficients)
# ===================== 示例：计算FG的分离值 =====================
calculate_separation('FG', all_vectors, coefficients)



import numpy as np
def calculate_separation(target_vector, all_vectors, coefficients, exclude_self=True):
    """
    计算指定向量的分离值
    :param target_vector: 目标向量键名（如'AE'）
    :param all_vectors: 包含所有向量的字典
    :param coefficients: 加权系数
    :param exclude_self: 是否排除目标向量本身（如计算AE时排除AE和EA）
    :return: 分离值及中间计算结果
    """
    prefix, suffix = target_vector[0], target_vector[1]  # 解析目标向量的前缀和后缀（如AE→前缀A，后缀E）
    other_prefix = suffix  # 另一组向量的前缀为目标后缀（如AE对应EA，即另一组前缀为E）

    # 构建A组向量（前缀为target_vector的前缀，排除目标向量本身）
    vectors_A = {
        k: v for k, v in all_vectors.items()
        if k.startswith(prefix) and k != target_vector and k[1] != suffix  # 排除目标向量和同后缀向量（如AE的同后缀向量不存在）
    }

    # 构建另一组向量（前缀为target_vector的后缀，排除对应的逆向量）
    vectors_other = {
        k: v for k, v in all_vectors.items()
        if k.startswith(other_prefix) and k != f"{suffix}{prefix}"  # 排除逆向量（如AE排除EA）
    }

    # 检查向量对数量是否一致（假设每组有5个向量，如A组排除AE后有AB、AC、AD、AF、AG共5个）
    if len(vectors_A) != len(vectors_other):
        raise ValueError("两组向量数量不一致，请检查数据")

    # 按后缀匹配向量对（如A组的AB对应E组的EB，AD对应ED等）
    suffixes = [k[1] for k in vectors_A.keys()]  # 获取A组向量的后缀（如B, C, D, F, G）
    vector_pairs = [
        (f"{prefix}{suf}", f"{other_prefix}{suf}") for suf in suffixes
    ]

    # 计算分子：所有匹配向量对的加权点积之和
    total_sum = 0
    print(f"\n=== 计算{target_vector}的分离值 ===")
    print("\n=== 匹配向量对及计算结果 ===")
    for a_key, o_key in vector_pairs:
        vec_a = all_vectors[a_key]
        vec_o = all_vectors[o_key]
        result = np.sum(vec_a * vec_o * coefficients)
        total_sum += result
        print(f"{a_key}与{o_key}: {result:.4f}")

    print(f"\n分子总和: {total_sum:.4f}")

    # 计算分母：A组和另一组的平方加权和乘积的平方根
    def sum_squared_weighted(vectors):
        return sum(np.sum(vec ** 2 * coefficients) for vec in vectors.values())

    total_sum_A = sum_squared_weighted(vectors_A)
    total_sum_other = sum_squared_weighted(vectors_other)

    print(f"\nA组平方加权和（排除{target_vector}）: {total_sum_A:.4f}")
    print(f"{other_prefix}组平方加权和（排除{suffix}{prefix}）: {total_sum_other:.4f}")

    sqrt_result = np.sqrt(total_sum_A * total_sum_other)
    final_result = total_sum / sqrt_result if sqrt_result != 0 else 0

    print(f"\n分母（平方根）: {sqrt_result:.4f}")
    print(f"\n最终分离值: {final_result:.4f}")
    return final_result


# ===================== 定义所有向量 =====================
all_vectors = {
    'AB': np.array([0.55, 0.15, 0, 0.3]),
    'AC': np.array([1, 0, 0, 0]),
    'AD': np.array([1, 0, 0, 0]),
    'AE': np.array([0.7, 0, 0, 0.3]),
    'AH': np.array([1, 0, 0, 0]),
    'BA': np.array([0.15, 0.55, 0, 0.3]),
    'BC': np.array([0.5, 0.2, 0, 0.3]),
    'BD': np.array([0.5, 0.2, 0, 0.3]),
    'BE': np.array([1, 0, 0, 0]),
    'BH': np.array([1, 0, 0, 0]),
    'CA': np.array([0, 1, 0, 0]),
    'CB': np.array([0.2, 0.5, 0, 0.3]),
    'CD': np.array([1, 0, 0, 0]),
    'CE': np.array([0.5, 0, 0, 0.5]),
    'CH': np.array([1, 0, 0, 0]),
    'DA': np.array([0, 1, 0, 0]),
    'DB': np.array([0.2, 0.5, 0, 0.3]),
    'DC': np.array([0, 1, 0, 0]),
    'DE': np.array([0.7, 0, 0, 0.3]),
    'DH': np.array([1, 0, 0, 0]),
    'EA': np.array([0, 0.7, 0, 0.3]),
    'EB': np.array([0, 1, 0, 0]),
    'EC': np.array([0, 0.5, 0, 0.5]),
    'ED': np.array([0, 0.7, 0, 0.3]),
    'EH': np.array([1, 0, 0, 0]),
    'HA': np.array([0, 1, 0, 0]),
    'HB': np.array([0, 1, 0, 0]),
    'HC': np.array([0, 1, 0, 0]),
    'HD': np.array([0, 1, 0, 0]),
    'HE': np.array([0, 1, 0, 0]),
}

coefficients = np.array([0.25, 0.25, 0.3, 0.2])

# ===================== 示例：计算AB的分离值 =====================
calculate_separation('AB', all_vectors, coefficients)
# ===================== 示例：计算AC的分离值 =====================
calculate_separation('AC', all_vectors, coefficients)
# ===================== 示例：计算AD的分离值 =====================
calculate_separation('AD', all_vectors, coefficients)
# ===================== 示例：计算AE的分离值 =====================
calculate_separation('AE', all_vectors, coefficients)
# ===================== 示例：计算AH的分离值 =====================
calculate_separation('AH', all_vectors, coefficients)

# ===================== 示例：计算BC的分离值 =====================
calculate_separation('BC', all_vectors, coefficients)
# ===================== 示例：计算BD的分离值 =====================
calculate_separation('BD', all_vectors, coefficients)
# ===================== 示例：计算BE的分离值 =====================
calculate_separation('BE', all_vectors, coefficients)
# ===================== 示例：计算BH的分离值 =====================
calculate_separation('BH', all_vectors, coefficients)

# ===================== 示例：计算CD的分离值 =====================
calculate_separation('CD', all_vectors, coefficients)
# ===================== 示例：计算CE的分离值 =====================
calculate_separation('CE', all_vectors, coefficients)
# ===================== 示例：计算CH的分离值 =====================
calculate_separation('CH', all_vectors, coefficients)

# ===================== 示例：计算DE的分离值 =====================
calculate_separation('DE', all_vectors, coefficients)
# ===================== 示例：计算DH的分离值 =====================
calculate_separation('DH', all_vectors, coefficients)

# ===================== 示例：计算EH的分离值 =====================
calculate_separation('EH', all_vectors, coefficients)



import numpy as np


def calculate_separation(target_vector, all_vectors, coefficients, exclude_self=True):
    """
    计算指定向量的分离值
    :param target_vector: 目标向量键名（如'AE'）
    :param all_vectors: 包含所有向量的字典
    :param coefficients: 加权系数
    :param exclude_self: 是否排除目标向量本身（如计算AE时排除AE和EA）
    :return: 分离值及中间计算结果
    """
    prefix, suffix = target_vector[0], target_vector[1]  # 解析目标向量的前缀和后缀（如AE→前缀A，后缀E）
    other_prefix = suffix  # 另一组向量的前缀为目标后缀（如AE对应EA，即另一组前缀为E）

    # 构建A组向量（前缀为target_vector的前缀，排除目标向量本身）
    vectors_A = {
        k: v for k, v in all_vectors.items()
        if k.startswith(prefix) and k != target_vector and k[1] != suffix  # 排除目标向量和同后缀向量（如AE的同后缀向量不存在）
    }

    # 构建另一组向量（前缀为target_vector的后缀，排除对应的逆向量）
    vectors_other = {
        k: v for k, v in all_vectors.items()
        if k.startswith(other_prefix) and k != f"{suffix}{prefix}"  # 排除逆向量（如AE排除EA）
    }

    # 检查向量对数量是否一致（假设每组有5个向量，如A组排除AE后有AB、AC、AD、AF、AG共5个）
    if len(vectors_A) != len(vectors_other):
        raise ValueError("两组向量数量不一致，请检查数据")

    # 按后缀匹配向量对（如A组的AB对应E组的EB，AD对应ED等）
    suffixes = [k[1] for k in vectors_A.keys()]  # 获取A组向量的后缀（如B, C, D, F, G）
    vector_pairs = [
        (f"{prefix}{suf}", f"{other_prefix}{suf}") for suf in suffixes
    ]

    # 计算分子：所有匹配向量对的加权点积之和
    total_sum = 0
    print(f"\n=== 计算{target_vector}的分离值 ===")
    print("\n=== 匹配向量对及计算结果 ===")
    for a_key, o_key in vector_pairs:
        vec_a = all_vectors[a_key]
        vec_o = all_vectors[o_key]
        result = np.sum(vec_a * vec_o * coefficients)
        total_sum += result
        print(f"{a_key}与{o_key}: {result:.4f}")

    print(f"\n分子总和: {total_sum:.4f}")

    # 计算分母：A组和另一组的平方加权和乘积的平方根
    def sum_squared_weighted(vectors):
        return sum(np.sum(vec ** 2 * coefficients) for vec in vectors.values())

    total_sum_A = sum_squared_weighted(vectors_A)
    total_sum_other = sum_squared_weighted(vectors_other)

    print(f"\nA组平方加权和（排除{target_vector}）: {total_sum_A:.4f}")
    print(f"{other_prefix}组平方加权和（排除{suffix}{prefix}）: {total_sum_other:.4f}")

    sqrt_result = np.sqrt(total_sum_A * total_sum_other)
    final_result = total_sum / sqrt_result if sqrt_result != 0 else 0

    print(f"\n分母（平方根）: {sqrt_result:.4f}")
    print(f"\n最终分离值: {final_result:.4f}")
    return final_result


# ===================== 定义所有向量 =====================
all_vectors = {
    'AB': np.array([0.55, 0.15, 0, 0.3]),
    'AI': np.array([1, 0, 0, 0]),
    'AE': np.array([0.7, 0, 0, 0.3]),
    'AH': np.array([1, 0, 0, 0]),
    'BA': np.array([0.15, 0.55, 0, 0.3]),
    'BI': np.array([0.5, 0.2, 0, 0.3]),
    'BE': np.array([1, 0, 0, 0]),
    'BH': np.array([1, 0, 0, 0]),
    'IA': np.array([0, 1, 0, 0]),
    'IB': np.array([0.2, 0.5, 0, 0.3]),
    'IE': np.array([0.5, 0, 0, 0.5]),
    'IH': np.array([1, 0, 0, 0]),
    'EA': np.array([0, 0.7, 0, 0.3]),
    'EB': np.array([0, 1, 0, 0]),
    'EI': np.array([0, 0.6, 0, 0.4]),
    'EH': np.array([1, 0, 0, 0]),
    'HA': np.array([0, 1, 0, 0]),
    'HB': np.array([0, 1, 0, 0]),
    'HI': np.array([0, 1, 0, 0]),
    'HE': np.array([0, 1, 0, 0]),
}

coefficients = np.array([0.25, 0.25, 0.3, 0.2])

# ===================== 示例：计算AB的分离值 =====================
calculate_separation('AB', all_vectors, coefficients)
# ===================== 示例：计算AI的分离值 =====================
calculate_separation('AI', all_vectors, coefficients)

# ===================== 示例：计算AE的分离值 =====================
calculate_separation('AE', all_vectors, coefficients)
# ===================== 示例：计算AH的分离值 =====================
calculate_separation('AH', all_vectors, coefficients)

# ===================== 示例：计算BI的分离值 =====================
calculate_separation('BI', all_vectors, coefficients)

# ===================== 示例：计算BE的分离值 =====================
calculate_separation('BE', all_vectors, coefficients)
# ===================== 示例：计算BH的分离值 =====================
calculate_separation('BH', all_vectors, coefficients)

# ===================== 示例：计算IE的分离值 =====================
calculate_separation('IE', all_vectors, coefficients)
# ===================== 示例：计算IH的分离值 =====================
calculate_separation('IH', all_vectors, coefficients)


# ===================== 示例：计算EH的分离值 =====================
calculate_separation('EH', all_vectors, coefficients)


import numpy as np


def calculate_separation(target_vector, all_vectors, coefficients, exclude_self=True):
    """
    计算指定向量的分离值
    :param target_vector: 目标向量键名（如'AE'）
    :param all_vectors: 包含所有向量的字典
    :param coefficients: 加权系数
    :param exclude_self: 是否排除目标向量本身（如计算AE时排除AE和EA）
    :return: 分离值及中间计算结果
    """
    prefix, suffix = target_vector[0], target_vector[1]  # 解析目标向量的前缀和后缀（如AE→前缀A，后缀E）
    other_prefix = suffix  # 另一组向量的前缀为目标后缀（如AE对应EA，即另一组前缀为E）

    # 构建A组向量（前缀为target_vector的前缀，排除目标向量本身）
    vectors_A = {
        k: v for k, v in all_vectors.items()
        if k.startswith(prefix) and k != target_vector and k[1] != suffix  # 排除目标向量和同后缀向量（如AE的同后缀向量不存在）
    }

    # 构建另一组向量（前缀为target_vector的后缀，排除对应的逆向量）
    vectors_other = {
        k: v for k, v in all_vectors.items()
        if k.startswith(other_prefix) and k != f"{suffix}{prefix}"  # 排除逆向量（如AE排除EA）
    }

    # 检查向量对数量是否一致（假设每组有5个向量，如A组排除AE后有AB、AC、AD、AF、AG共5个）
    if len(vectors_A) != len(vectors_other):
        raise ValueError("两组向量数量不一致，请检查数据")

    # 按后缀匹配向量对（如A组的AB对应E组的EB，AD对应ED等）
    suffixes = [k[1] for k in vectors_A.keys()]  # 获取A组向量的后缀（如B, C, D, F, G）
    vector_pairs = [
        (f"{prefix}{suf}", f"{other_prefix}{suf}") for suf in suffixes
    ]

    # 计算分子：所有匹配向量对的加权点积之和
    total_sum = 0
    print(f"\n=== 计算{target_vector}的分离值 ===")
    print("\n=== 匹配向量对及计算结果 ===")
    for a_key, o_key in vector_pairs:
        vec_a = all_vectors[a_key]
        vec_o = all_vectors[o_key]
        result = np.sum(vec_a * vec_o * coefficients)
        total_sum += result
        print(f"{a_key}与{o_key}: {result:.4f}")

    print(f"\n分子总和: {total_sum:.4f}")

    # 计算分母：A组和另一组的平方加权和乘积的平方根
    def sum_squared_weighted(vectors):
        return sum(np.sum(vec ** 2 * coefficients) for vec in vectors.values())

    total_sum_A = sum_squared_weighted(vectors_A)
    total_sum_other = sum_squared_weighted(vectors_other)

    print(f"\nA组平方加权和（排除{target_vector}）: {total_sum_A:.4f}")
    print(f"{other_prefix}组平方加权和（排除{suffix}{prefix}）: {total_sum_other:.4f}")

    sqrt_result = np.sqrt(total_sum_A * total_sum_other)
    final_result = total_sum / sqrt_result if sqrt_result != 0 else 0

    print(f"\n分母（平方根）: {sqrt_result:.4f}")
    print(f"\n最终分离值: {final_result:.4f}")
    return final_result


# ===================== 定义所有向量 =====================
all_vectors = {
    'AB': np.array([0.55, 0.15, 0, 0.3]),
    'AI': np.array([1, 0, 0, 0]),
    'AJ': np.array([0.85, 0, 0, 0.15]),
    'BA': np.array([0.15, 0.55, 0, 0.3]),
    'BI': np.array([0.5, 0.2, 0, 0.3]),
    'BJ': np.array([1, 0, 0, 0]),

    'IA': np.array([0, 1, 0, 0]),
    'IB': np.array([0.2, 0.5, 0, 0.3]),
    'IJ': np.array([0.8, 0, 0, 0.2]),
    'JA': np.array([0, 0.85, 0, 0.15]),
    'JB': np.array([0, 1, 0, 0]),
    'JI': np.array([0, 0.8, 0, 0.2]),
}

coefficients = np.array([0.25, 0.25, 0.3, 0.2])

# ===================== 示例：计算AB的分离值 =====================
calculate_separation('AB', all_vectors, coefficients)
# ===================== 示例：计算AI的分离值 =====================
calculate_separation('AI', all_vectors, coefficients)
# ===================== 示例：计算AJ的分离值 =====================
calculate_separation('AJ', all_vectors, coefficients)
# ===================== 示例：计算BI的分离值 =====================
calculate_separation('BI', all_vectors, coefficients)
# ===================== 示例：计算BJ的分离值 =====================
calculate_separation('BJ', all_vectors, coefficients)
# ===================== 示例：计算IJ的分离值 =====================
calculate_separation('IJ', all_vectors, coefficients)


import numpy as np


def calculate_separation(target_vector, all_vectors, coefficients, exclude_self=True):
    """
    计算指定向量的分离值
    :param target_vector: 目标向量键名（如'AE'）
    :param all_vectors: 包含所有向量的字典
    :param coefficients: 加权系数
    :param exclude_self: 是否排除目标向量本身（如计算AE时排除AE和EA）
    :return: 分离值及中间计算结果
    """
    prefix, suffix = target_vector[0], target_vector[1]  # 解析目标向量的前缀和后缀（如AE→前缀A，后缀E）
    other_prefix = suffix  # 另一组向量的前缀为目标后缀（如AE对应EA，即另一组前缀为E）

    # 构建A组向量（前缀为target_vector的前缀，排除目标向量本身）
    vectors_A = {
        k: v for k, v in all_vectors.items()
        if k.startswith(prefix) and k != target_vector and k[1] != suffix  # 排除目标向量和同后缀向量（如AE的同后缀向量不存在）
    }

    # 构建另一组向量（前缀为target_vector的后缀，排除对应的逆向量）
    vectors_other = {
        k: v for k, v in all_vectors.items()
        if k.startswith(other_prefix) and k != f"{suffix}{prefix}"  # 排除逆向量（如AE排除EA）
    }

    # 检查向量对数量是否一致（假设每组有5个向量，如A组排除AE后有AB、AC、AD、AF、AG共5个）
    if len(vectors_A) != len(vectors_other):
        raise ValueError("两组向量数量不一致，请检查数据")

    # 按后缀匹配向量对（如A组的AB对应E组的EB，AD对应ED等）
    suffixes = [k[1] for k in vectors_A.keys()]  # 获取A组向量的后缀（如B, C, D, F, G）
    vector_pairs = [
        (f"{prefix}{suf}", f"{other_prefix}{suf}") for suf in suffixes
    ]

    # 计算分子：所有匹配向量对的加权点积之和
    total_sum = 0
    print(f"\n=== 计算{target_vector}的分离值 ===")
    print("\n=== 匹配向量对及计算结果 ===")
    for a_key, o_key in vector_pairs:
        vec_a = all_vectors[a_key]
        vec_o = all_vectors[o_key]
        result = np.sum(vec_a * vec_o * coefficients)
        total_sum += result
        print(f"{a_key}与{o_key}: {result:.4f}")

    print(f"\n分子总和: {total_sum:.4f}")

    # 计算分母：A组和另一组的平方加权和乘积的平方根
    def sum_squared_weighted(vectors):
        return sum(np.sum(vec ** 2 * coefficients) for vec in vectors.values())

    total_sum_A = sum_squared_weighted(vectors_A)
    total_sum_other = sum_squared_weighted(vectors_other)

    print(f"\nA组平方加权和（排除{target_vector}）: {total_sum_A:.4f}")
    print(f"{other_prefix}组平方加权和（排除{suffix}{prefix}）: {total_sum_other:.4f}")

    sqrt_result = np.sqrt(total_sum_A * total_sum_other)
    final_result = total_sum / sqrt_result if sqrt_result != 0 else 0

    print(f"\n分母（平方根）: {sqrt_result:.4f}")
    print(f"\n最终分离值: {final_result:.4f}")
    return final_result


# ===================== 定义所有向量 =====================
all_vectors = {
    'KB': np.array([0.375, 0.325, 0, 0.3]),
    'KJ': np.array([0.825, 0, 0, 0.175]),

    'BK': np.array([0.325, 0.375, 0, 0.3]),
    'BJ': np.array([1, 0, 0, 0]),

    'JK': np.array([0, 0.825, 0, 0.175]),
    'JB': np.array([0, 1, 0, 0]),
}

coefficients = np.array([0.25, 0.25, 0.3, 0.2])

# ===================== 示例：计算KB的分离值 =====================
calculate_separation('KB', all_vectors, coefficients)

# ===================== 示例：计算KJ的分离值 =====================
calculate_separation('KJ', all_vectors, coefficients)

# ===================== 示例：计算BJ的分离值 =====================
calculate_separation('BJ', all_vectors, coefficients)

from typing import Dict, List, Set, Tuple, Union


class OperationComponentSimilarity:
    """计算两个流程中相同操作的组件相似性"""

    def __init__(self, process1: Dict[str, List[Union[str, int]]],
                 process2: Dict[str, List[Union[str, int]]]):
        """
        初始化计算器

        Args:
            process1: 第一个流程的操作-组件映射 {操作名称: [组件列表]}
            process2: 第二个流程的操作-组件映射 {操作名称: [组件列表]}
        """
        # 转换为集合去重
        self.process1 = {op: set(comps) for op, comps in process1.items()}
        self.process2 = {op: set(comps) for op, comps in process2.items()}

    def calculate_similarity(self, operation: str) -> float:
        """
        计算指定操作的组件相似性（Jaccard系数）

        Args:
            operation: 操作名称

        Returns:
            相似性分数（0-1），操作不存在返回-1
        """
        if operation not in self.process1 or operation not in self.process2:
            return -1

        comps1 = self.process1[operation]
        comps2 = self.process2[operation]

        # 处理空集特殊情况：均为空时相似性为1，否则为0
        if not comps1 and not comps2:
            return 1.0
        if not comps1 or not comps2:
            return 0.0

        intersection = comps1.intersection(comps2)
        union = comps1.union(comps2)
        return len(intersection) / len(union)

    def batch_calculate(self) -> Dict[str, float]:
        """
        批量计算所有共有操作的组件相似性

        Returns:
            {操作名称: 相似性分数} 的映射
        """
        common_ops = set(self.process1.keys()) & set(self.process2.keys())
        return {op: self.calculate_similarity(op) for op in common_ops}

    def get_final_similarity(self) -> float:
        """
        计算最终相似性：所有操作相似性的和除以两个流程操作并集的元素个数

        Returns:
            最终相似性分数，保留两位小数
        """
        all_ops = set(self.process1.keys()).union(set(self.process2.keys()))
        common_ops = set(self.process1.keys()).intersection(set(self.process2.keys()))

        total_similarity = 0.0
        for op in common_ops:
            similarity = self.calculate_similarity(op)
            total_similarity += similarity

        if not all_ops:
            return 0.0

        return round(total_similarity / len(all_ops), 2)



# 使用示例 - 修改后的调用方式
def main():
    # 示例数据：两个流程的操作-组件映射
    process_1 = {
        "A": ["R1", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_1_1 = {
        "A": ["R1", "R15", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R16", "R17"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_1_2 = {
        "A": ["R1", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R18"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_1_3 = {
        "A": ["R19", "R15", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R10","R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_1_4 = {
        "A": ["R1", "R15", "R21", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    # 初始化计算器(1-1)
    calculator1_1 = OperationComponentSimilarity(process_1, process_1_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator1_1.batch_calculate():
        print(f"{op}: {calculator1_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性1_1:", calculator1_1.get_final_similarity())


    # 初始化计算器(1-2)
    calculator1_2 = OperationComponentSimilarity(process_1, process_1_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator1_2.batch_calculate():
        print(f"{op}: {calculator1_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性1_2:", calculator1_2.get_final_similarity())


    # 初始化计算器(1-3)
    calculator1_3 = OperationComponentSimilarity(process_1, process_1_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator1_3.batch_calculate():
        print(f"{op}: {calculator1_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性1_3:", calculator1_3.get_final_similarity())


    # 初始化计算器(1-4)
    calculator1_4 = OperationComponentSimilarity(process_1, process_1_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator1_4.batch_calculate():
        print(f"{op}: {calculator1_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性1_4:", calculator1_4.get_final_similarity())


    process_2 = {
        "A": ["R25", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R27"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_2_1 = {
        "A": ["R19", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R18"],
        "E": ["R27"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_2_2 = {
        "A": ["R25", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9","R28"],
        "E": ["R27"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_2_3 = {
        "A": ["R25", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R27"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_2_4 = {
        "A": ["R19", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R27"],
        "F": ["R13", "R24"],
        "G": []
    }

    # 初始化计算器(2-1)
    calculator2_1 = OperationComponentSimilarity(process_2, process_2_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator2_1.batch_calculate():
        print(f"{op}: {calculator2_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性2_1:", calculator2_1.get_final_similarity())


    # 初始化计算器(2-2)
    calculator2_2 = OperationComponentSimilarity(process_2, process_2_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator2_2.batch_calculate():
        print(f"{op}: {calculator2_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性2_2:", calculator2_2.get_final_similarity())

    # 初始化计算器(2-3)
    calculator2_3 = OperationComponentSimilarity(process_2, process_2_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator2_3.batch_calculate():
        print(f"{op}: {calculator2_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性2_3:", calculator2_3.get_final_similarity())

    # 初始化计算器(2-4)
    calculator2_4 = OperationComponentSimilarity(process_2, process_2_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator2_4.batch_calculate():
        print(f"{op}: {calculator2_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性2_4:", calculator2_4.get_final_similarity())

    process_3 = {
        "A": ["R1", "R15", "R29", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_3_1 = {
        "A": ["R25", "R15", "R29", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_3_2 = {
        "A": ["R1", "R15", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_3_3 = {
        "A": ["R19", "R15", "R29", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_3_4 = {
        "A": ["R1", "R15", "R29", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    # 初始化计算器(3-1)
    calculator3_1 = OperationComponentSimilarity(process_3, process_3_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator3_1.batch_calculate():
        print(f"{op}: {calculator3_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性3_1:", calculator3_1.get_final_similarity())

    # 初始化计算器(3-2)
    calculator3_2 = OperationComponentSimilarity(process_3, process_3_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator3_2.batch_calculate():
        print(f"{op}: {calculator3_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性3_2:", calculator3_2.get_final_similarity())

    # 初始化计算器(3-3)
    calculator3_3 = OperationComponentSimilarity(process_3, process_3_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator3_3.batch_calculate():
        print(f"{op}: {calculator3_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性3_3:", calculator3_3.get_final_similarity())


    # 初始化计算器(3-4)
    calculator3_4 = OperationComponentSimilarity(process_3, process_3_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator3_4.batch_calculate():
        print(f"{op}: {calculator3_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性3_4:", calculator3_4.get_final_similarity())

    process_4 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R30", "R31"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_4_1 = {
        "A": ["R1", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_4_2 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R30", "R31"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_4_3 = {
        "A": ["R19", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_4_4 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R30", "R31"],
        "E": ["R33"],
        "F": ["R13", "R14"],
        "G": []
    }

    # 初始化计算器(4-1)
    calculator4_1 = OperationComponentSimilarity(process_4, process_4_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator4_1.batch_calculate():
        print(f"{op}: {calculator4_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性4_1:", calculator4_1.get_final_similarity())

    # 初始化计算器(4-2)
    calculator4_2 = OperationComponentSimilarity(process_4, process_4_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator4_2.batch_calculate():
        print(f"{op}: {calculator4_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性4_2:", calculator4_2.get_final_similarity())

    # 初始化计算器(4-3)
    calculator4_3 = OperationComponentSimilarity(process_4, process_4_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator4_3.batch_calculate():
        print(f"{op}: {calculator4_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性4_3:", calculator4_3.get_final_similarity())

    # 初始化计算器(4-4)
    calculator4_4 = OperationComponentSimilarity(process_4, process_4_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator4_4.batch_calculate():
        print(f"{op}: {calculator4_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性4_4:", calculator4_4.get_final_similarity())

    process_5 = {
        "A": ["R1", "R2", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_5_1 = {
        "A": ["R1", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_5_2 = {
        "A": ["R1", "R2", "R3", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R40", "R41"],
        "E": ["R42"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_5_3 = {
        "A": ["R1", "R2", "R34", "R35", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R9"],
        "D": ["R10", "R28"],
        "E": ["R12"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_5_4 = {
        "A": ["R1", "R2", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    # 初始化计算器(5-1)
    calculator5_1 = OperationComponentSimilarity(process_5, process_5_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator5_1.batch_calculate():
        print(f"{op}: {calculator5_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性5_1:", calculator5_1.get_final_similarity())

    # 初始化计算器(5-2)
    calculator5_2 = OperationComponentSimilarity(process_5, process_5_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator5_2.batch_calculate():
        print(f"{op}: {calculator5_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性5_2:", calculator5_2.get_final_similarity())

    # 初始化计算器(5-3)
    calculator5_3 = OperationComponentSimilarity(process_5, process_5_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator5_3.batch_calculate():
        print(f"{op}: {calculator5_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性5_3:", calculator5_3.get_final_similarity())

    # 初始化计算器(5-4)
    calculator5_4 = OperationComponentSimilarity(process_5, process_5_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator5_4.batch_calculate():
        print(f"{op}: {calculator5_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性5_4:", calculator5_4.get_final_similarity())

    process_6 = {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R10", "R23"],
        "E": ["R42"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_6_1 = {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R40", "R41"],
        "E": ["R42"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_6_2 = {
        "A": ["R25", "R15", "R21", "R22", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R20"],
        "D": ["R10", "R23"],
        "E": ["R42"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_6_3 = {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R10", "R11"],
        "E": ["R42"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_6_4 = {
        "A": ["R25", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R10", "R23"],
        "E": ["R42"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    # 初始化计算器(6-1)
    calculator6_1 = OperationComponentSimilarity(process_6, process_6_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator6_1.batch_calculate():
        print(f"{op}: {calculator6_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性6_1:", calculator6_1.get_final_similarity())

    # 初始化计算器(6-2)
    calculator6_2 = OperationComponentSimilarity(process_6, process_6_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator6_2.batch_calculate():
        print(f"{op}: {calculator6_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性6_2:", calculator6_2.get_final_similarity())

    # 初始化计算器(6-3)
    calculator6_3 = OperationComponentSimilarity(process_6, process_6_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator6_3.batch_calculate():
        print(f"{op}: {calculator6_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性6_3:", calculator6_3.get_final_similarity())

    # 初始化计算器(6-4)
    calculator6_4 = OperationComponentSimilarity(process_6, process_6_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator6_4.batch_calculate():
        print(f"{op}: {calculator6_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性6_4:", calculator6_4.get_final_similarity())

    process_7= {
        "A": ["R25", "R2", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R20"],
        "D": ["R16", "R43"],
        "E": ["R12"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    process_7_1 = {
        "A": ["R25", "R15", "R29", "R22", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R20"],
        "D": ["R16", "R43"],
        "E": ["R33"],
        "F": ["R13", "R43"],
        "G": []
    }

    process_7_2 = {
        "A": ["R25", "R2", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R9"],
        "D": ["R16", "R43"],
        "E": ["R12"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    process_7_3 = {
        "A": ["R25", "R2", "R3", "R4", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R16", "R43"],
        "E": ["R12"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    process_7_4 = {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R20"],
        "D": ["R18"],
        "E": ["R12"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    # 初始化计算器(7-1)
    calculator7_1 = OperationComponentSimilarity(process_7, process_7_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator7_1.batch_calculate():
        print(f"{op}: {calculator7_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性7_1:", calculator7_1.get_final_similarity())

    # 初始化计算器(7-2)
    calculator7_2 = OperationComponentSimilarity(process_7, process_7_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator7_2.batch_calculate():
        print(f"{op}: {calculator7_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性7_2:", calculator7_2.get_final_similarity())

    # 初始化计算器(7-3)
    calculator7_3 = OperationComponentSimilarity(process_7, process_7_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator7_3.batch_calculate():
        print(f"{op}: {calculator7_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性7_3:", calculator7_3.get_final_similarity())

    # 初始化计算器(7-4)
    calculator7_4 = OperationComponentSimilarity(process_7, process_7_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator7_4.batch_calculate():
        print(f"{op}: {calculator7_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性7_4:", calculator7_4.get_final_similarity())

    process_8 = {
        "A": ["R19", "R2", "R34", "R35", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R44"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_8_1 = {
        "A": ["R19", "R45", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R44"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_8_2 = {
        "A": ["R1", "R45", "R34", "R35", "R5"],
        "B": ["R6", "R7"],
        "C": ["R9", "R38"],
        "D": ["R9", "R26"],
        "E": ["R44"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_8_3 = {
        "A": ["R19", "R2", "R34", "R35", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R9", "R26"],
        "E": ["R44"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_8_4 = {
        "A": ["R19", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8", "R20"],
        "D": ["R47", "R26"],
        "E": ["R44"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    # 初始化计算器(8-1)
    calculator8_1 = OperationComponentSimilarity(process_8, process_8_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator8_1.batch_calculate():
        print(f"{op}: {calculator8_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性8_1:", calculator8_1.get_final_similarity())

    # 初始化计算器(8-2)
    calculator8_2 = OperationComponentSimilarity(process_8, process_8_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator8_2.batch_calculate():
        print(f"{op}: {calculator8_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性8_2:", calculator8_2.get_final_similarity())

    # 初始化计算器(8-3)
    calculator8_3 = OperationComponentSimilarity(process_8, process_8_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator8_3.batch_calculate():
        print(f"{op}: {calculator8_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性8_3:", calculator8_3.get_final_similarity())

    # 初始化计算器(8-4)
    calculator8_4 = OperationComponentSimilarity(process_8, process_8_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator8_4.batch_calculate():
        print(f"{op}: {calculator8_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性8_4:", calculator8_4.get_final_similarity())

    process_9 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R46"],
        "D": ["R47", "R26"],
        "E": ["R44"],
        "F": ["R14", "R48"],
        "G": []
    }

    process_9_1 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R46"],
        "D": ["R9", "R26"],
        "E": ["R27"],
        "F": ["R14", "R48"],
        "G": []
    }

    process_9_2 = {
        "A": ["R1", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R8","R20"],
        "D": ["R47", "R26"],
        "E": ["R44"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_9_3 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R46"],
        "D": ["R47", "R26"],
        "E": ["R44"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_9_4 = {
        "A": ["R25", "R2", "R32", "R22", "R5"],
        "B": ["R36", "R37"],
        "C": ["R46"],
        "D": ["R47", "R26"],
        "E": ["R27"],
        "F": ["R13", "R14"],
        "G": []
    }

    # 初始化计算器(9-1)
    calculator9_1 = OperationComponentSimilarity(process_9, process_9_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator9_1.batch_calculate():
        print(f"{op}: {calculator9_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性9_1:", calculator9_1.get_final_similarity())

    # 初始化计算器(9-2)
    calculator9_2 = OperationComponentSimilarity(process_9, process_9_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator9_2.batch_calculate():
        print(f"{op}: {calculator9_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性9_2:", calculator9_2.get_final_similarity())

    # 初始化计算器(9-3)
    calculator9_3 = OperationComponentSimilarity(process_9, process_9_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator9_3.batch_calculate():
        print(f"{op}: {calculator9_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性9_3:", calculator9_3.get_final_similarity())

    # 初始化计算器(9-4)
    calculator9_4 = OperationComponentSimilarity(process_9, process_9_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator9_4.batch_calculate():
        print(f"{op}: {calculator9_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性9_4:", calculator9_4.get_final_similarity())

    process_10 = {
        "A": ["R25", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9","R38"],
        "D": ["R49","R55"],
        "E": ["R44"],
        "F": ["R14", "R48"],
        "G": []
    }

    process_10_1 = {
        "A": ["R19", "R2", "R32", "R22", "R5"],
        "B": ["R6", "R7"],
        "C": ["R46"],
        "D": ["R49", "R55"],
        "E": ["R44"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_10_2 = {
        "A": ["R25", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R50"],
        "C": ["R9","R38"],
        "D": ["R49","R55"],
        "E": ["R44"],
        "F": ["R14", "R48"],
        "G": []
    }

    process_10_3 = {
        "A": ["R25", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R50"],
        "C": ["R9","R38"],
        "D": ["R49","R55"],
        "E": ["R44"],
        "F": ["R14", "R48"],
        "G": []
    }

    process_10_4= {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R51"],
        "C": ["R9","R38"],
        "D": ["R49","R55"],
        "E": ["R44"],
        "F": ["R14", "R48"],
        "G": []
    }

    # 初始化计算器(10-1)
    calculator10_1 = OperationComponentSimilarity(process_10, process_10_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator10_1.batch_calculate():
        print(f"{op}: {calculator10_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性10_1:", calculator10_1.get_final_similarity())

    # 初始化计算器(10-2)
    calculator10_2 = OperationComponentSimilarity(process_10, process_10_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator10_2.batch_calculate():
        print(f"{op}: {calculator10_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性10_2:", calculator10_2.get_final_similarity())

    # 初始化计算器(10-3)
    calculator10_3 = OperationComponentSimilarity(process_10, process_10_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator10_3.batch_calculate():
        print(f"{op}: {calculator10_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性10_3:", calculator10_3.get_final_similarity())

    # 初始化计算器(10-4)
    calculator10_4 = OperationComponentSimilarity(process_10, process_10_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator10_4.batch_calculate():
        print(f"{op}: {calculator10_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性10_4:", calculator10_4.get_final_similarity())

    process_11 = {
        "A": ["R19", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R51"],
        "C": ["R9", "R38"],
        "D": ["R49", "R55"],
        "E": ["R44"],
        "F": ["R13", "R14","R39"],
        "G": []
    }

    process_11_1 = {
        "A": ["R1", "R15", "R29", "R22", "R5"],
        "B": ["R36", "R51"],
        "C": ["R9", "R38"],
        "D": ["R41", "R52"],
        "E": ["R44"],
        "F": ["R13", "R24"],
        "G": []
    }

    process_11_2 = {
        "A": ["R25", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R9", "R38"],
        "D": ["R49", "R55"],
        "E": ["R44"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    process_11_3 = {
        "A": ["R19", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R51"],
        "C": ["R9", "R38"],
        "D": ["R49", "R55"],
        "E": ["R44"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_11_4 = {
        "A": ["R19", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R50"],
        "C": ["R9", "R38"],
        "D": ["R49", "R55"],
        "E": ["R27"],
        "F": ["R13", "R14", "R39"],
        "G": []
    }

    # 初始化计算器(11-1)
    calculator11_1 = OperationComponentSimilarity(process_11, process_11_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator11_1.batch_calculate():
        print(f"{op}: {calculator11_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性11_1:", calculator11_1.get_final_similarity())

    # 初始化计算器(11-2)
    calculator11_2 = OperationComponentSimilarity(process_11, process_11_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator11_2.batch_calculate():
        print(f"{op}: {calculator11_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性11_2:", calculator11_2.get_final_similarity())

    # 初始化计算器(11-3)
    calculator11_3 = OperationComponentSimilarity(process_11, process_11_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator11_3.batch_calculate():
        print(f"{op}: {calculator11_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性11_3:", calculator11_3.get_final_similarity())

    # 初始化计算器(11-4)
    calculator11_4 = OperationComponentSimilarity(process_11, process_11_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator11_4.batch_calculate():
        print(f"{op}: {calculator11_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性11_4:", calculator11_4.get_final_similarity())

    process_12 = {
        "A": ["R1", "R2", "R29", "R22", "R5"],
        "B": ["R36", "R50"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_12_1 = {
        "A": ["R1", "R2", "R29", "R22", "R5"],
        "B": ["R36", "R50"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_12_2 = {
        "A": ["R1", "R15", "R34", "R35", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R9"],
        "D": ["R10", "R23"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_12_3 = {
        "A": ["R1", "R2", "R29", "R22", "R5"],
        "B": ["R36", "R51"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R14"],
        "G": []
    }

    process_12_4 = {
        "A": ["R1", "R2", "R29", "R22", "R5"],
        "B": ["R36", "R37"],
        "C": ["R8", "R9"],
        "D": ["R10", "R11"],
        "E": ["R12"],
        "F": ["R13", "R24"],
        "G": []
    }

    # 初始化计算器(12-1)
    calculator12_1 = OperationComponentSimilarity(process_12, process_12_1)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator12_1.batch_calculate():
        print(f"{op}: {calculator12_1.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性12_1:", calculator12_1.get_final_similarity())

    # 初始化计算器(12-2)
    calculator12_2 = OperationComponentSimilarity(process_12, process_12_2)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator12_2.batch_calculate():
        print(f"{op}: {calculator12_2.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性12_2:", calculator12_2.get_final_similarity())

    # 初始化计算器(12-3)
    calculator12_3 = OperationComponentSimilarity(process_12, process_12_3)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator12_3.batch_calculate():
        print(f"{op}: {calculator12_3.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性12_3:", calculator12_3.get_final_similarity())

    # 初始化计算器(12-4)
    calculator12_4 = OperationComponentSimilarity(process_12, process_12_4)
    # 批量计算所有共有操作
    print("\n所有共有操作的组件相似性:")
    for op in calculator12_4.batch_calculate():
        print(f"{op}: {calculator12_4.calculate_similarity(op):.2f}")

    # 计算最终相似性
    print("\n最终相似性12_4:", calculator12_4.get_final_similarity())

# 确保类定义后再执行代码
if __name__ == "__main__":
    main()


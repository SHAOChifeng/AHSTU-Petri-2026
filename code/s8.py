import numpy as np

# 定义两个矩阵(参1‘-变3（2’）)
matrix_1 = np.array([[0,1,1/2,1/3,1/4,1/5,1/6], [0,0,1,1/2,1/3,1/4,1/5],[0,0,0,1,1/2,1/3,1/4],[0,0,0,0,1,1/2,1/3],[0,0,0,0,0,1,1/2],[0,0,0,0,0,0,1]])
matrix_2 = np.array([[0,0,1,1/2,1/3,1/4,1/5], [1,0,1/2,1/3,1/4,1/5,1/6],[0,0,0,1,1/2,1/3,1/4],[0,0,0,0,1,1/2,1/3],[0,0,0,0,0,1,1/2],[0,0,0,0,0,0,1]])

result1 = np.sum(matrix_1 ** 2)

result2 = np.sum(matrix_2 ** 2)


# 对应元素相乘
element_multiply = np.multiply(matrix_1, matrix_2)

# 将对应元素相乘的结果相加
result1_2 = np.sum(element_multiply)


import math

sqrt_result1 = math.sqrt(result1)
sqrt_result2 = math.sqrt(result2)
s1_2=0.5*0.82+0.5*result1_2/(sqrt_result1*sqrt_result2)
print(s1_2)



# 定义两个矩阵(参1‘-变2（3’）)
matrix_3 = np.array([[0,0,1,1/2,1/3,1/4,1/5], [0,0,0,0,1,1/2,1/3],[0,0,0,1,0,1/2,1/3],[0,0,0,0,0,1,1/2],[0,0,0,0,0,1,1/2],[0,0,0,0,0,0,1]])

# 计算平方和
result3 = np.sum(matrix_3 ** 2)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_1, matrix_3)
result1_3 = np.sum(element_multiply)


sqrt_result3 = math.sqrt(result3)
s1_3=0.5*6/7+0.5*result1_3/(sqrt_result1*sqrt_result3)
print(s1_3)

# 定义两个矩阵(参1‘-变4（4’）)
matrix_4 = np.array([[0,1,1/3,1/4,1/2,1/5,1/6], [0,0,1/2,1/3,1,1/4,1/5],[0,0,0,1,0,1/2,1/3],[0,0,0,0,0,1,1/2],[0,0,1,1/2,0,1/3,1/4],[0,0,0,0,0,0,1]])

# 计算平方和
result4 = np.sum(matrix_4 ** 2)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_1, matrix_4)
result1_4 = np.sum(element_multiply)


sqrt_result4 = math.sqrt(result4)
s1_4=0.5*0.7+0.5*result1_4/(sqrt_result1*sqrt_result4)
print(s1_4)

# 定义两个矩阵(参2‘-变1（7’）)
matrix_7 = np.array([[0,1,1/2,1/3,1/2,1/3,1/4], [0,0,1,1/2,1,1/2,1/3],[0,0,0,1,0,1/2,1/3],[0,0,0,0,0,1,1/2],[0,0,0,0,0,1,1/2],[0,0,0,0,0,0,1]])

# 计算平方和
result7 = np.sum(matrix_7 ** 2)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_2, matrix_7)
result2_7 = np.sum(element_multiply)


sqrt_result7 = math.sqrt(result7)
s2_7=0.5*0.81+0.5*result2_7/(sqrt_result2*sqrt_result7)
print(s2_7)

# (参2‘-变2（4’）)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_2, matrix_4)
result2_4 = np.sum(element_multiply)



s2_4=0.5*0.91+0.5*result2_4/(sqrt_result2*sqrt_result4)
print(s2_4)

# 定义两个矩阵(参2‘-变3（5’）)
matrix_5 = np.array([[0,1/3,1,1/2,1/4,1/5,1/6], [0,0,0,0,1,1/2,1/3],[0,1/2,0,1,1/3,1/4,1/5],[0,1,0,0,1/2,1/3,1/4],[0,0,0,0,0,1,1/2],[0,0,0,0,0,0,1]])

# 计算平方和
result5 = np.sum(matrix_5 ** 2)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_2, matrix_5)
result2_5 = np.sum(element_multiply)


sqrt_result5 = math.sqrt(result5)
s2_5=0.5*1+0.5*result2_5/(sqrt_result2*sqrt_result5)
print(s2_5)

# 定义两个矩阵(参2‘-变4（2’）)
# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_2, matrix_2)
result2_2 = np.sum(element_multiply)
s2_2=0.5*0.95+0.5*result2_2/(sqrt_result2*sqrt_result2)
print(s2_2)


# 定义两个矩阵(参3‘-变1（3’）)
# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_3, matrix_3)
result3_3 = np.sum(element_multiply)
s3_3=0.5*0.86+0.5*result3_3/(sqrt_result3*sqrt_result3)
print(s3_3)

# 定义两个矩阵(参3‘-变2（6’）)
matrix_6 = np.array([[0,0,1,1/2,0,1/3,1/4], [1/2,0,1/3,1/4,1,1/5,1/6],[0,0,0,1,0,1/2,1/3],[0,0,0,0,0,1,1/2],[1,0,1/2,1/3,0,1/4,1/5],[0,0,0,0,0,0,1]])
# 计算平方和
result6 = np.sum(matrix_6 ** 2)

# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_3, matrix_6)
result3_6 = np.sum(element_multiply)


sqrt_result6 = math.sqrt(result6)
s3_6=0.5*0.82+0.5*result3_6/(sqrt_result3*sqrt_result6)
print(s3_6)

# 定义两个矩阵(参3‘-变3（3’）)
s3_3_3=0.5*0.95+0.5*result3_3/(sqrt_result3*sqrt_result3)
print(s3_3_3)


# 定义两个矩阵(参3‘-变4（5’）)
# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_3, matrix_5)
result3_5 = np.sum(element_multiply)


s3_5=0.5*1+0.5*result3_5/(sqrt_result3*sqrt_result5)
print(s3_5)


# 定义两个矩阵(参4‘-变1（4’）)
# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_4, matrix_4)
result4_4 = np.sum(element_multiply)


s4_4=0.5*0.81+0.5*result4_4/(sqrt_result4*sqrt_result4)
print(s4_4)

# 定义两个矩阵(参4‘-变2（7’）)
# 计算平方和
# 对应元素相乘累积相加
element_multiply = np.multiply(matrix_4, matrix_7)
result4_7= np.sum(element_multiply)

s4_7=0.5*1+0.5*result4_7/(sqrt_result4*sqrt_result7)
print(s4_7)

# 定义两个矩阵(参4‘-变3（1’）)
element_multiply = np.multiply(matrix_4, matrix_1)
result4_1= np.sum(element_multiply)

s4_1=0.5*0.62+0.5*result4_1/(sqrt_result4*sqrt_result1)
print(s4_1)

# 定义两个矩阵(参4‘-变4（1’）)
s4_4_1=0.5*0.76+0.5*result4_1/(sqrt_result4*sqrt_result1)
print(s4_4_1)

# 定义两个矩阵(参5‘-变1（5’）)
element_multiply = np.multiply(matrix_5, matrix_5)
result5_5= np.sum(element_multiply)
s5_5=0.5*0.63+0.5*result5_5/(sqrt_result5*sqrt_result5)
print(s5_5)

# 定义两个矩阵(参5‘-变2（3’）)
element_multiply = np.multiply(matrix_5, matrix_3)
result5_3= np.sum(element_multiply)
s5_3=0.5*0.67+0.5*result5_3/(sqrt_result5*sqrt_result3)
print(s5_3)

# 定义两个矩阵(参5‘-变3（6’）)
element_multiply = np.multiply(matrix_5, matrix_6)
result5_6= np.sum(element_multiply)
s5_6=0.5*0.67+0.5*result5_6/(sqrt_result5*sqrt_result6)
print(s5_6)

# 定义两个矩阵(参5‘-变4（4’）)
element_multiply = np.multiply(matrix_5, matrix_4)
result5_4= np.sum(element_multiply)
s5_4=0.5*1+0.5*result5_4/(sqrt_result5*sqrt_result4)
print(s5_4)

# 定义两个矩阵(参6‘-变1（2’）)
element_multiply = np.multiply(matrix_6, matrix_2)
result6_2= np.sum(element_multiply)
s6_2=0.5*0.86+0.5*result6_2/(sqrt_result6*sqrt_result2)
print(s6_2)

# 定义两个矩阵(参6‘-变2（3’）)
element_multiply = np.multiply(matrix_6, matrix_3)
result6_3= np.sum(element_multiply)
s6_3=0.5*0.64+0.5*result6_3/(sqrt_result6*sqrt_result3)
print(s6_3)

# 定义两个矩阵(参6‘-变3（4’）)
element_multiply = np.multiply(matrix_6, matrix_4)
result6_4= np.sum(element_multiply)
s6_4=0.5*0.9+0.5*result6_4/(sqrt_result6*sqrt_result4)
print(s6_4)

# 定义两个矩阵(参6‘-变4（6’）)
element_multiply = np.multiply(matrix_6, matrix_6)
result6_6= np.sum(element_multiply)
s6_6=0.5*0.95+0.5*result6_6/(sqrt_result6*sqrt_result6)
print(s6_6)

# 定义两个矩阵(参7‘-变1（1’）)
element_multiply = np.multiply(matrix_7, matrix_1)
result7_1= np.sum(element_multiply)
s7_1=0.5*0.64+0.5*result7_1/(sqrt_result7*sqrt_result1)
print(s7_1)

# 定义两个矩阵(参7‘-变2（4’）)
element_multiply = np.multiply(matrix_7, matrix_4)
result7_4= np.sum(element_multiply)
s7_4=0.5*0.9+0.5*result7_4/(sqrt_result7*sqrt_result4)
print(s7_4)

# 定义两个矩阵(参7‘-变3（5’）)
element_multiply = np.multiply(matrix_7, matrix_5)
result7_5= np.sum(element_multiply)
s7_5=0.5*0.78+0.5*result7_5/(sqrt_result7*sqrt_result5)
print(s7_5)

# 定义两个矩阵(参7‘-变4（7’）)
element_multiply = np.multiply(matrix_7, matrix_7)
result7_7= np.sum(element_multiply)
s7_7=0.5*0.78+0.5*result7_7/(sqrt_result7*sqrt_result7)
print(s7_7)

# 定义两个矩阵(参8(1‘)-变1（2’）)
s8_1_2=0.5*0.71+0.5*result1_2/(sqrt_result1*sqrt_result2)
print(s8_1_2)

# 定义两个矩阵(参8(1‘)-变2（4’）)
s8_1_4=0.5*0.78+0.5*result1_4/(sqrt_result1*sqrt_result4)
print(s8_1_4)

# 定义两个矩阵(参8(1‘)-变3（5’）)
element_multiply = np.multiply(matrix_1, matrix_5)
result1_5= np.sum(element_multiply)
s8_1_5=0.5*1+0.5*result1_5/(sqrt_result1*sqrt_result5)
print(s8_1_5)

# 定义两个矩阵(参8(1‘)-变4（6’）)
element_multiply = np.multiply(matrix_1, matrix_6)
result1_6= np.sum(element_multiply)
s8_1_6=0.5*0.72+0.5*result1_6/(sqrt_result1*sqrt_result6)
print(s8_1_6)

# 定义两个矩阵(参9(6‘)-变1（1’）)
element_multiply = np.multiply(matrix_6, matrix_1)
result6_1= np.sum(element_multiply)
s9_6_1=0.5*0.77+0.5*result6_1/(sqrt_result6*sqrt_result1)
print(s9_6_1)


# 定义两个矩阵(参9(6‘)-变2（7’）)
element_multiply = np.multiply(matrix_6, matrix_7)
result6_7= np.sum(element_multiply)
s9_6_7=0.5*0.75+0.5*result6_7/(sqrt_result6*sqrt_result7)
print(s9_6_7)

# 定义两个矩阵(参9(6‘)-变3（2’）)
s9_6_2=0.5*0.9+0.5*result6_2/(sqrt_result6*sqrt_result2)
print(s9_6_2)

# 定义两个矩阵(参9(6‘)-变4（5’）)
element_multiply = np.multiply(matrix_6, matrix_5)
result6_5= np.sum(element_multiply)
s9_6_5=0.5*0.71+0.5*result6_5/(sqrt_result6*sqrt_result5)
print(s9_6_5)

# 定义两个矩阵(参10(2‘)-变1（1’）)
element_multiply = np.multiply(matrix_2, matrix_1)
result2_1= np.sum(element_multiply)
s10_2_1=0.5*0.49+0.5*result2_1/(sqrt_result2*sqrt_result1)
print(s10_2_1)

# 定义两个矩阵(参10(2‘)-变2（5’）)

s10_2_5=0.5*0.91+0.5*result2_5/(sqrt_result2*sqrt_result5)
print(s10_2_5)

# 定义两个矩阵(参10(2‘)-变3（6’）)
element_multiply = np.multiply(matrix_2, matrix_6)
result2_6= np.sum(element_multiply)
s10_2_6=0.5*0.91+0.5*result2_6/(sqrt_result2*sqrt_result6)
print(s10_2_6)

# 定义两个矩阵(参10(2‘)-变4（3’）)
element_multiply = np.multiply(matrix_2, matrix_3)
result2_3= np.sum(element_multiply)
s10_2_3=0.5*0.86+0.5*result2_3/(sqrt_result2*sqrt_result3)
print(s10_2_3)

# 定义两个矩阵(参11(7‘)-变1（1’）)
s11_7_1=0.5*0.64+0.5*result7_1/(sqrt_result7*sqrt_result1)
print(s11_7_1)

# 定义两个矩阵(参11(7‘)-变2（2’）)
element_multiply = np.multiply(matrix_7, matrix_2)
result7_2= np.sum(element_multiply)
s11_7_2=0.5*0.86+0.5*result7_2/(sqrt_result7*sqrt_result2)
print(s11_7_2)

# 定义两个矩阵(参11(7‘)-变3（1’）)
s11_73_1=0.5*0.95+0.5*result7_1/(sqrt_result7*sqrt_result1)
print(s11_73_1)

# 定义两个矩阵(参11(7‘)-变4（4’）)
s11_7_4=0.5*0.76+0.5*result7_4/(sqrt_result7*sqrt_result4)
print(s11_7_4)

# 定义两个矩阵(参12(3‘)-变1（7’）)
element_multiply = np.multiply(matrix_3, matrix_7)
result3_7= np.sum(element_multiply)
s12_3_7=0.5*1+0.5*result3_7/(sqrt_result3*sqrt_result7)
print(s12_3_7)

# 定义两个矩阵(参12(3‘)-变2（1’）)
element_multiply = np.multiply(matrix_3, matrix_1)
result3_1= np.sum(element_multiply)
s12_3_1=0.5*0.7+0.5*result3_1/(sqrt_result3*sqrt_result1)
print(s12_3_1)

# 定义两个矩阵(参12(3‘)-变3（5’）)

s12_3_5=0.5*0.9+0.5*result3_5/(sqrt_result3*sqrt_result5)
print(s12_3_5)

# 定义两个矩阵(参12(3‘)-变4（2’）)
element_multiply = np.multiply(matrix_3, matrix_2)
result3_2= np.sum(element_multiply)
s12_3_2=0.5*0.81+0.5*result3_2/(sqrt_result3*sqrt_result2)
print(s12_3_2)
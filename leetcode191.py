def hammingWeight(n):
    # 第一种方法
    # py3中库函数
    # return bin(n).count("1")
    # 第二种方法
    # 直观统计二进制中每一位是否包含1
    return sum(1 for i in range(32) if n & (1<<i))


print(hammingWeight(0b00000000000000000000000000001011))
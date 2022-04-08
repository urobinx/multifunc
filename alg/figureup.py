import re


def two_sum(nums, target):
    """
    @param nums: list
    @param target: int
    @param dic: dict
    @param cot: default=0
    @return: str
    """

    dic = dict()
    for i, n in enumerate(nums):
        if target - n in dic:
            return "+".join([str(nums[i]), str(target - n)]) + "=" + str(target)
        dic.update({n: i})


def three_sum(nums, target, dic: dict, cot=0):
    """
    @param nums: list
    @param target: int
    @param dic: dict
    @param cot: default=0
    @return: str
    """
    sec_target = target - nums[cot]
    for i, n in enumerate(dic.keys()):
        if sec_target - n in dic:
            return "+".join([str(n), str(nums[cot]), str(sec_target - n)]) + "=" + str(target)
    dic.update({nums[cot]: cot})
    cot += 1
    return three_sum(nums, target, dic, cot)


def count_primes(n: int):
    if n < 5:
        if n < 3:
            if n < 2:
                return 0
            return 1
        return 2
    i = 2
    for num in range(1, n):
        a = 6 * num - 1
        b = 6 * num + 1
        if a < n and judge(a) is None:
            i += 1
        if b < n and judge(b) is None:
            i += 1
    return i


def judge(n):
    for i in range(3, int(n ** 0.5 + 1), 2):
        a = n % i
        if a == 0:
            return i

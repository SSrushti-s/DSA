# Boyer Moore's Voting Algorithm

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

def majority_element2(nums):
    n = len(nums)
    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')
    for num in nums:
        if cnt1 == 0 and el2 != num:
            cnt1 = 1
            el1 = num 
        elif cnt2 == 0 and el1 != num:
            cnt2 = 1
            el2 = num 
        elif num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1 
        else:
            cnt1 -= 1 
            cnt2 -= 1
    cnt1, cnt2 = 0, 0 
    for num in nums:
        if num == el1:
            cnt1 += 1 
        if num == el2:
            cnt2 += 1
    mini = n // 3 + 1
    result = []
    if cnt1 >= mini:
        result.append(el1)
        
    if cnt2 >= mini and el1 != el2:
        result.append(el2)
    return result
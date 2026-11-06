import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target=random.randint(-110,110)
        original = list(nums)
        if fn == linear_search:
            result = fn(original,target)
            if target in original:
                assert result == original.index(target), f"{fn.__name__} ошиблась {target},{result},{original}"
            else:
                assert result == -1,  f"{fn.__name__} ошиблась {target}: {result}"
        elif fn == binary_search:
            original.sort()
            sortor=original[::]
            result=fn(sortor,target)
            if target in sortor:
                assert result == sortor.index(target), f"{fn.__name__} ошиблась {target},{result},{sortor}"
            else:
                assert result == -1,  f"{fn.__name__} ошиблась {target}: {result}"

def chech_two_sum(fn1,fn2, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result1 = fn1(nums,n)
        result2 = fn2(nums,n)
        if result1!=None:
            assert nums[result1[0]]+nums[result1[1]] == nums[result1[0]]+nums[result1[1]] == n,\
              f"1 {fn1.__name__} и {fn2.__name__} не совпали: {n},{result1},{result2},{nums}"
        else: 
            assert result1==result2, f"2 {fn1.__name__} и {fn2.__name__} не совпали: {n},{result1},{result2},{nums}"

if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    print("OK: 100 проверок")
if __name__ == "__main__":
    random.seed(42)
    for fn in (linear_search, binary_search):
        check_search(fn)
    print("OK: 100 проверок")
if __name__ == "__main__":
    random.seed(42)
    chech_two_sum(two_sum_brute,two_sum_fast)
    print("OK: 100 проверок")
#     python -m src.lab07.check
import datetime

from typing import List

# list comprehension example
def doubledNums(nums: List[int]) -> List[int]:
   return [num * 2 for num in nums]; 

total_belanja = 400000

def calculate_total_price(total_belanja: int) -> float:
    discount = 0.1
    if total_belanja > 500000:
        return total_belanja - (total_belanja * discount)
    return total_belanja 

'''
    Given an array of positive integers nums and an integer k, find the length of the longest
    subarray whose sum is less than or equal to k.
'''

nums, k = [3, 1, 2, 7, 2, 2, 1, 8, 5], 8

def longest_subarray(nums: list[int], k: int) -> int:
    left = 0
    current = 0
    answer = 0
    for right in range(len(nums)):
        current = current + nums[right]
        while current > k:
            current = current - nums[left]
            left = left + 1
        answer = max(answer, right - left + 1)
    return answer 
    

def main() -> None:
    print('main execution')
    x = doubledNums([1, 2, 3, 4])
    print(x)


if __name__ == "__main__":
    main()
    # waktu = datetime.time().isoformat() 
    # print(waktu, '<< WAKTU SEKARANG')j
    print(longest_subarray(nums, k))
    

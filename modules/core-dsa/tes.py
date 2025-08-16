
'''
    Given a binary string s (a string containing only "0" and "1"). You may choose up to one
    "0" and flip it to a "1". What is the length of the longest substring achievable
    that contains only "1" ?

    for example, given s = "1101100111", the answer is 5. if you perform the flip at index 2,
    the string becomes 1111100111.
'''


def solve(s: str) -> int:
    l = 0
    zero_counter = 0
    max_length = 0
    for r in range(len(s)):
        if s[r] == "0":
            zero_counter += 1
        while zero_counter > 1:
            if s[l] == "0":
                zero_counter -= 1
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length



print(solve("1000111001101")) 

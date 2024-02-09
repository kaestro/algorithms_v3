# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/

# method 1
# create all the substrings and then calculate the beauty of each substring
# time complexity: O(n^3)
# proof: n(n+1)/2 substrings and for each substring, we need to calculate the beauty of the substring
# space complexity: O(n^2)
# proof: n(n+1)/2 substrings and each substring has a length of n

from collections import Counter

class Solution:
    def beautySum(self, input_str: str) -> int:
        # create substrings of input_str
        substrings = []
        for i in range(len(input_str)):
            for j in range(i, len(input_str)):
                substrings.append(input_str[i:j+1]) 
        
        return sum(self.calculate_beauty(substring) for substring in substrings)
    
    def calculate_beauty(self, substring: str) -> int:
        # calculate the beauty of the substring
        # create a dictionary to store the frequency of each character
        frequency = Counter(substring)
        return max(frequency.values()) - min(frequency.values())


def main():
    result = Solution().beautySum("aabcbaa")
    print(f"The sum of elements with maximum beauty is: {result}")

if __name__ == "__main__":
    main()
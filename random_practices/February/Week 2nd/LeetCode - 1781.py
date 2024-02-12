# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/

# method 1
# create all the substrings and then calculate the beauty of each substring
# time complexity: O(n^3)
# proof: n(n+1)/2 substrings and for each substring, we need to calculate the beauty of the substring
# space complexity: O(n^2)
# proof: n(n+1)/2 substrings and each substring has a length of n

# Question
# For the highest burden is on creating all the substrings, which is O(n^2)
# this is of bottleneck for the solution.
# Is there any way to reduce the time complexity of the solution?

# Answer
# Yes, we can reduce the time complexity of the solution by 'not creating all the substrings'.
# We can calculate the beauty of the substring while creating the substring.
# This improves the time complexity of the solution from O(n^3) to O(n^2)

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
    
    def advanced_beautySum(self, input_str: str) -> int:
        total_beauty = 0
        for i in range(len(input_str)):
            frequency = Counter()
            for j in range(i, len(input_str)):
                frequency[input_str[j]] += 1
                total_beauty += max(frequency.values()) - min(frequency.values())
        return total_beauty        

def main():
    result = Solution().beautySum("aabcbaa")
    print(f"The sum of elements with maximum beauty is: {result}")

if __name__ == "__main__":
    main()
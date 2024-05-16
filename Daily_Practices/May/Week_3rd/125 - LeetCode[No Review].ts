// https://leetcode.com/problems/valid-palindrome/description/

function isPalindrome(sentence: string): boolean {
    sentence = sentence.toLowerCase();
    sentence = sentence.replace(/[^a-z0-9]/g, '');

    let left = 0, right = sentence.length - 1;

    while (left < right) {
        if (sentence[left] !== sentence[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
};

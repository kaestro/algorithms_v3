// https://leetcode.com/problems/repeated-substring-pattern/description/

function repeatedSubstringPattern(sentence: string): boolean {

    let len = sentence.length;
    for (let i = 1; i <= len / 2; i++) {
        if (len % i === 0) {
            let subStr = sentence.slice(0, i);
            let j = i;
            while (j < len) {
                if (sentence.slice(j, j + i) !== subStr) {
                    break;
                }
                j += i;
            }
            if (j === len) {
                return true;
            }
        }
    }

    return false;
};

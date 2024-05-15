// https://leetcode.com/problems/reverse-vowels-of-a-string/

function reverseVowels(sentence: string): string {
    let start = 0, end = sentence.length - 1;
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let sentenceArray = sentence.split('');

    while (start < end) {
        if (vowels.includes(sentenceArray[start].toLowerCase()) && vowels.includes(sentenceArray[end].toLowerCase())) {
            swap(sentenceArray, start, end);
            start++;
            end--;
        } else if (vowels.includes(sentenceArray[start].toLowerCase())) {
            end--;
        } else {
            start++;
        }
    }

    return sentenceArray.join('');
};


function swap(arr: any[], index1: number, index2: number): void {
    let temp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = temp;
}

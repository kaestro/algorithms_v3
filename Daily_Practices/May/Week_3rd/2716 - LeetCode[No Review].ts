// https://leetcode.com/problems/minimize-string-length/description/

function minimizedStringLength(s: string): number {
    const stringArray = s.split('');
    const stringSet = new Set(stringArray);
    return stringSet.size;
};

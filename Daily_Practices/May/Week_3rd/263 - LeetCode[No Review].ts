// https://leetcode.com/problems/ugly-number/description/

function isUgly(inputNumber: number): boolean {

    if (inputNumber <= 0) return false;

    while (inputNumber > 1) {
        if (inputNumber % 2 === 0) {
            inputNumber /= 2;
        } else if (inputNumber % 3 === 0) {
            inputNumber /= 3;
        } else if (inputNumber % 5 === 0) {
            inputNumber /= 5;
        } else {
            return false;
        }
    }

    return true;
};

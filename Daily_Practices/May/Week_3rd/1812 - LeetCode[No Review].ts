// https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

function squareIsWhite(coordinates: string): boolean {

    const letter = coordinates[0];
    const number = parseInt(coordinates[1]);
    const letterIndex = letter.charCodeAt(0) - 'a'.charCodeAt(0);

    return (letterIndex + number) % 2 === 0;
};

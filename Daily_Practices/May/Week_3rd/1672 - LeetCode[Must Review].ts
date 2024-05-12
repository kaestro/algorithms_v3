// https://leetcode.com/problems/richest-customer-wealth/description/

function maximumWealth(accounts: number[][]): number {
    return accounts.reduce((maxWealth, account) => {
        const wealth = account.reduce((a, b) => a + b, 0);
        return Math.max(maxWealth, wealth);
    }, 0);
}

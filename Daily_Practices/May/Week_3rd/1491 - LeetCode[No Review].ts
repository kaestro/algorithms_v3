//https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

function average(salary: number[]): number {

    let minSalary = Math.min(...salary);
    let maxSalary = Math.max(...salary);

    let sum = salary.reduce((acc, curr) => acc + curr, 0);
    sum -= (minSalary + maxSalary);

    return sum / (salary.length - 2);
};

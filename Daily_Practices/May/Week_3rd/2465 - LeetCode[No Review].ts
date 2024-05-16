//https://leetcode.com/problems/number-of-distinct-averages/description/

function distinctAverages(nums: number[]): number {
  let uniqueAverages = new Set<number>();
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length / 2; i++) {
    const average = (nums[i] + nums[nums.length - 1 - i]) / 2;
    uniqueAverages.add(average);
  }
  return uniqueAverages.size;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    x = 0
    y = 1
    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++) {
            // if (nums[i] > target || nums[j] > target) continue;
            sum = nums[i] + nums[j]
            if (sum == target) return [i, j]
        }
    }
};
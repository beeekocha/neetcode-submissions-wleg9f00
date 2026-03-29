class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // create a dict with key = value from nums and value = it's index
        // then go through each value in nums to find if there are any key for the target - num
        // if tes, return index and value from dict

        const dict = {}

        for (let i = 0; i < nums.length; i++) {
            dict[nums[i]] = i
        }

        for (let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            if (dict[diff] && dict[diff] != i) {
                return [i, dict[diff]]
            }
        }
        return []
    }
}

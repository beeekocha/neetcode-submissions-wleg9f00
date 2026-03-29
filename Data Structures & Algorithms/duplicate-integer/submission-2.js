class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // easiest solution
        // Set contains only unique values
        // return new Set(nums).size < nums.length;

        const visited = new Set();

        for (const num of nums) {
            if (visited.has(num)) {
                return true
            }
            visited.add(num);
        }
        return false
    }
}

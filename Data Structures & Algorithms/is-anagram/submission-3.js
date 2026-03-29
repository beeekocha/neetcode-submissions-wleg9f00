class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) {
            return false
        }

        let s_sort = s.split("").sort().join("");
        console.log(s_sort);
        let t_sort = t.split("").sort().join("");
        console.log(t_sort);
        return s_sort === t_sort;
    }
}

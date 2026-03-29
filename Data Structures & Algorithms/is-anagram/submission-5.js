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

        // #1 Using sorting
        // (O(nlogn + mlogm)) T
        // (O(1) or O(n+m)) S
        // let s_sort = s.split("").sort().join("");
        // let t_sort = t.split("").sort().join("");
        // return s_sort === t_sort;

        // #2 Using hash map
        // const dictS = {};
        // const dictT = {};

        // for(let i = 0; i < s.length; i++) {
        //     dictS[s[i]] = (dictS[s[i]] || 0) + 1;
        //     dictT[t[i]] = (dictT[t[i]] || 0) + 1;
        // }

        // for (let key in dictS) {
        //     if(dictS[key] !== dictT[key]) {
        //         return false
        //     }
        // }

        // return true

        const countList = new Array(26).fill(0);

        for(let i = 0; i < s.length; i++) {
            // where s.charCodeAt(i), i - is a position of charachter in a string, and charAtCode find the value it's located
            // in an array of strings
            countList[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            countList[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }

        return countList.every(val => val === 0)
    }
}

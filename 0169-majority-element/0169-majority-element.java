import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> count = new HashMap<>();
        int max_count =0;
        int target= nums[0];
        int i=0;
        while(i<nums.length){
            int val = count.getOrDefault(nums[i],1)+1;
            count.put(nums[i], val);

            if(val > (nums.length / 2) ) {
                return nums[i];
            }
            i++;
        }
        return target;
    }
}
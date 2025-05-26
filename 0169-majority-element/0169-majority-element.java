import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> count = new HashMap<>();
        int i=0;
        while(i<nums.length){
            count.put(nums[i],count.getOrDefault(nums[i],0)+1);
            i++;
        }
        for(Integer j: count.keySet()){
            // System.out.println(count.get(j)+""+count);
            if(count.get(j)>nums.length/2){
                return j;
            }
        }
        return 0;
    }
}
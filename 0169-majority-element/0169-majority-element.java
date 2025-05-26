import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> count = new HashMap<>();
        int max_count =0;
        int target= nums[0];
        int i=0;
        while(i<nums.length){
            if(count.containsKey(nums[i])) {
               int counter =  count.get(nums[i]) + 1;
               count.put(nums[i], counter);
               if(counter > max_count) {
                max_count = counter;
                target = nums[i];
               } 
            } else {
              count.put(nums[i],1);
            }
            i++;
        }
        /*for(Integer j: count.keySet()){
            // System.out.println(count.get(j)+""+count);
            if(count.get(j)>nums.length/2){
                return j;
            }
        }*/
        return target;
    }
}
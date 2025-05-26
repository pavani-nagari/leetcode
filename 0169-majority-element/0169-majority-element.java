import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> count = new HashMap<>();
        int max_count =0;
        int target= nums[0];
        int i=0;
        while(i<nums.length){
            int val = count.getOrDefault(nums[i],0)+1;
            count.put(nums[i], val);

            if(val > max_count && val > (nums.length / 2) ) {
                max_count = val;
                target = nums[i];
                break;
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
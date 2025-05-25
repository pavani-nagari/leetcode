/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 import java.util.*;
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        /*HashSet<ListNode> hash = new HashSet<>();
        while(headA !=null){
            hash.add(headA);
            headA = headA.next;
        }
        while(headB != null){
            if(hash.contains(headB)){
                return headB;
            }
            else{
                headB = headB.next;
            }
        }
        return headB;

        */
        ListNode listA = headA;
        ListNode listB = headB;
        while(listA != listB) {
            listA = listA != null ? listA.next: headA;
            listB = listB != null ? listB.next: headB;
        }
        return listA;
    }
}
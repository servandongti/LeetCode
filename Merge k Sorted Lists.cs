public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        if(lists==null || lists.Length==0)
            return null;
        
        while(lists.Length>1)
        {
            List<ListNode> temp=new List<ListNode>();
            
            for(int i=0;i<lists.Length;i=i+2)
            {
                ListNode l1=lists[i];
                ListNode l2 = (i+1<lists.Length)?lists[i+1]:null;
                temp.Add(mergeTwoLists(l1,l2));
            }
            lists=temp.ToArray<ListNode>();
        }
        
        return lists[0];
        
        ListNode mergeTwoLists(ListNode l1, ListNode l2)
        {
            ListNode dummy=new ListNode();
            ListNode temp = dummy;
            while(l1!=null && l2!=null)
            {
                if(l1.val>l2.val)
                {
                    temp.next=l2;
                    l2=l2.next;
                }
                else
                {
                    temp.next=l1;
                    l1=l1.next;
                }
                temp=temp.next;
            }
            
            if(l1!=null)
                temp.next=l1;
            if(l2!=null)
                temp.next=l2;
            
            return dummy.next;
        }
    }
}
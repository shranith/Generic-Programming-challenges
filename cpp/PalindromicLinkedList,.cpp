/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *fast,*slow,*head2,*p,*q;
        if(head == NULL || head->next == NULL)
            return true;
        if(head->next->next == NULL)
        {
            if(head->val == head->next->val)
                return true;
            else 
                return false;
        }
        fast = slow = head;
        int flag = 0;
        while(fast!=NULL)
        {   if(fast->next == NULL)
                break;
            slow = slow->next;
            fast = fast->next->next;
        }
        head2 = reverseList(slow);
        p = head;
        q = head2;
        
            while(q!=NULL)
            {
                if(p->val != q->val)
                    return false;
                    p = p->next;
                    q = q->next;
            }
            return true;
            
        
        
    }
    ListNode* reverseList(ListNode* head) {
      if(head == NULL || head->next == NULL)
        return head;
        ListNode *p,*q,*r;
        p = head;
        q = head->next;
        if(q->next == NULL){
        p->next = NULL;q->next = p;return q;}
        r = q->next;
        p->next =NULL;
        while(r!=NULL)
        {
            q->next = p;
            p = q;
            q = r;
            r = q->next;
    
        }
        q->next = p;
        return q;
        
        
        
    }
};

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

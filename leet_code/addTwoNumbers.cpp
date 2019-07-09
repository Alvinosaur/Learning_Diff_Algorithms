#include <cmath>
#include <iostream>

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

/*
 Problem with this is the possibility of integer overflow with failure when the inputs
 are 9999999 and 9999999.

 Learned to use "new ListNode(val)" instead of malloc.
*/
ListNode* addTwoNumbers1(ListNode* l1, ListNode* l2) {
    int scaled_val = 0, trueVal = 0, digit = 0;
    int l1_size = 0, l2_size = 0;
    ListNode *cur = NULL, *prev = NULL, *result = NULL;
    
    // Add in the first number's digits
    int power_l1 = 0;
    for (cur = l1; cur != NULL; cur = cur->next) {
        scaled_val = cur->val * pow(10, power_l1);
        trueVal += scaled_val;
        power_l1++;
    }
    
    // Second number
    int power_l2 = 0;
    for (cur = l2; cur != NULL; cur = cur->next) {
        scaled_val = cur->val * pow(10, power_l2);
        trueVal += scaled_val;
        power_l2++;
    }
    
    // Store result
    cur = NULL;
    while (trueVal > 0) {
        digit = trueVal % 10;
        std::cout << digit << std::endl;
        trueVal = trueVal / 10;
        cur = new ListNode(digit);
        // cur->val = digit;
        if (prev == NULL) {
            prev = cur;
            result = cur;
        }
        else {
            prev->next = cur;
            prev = cur;
        }
    }
    return result;
}

/* 
    Edge cases: 99999999 + 9999999999
    0 + 189
    5 + 5
*/
ListNode* addTwoNumbers2(ListNode* l1, ListNode* l2) {
    ListNode *result = NULL, *prev = NULL;
    int carry = 0;
    while (l1 != NULL || l2 != NULL) {
        int l1_val = (l1 != NULL) ? l1->val : 0;
        int l2_val = (l2 != NULL) ? l2->val : 0;
        int sum = l1_val + l2_val + carry;

        carry = sum / 10;  // 16/10 = 1
        if (carry) sum = sum % 10;  // 16 % 10 = 6
        std::cout << sum << std::endl;

        ListNode *node = new ListNode(sum);
        if (prev == NULL) result = node;
        else prev->next = node;
        prev = node;

        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }
    if (carry) {
        ListNode *node = new ListNode(1);
        prev->next = node;
    }
    return result;
}



int main() {
    ListNode *l1_1 = new ListNode(2);
    ListNode *l1_2 = new ListNode(4);
    ListNode *l1_3 = new ListNode(3);
    l1_1->next = l1_2;
    l1_2->next = l1_3;

    ListNode *l2_1 = new ListNode(5);
    ListNode *l2_2 = new ListNode(6);
    ListNode *l2_3 = new ListNode(4);
    l2_1->next = l2_2;
    l2_2->next = l2_3;
    ListNode *result = addTwoNumbers2(l1_1, l2_1);
    return 0;
}
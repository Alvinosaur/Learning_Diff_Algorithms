#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

typedef struct Node Node_t;

struct Node
{
    int data;
    Node_t* npx;
};

Node_t* XOR(Node_t* a, Node_t* b) {
    return (Node_t*)((size_t)(void*)a ^ (size_t)(void*)b);
}

void insert(Node_t **head_ref, int data) {
    Node_t* new_node = (Node_t*)malloc(sizeof(Node_t));
    if (new_node == NULL) exit(-1);
    new_node->data = data;
    new_node->npx = XOR(NULL, head_ref);
    if (head_ref != NULL) {
        Node_t* next = XOR((*head_ref)->npx, NULL);  // filter out NULL
        (*head_ref)->npx = XOR(next, new_node);
    }
    // need **head_ref since if we only had *head_ref, we would be assigning
    // local variable pointer to new_node and not truly modifiying the 
    // head_ref passed in
    *head_ref = new_node;  
}
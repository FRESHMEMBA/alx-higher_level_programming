#include <lists.h>

/*
 * check_cycle - Checks if a linked list has cycle
 * @list: The linked list to be checked if it has a cycle.
 * Return: 1 if list has a cyclec, otherwise returns 0.
 */
int check_cycle(listint_t *list) {
    /*Initialize two pointers, slow and fast*/
    listint_t *slow = list;
    listint_t *fast = list;

    /*Traverse the list using slow and fast pointers*/
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;          /*Move slow pointer one step*/
        fast = fast->next->next;    /*Move fast pointer two steps*/

        /*If there is a cycle, slow and fast pointers will meet*/
        if (slow == fast) {
            return 1; /*There is a cycle*/
        }
    }

    return 0; /*No cycle found*/
}

#include "lists.h"

/*
 * insert_node - Inserts a number into a ordered singly linked lists
 * @head: Pointer to the first node of the ordered singly linked list
 * @number: Number to be inserted into the ordered singly linked list
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = (listint_t *)(malloc)(sizeof(listint_t));
    listint_t *current = *head;

    if (!new_node) {
	    return NULL;
    }

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->n) {
	    new_node->next = *head;
	    *head = new_node;
	    return new_node;
    }

    while(current->next != NULL && current->next->n < number) {
	    current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;
    return new_node;
}

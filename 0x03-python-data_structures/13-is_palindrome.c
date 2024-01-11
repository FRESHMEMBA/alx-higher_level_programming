#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the linked list to be reversed
 * Return: the reversed linked list.
 */
listint_t *reverse_list(listint_t *head) {
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL) {
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the list to checked if its a palindrome
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head) {
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *first_half;

	if (*head == NULL || (*head)->next == NULL) {
		return (1);
	}

	while (fast != NULL && fast->next != NULL) {
		fast = fast->next->next;
		slow = slow->next;
	}

	/*reversing the second half of the linked list*/
	second_half = reverse_list(slow);
	first_half = *head;

	while (second_half != NULL) {
		if (first_half->n != second_half->n) {
			return (0);
		}

		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}

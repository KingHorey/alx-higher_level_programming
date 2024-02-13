#include "lists.h"
#include <string.h>

/**
 * is_palindrome - checks if a linked list is a
 * palindrome
 *
 *@head: head of the linked list
 *Return: 0 if it is not a linked list and 1 if it is
 */

int is_palindrome(listint_t **head)
{
	// printf("Mem addr: %p/n", &(**head));
	if (*head == NULL)
		return (0);
	else if ((*head)->next == NULL)
		return (1);
	listint_t *ptr, **ptr_data;
	int ptr_check;

	ptr = *head;
	ptr_data = head;
	ptr_check = recurse(ptr_data, ptr);
	if (ptr_check)
		return (ptr_check);
	return (0);
}

/**
 * recurse - recurse the linked list till end
 * @ptr_head - a pointer to the head of the linked list
 * @ptr: pointer to the head of the linked list
 *
 * Return: NULL if pointer is NULL or ptr at end of noode
 */

int recurse(listint_t **ptr_head, listint_t *ptr)
{
	int result_checker, final_result;

	if (ptr == NULL)
		return (1);
	result_checker = recurse(ptr_head, ptr->next);
	*ptr_head = (*ptr_head)->next;
	if (result_checker == 0)
		return 0;
	final_result = (*ptr_head)->n == ptr->n;
	*ptr_head = (*ptr_head)->next;

	return (final_result);

}


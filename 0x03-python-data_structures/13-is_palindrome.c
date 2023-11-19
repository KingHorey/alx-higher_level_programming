#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a
 * palindrome
 *
 *@head: head of the linked list
 *Return: 0 if it is not a linked list and 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (0);
	else if ((*head)->next == NULL)
		return (1);
	listint_t *ptr, *ptr_data;

	ptr = *head;
	ptr_data = *head;
	ptr = recurse(ptr);
	while (ptr_data && ptr)
	{
		if (ptr_data->n == ptr->n)
		{
			if (ptr_data->next == NULL)
				return (1);
		}
		if (ptr_data->n != ptr->n)
			return (0);
		ptr_data = ptr_data->next;
	}
	return (0);
}

/**
 * recurse - recurse the linked list till end
 *
 * @ptr: pointer to the head of the linked list
 *
 * Return: NULL if pointer is NULL or ptr at end of noode
 */

listint_t *recurse(listint_t *ptr)
{
	if (ptr->next == NULL)
		return (ptr);
	ptr = ptr->next;
	return (recurse(ptr));
}


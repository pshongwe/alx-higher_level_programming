#include "lists.h"

/**
 * check_cycle - checks if linked list has cycle
 * @list: pointer to linked list to check
 * Return: 0 (no cycle), 1 (has cycle)
 */
int check_cycle(listint_t *list)
{
	int first_value;
	listint_t *current = NULL;

	first_value = list->n;
	current = list->next;
	while (current != NULL)
	{
		if (current->n == first_value)
			return (1);
		current = current->next;
	}
	return (0);
}

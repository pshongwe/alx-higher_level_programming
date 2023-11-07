#include "lists.h"

/**
 * is_palindrome - check if list data
 * is a palindrome
 * @head: pointer to head of list
 * Return: 1 (true), 0 (false)
 */
int is_palindrome(listint_t **head)
{
int *int_array, left = 0, right = 0;
unsigned int len = 0, count = 0;
listint_t *current = *head;

if (*head == NULL)
	return (1);
while (current != NULL)
{
	len++;
	current = current->next;
}
int_array = (int *)malloc(sizeof(int) * len);
if (int_array == NULL)
	return (-1);
current = *head;
while (current != NULL)
{
	int_array[count] = current->n;
	count++;
	current = current->next;
}
right = len - 1;
while (left < right)
{
	if (int_array[left] != int_array[right])
	{
		free(int_array);
		return (0);
	}
	left++;
	right--;
}
free(int_array);
return (1);
}

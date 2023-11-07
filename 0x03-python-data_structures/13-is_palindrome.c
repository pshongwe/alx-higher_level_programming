#include "lists.h"

/**
 * is_palindrome - check if list data
 * is a palindrome
 * @head: pointer to head of list
 * Return: 1 (true), 0 (false)
 */
int is_palindrome(listint_t **head)
{
listint_t *next_node = NULL;
listint_t *slow = *head, *fast = *head, *prev = NULL;
listint_t *first_half = *head, *second_half = NULL;

if (*head == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast != NULL)
slow = slow->next;
prev = NULL;
while (slow != NULL)
{
next_node = slow->next;
slow->next = prev;
prev = slow;
slow = next_node;
}
second_half = prev;
while (second_half != NULL)
{
if (first_half->n != second_half->n)
return (0);
first_half = first_half->next;
second_half = second_half->next;
}
return (1);
}

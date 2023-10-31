#include "lists.h"

/**
 * check_cycle - checks if linked list has cycle
 * @list: pointer to linked list to check
 * Return: 0 (no cycle), 1 (has cycle)
 */
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

if (head == NULL)
return (NULL);

slow = head;
fast = head;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
slow = head;
while (slow != fast)
{
slow = slow->next;
fast = fast->next;
}
return (slow);
}
}
return (NULL);
}

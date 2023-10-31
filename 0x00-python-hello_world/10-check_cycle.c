#include "lists.h"

/**
 * check_cycle - checks if linked list has cycle
 * @list: pointer to linked list to check
 * Return: 0 (no cycle), 1 (has cycle)
 */
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;

if (list == NULL)
return (0);

slow = list;
fast = list->next;
while (fast && slow && fast->next)
{
if (slow == fast)
return (1);
slow = slow->next;
fast = fast->next->next;
}
return (0);
}

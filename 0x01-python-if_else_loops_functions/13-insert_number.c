#include "lists.h"

/**
 * insert_node - inserts new node
 * @head: pointer to linked list
 * @number: number to insert/store
 * Return: head
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head, *new_node;

new_node = malloc(sizeof(listint_t));
if (!new_node)
return (NULL);
new_node->n = number;
if (!current || current->n >= number)
{
new_node->next = current;
*head = new_node;
return (new_node);
}
while (current && current->next && current->next->n < number)
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
return (new_node);
}

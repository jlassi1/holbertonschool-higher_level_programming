#include "lists.h"
/**
  *insert_nodeint_at_index- inserts a new node at a given position.
  *@head: nodes of linked list
  *@idx: the index of the list where the new node should be added
  *@n: integer of new node to add
  *Return: the address of the new node
  */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
listint_t *new_node;
listint_t *temp;
unsigned int i = 0;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

if (idx == 0)
{
new_node->next = *head;
new_node->n = n;
*head = new_node;
return (new_node);
}

temp = *head;

while (temp != NULL)
{

if (i == idx - 1)
{
new_node->next = temp->next;
new_node->n = n;
temp->next = new_node;
return (new_node);
}

temp = temp->next;
i++;
}
return (NULL);
}
#include "lists.h"
/**
  *insert_node-  adds number to the listint_t
  *@head: pointer to nodes of list
  *@number: integer to add to the node
  *Return: node
  */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *temp = *head, *current;


new_node = malloc(sizeof(lisbtint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (!*head)
{
*head = new_node;
return (new_node);
}
if (temp->n > number)
{
new_node->next = *head;
*head = new_node;
}

else
{

while (temp)
{
if (temp->n > number)
break;
current = temp;
temp = temp->next;
}

new_node->next = current->next;
current->next = new_node;
}

return (new_node);
}

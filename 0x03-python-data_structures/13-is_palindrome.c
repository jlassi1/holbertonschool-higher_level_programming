#include "lists.h"
/**
 *palindrome_check - fun
 *@s: char
 *@i: integer
 *Return: 0 or 1 or result of check
 */
int palindrome_check(char *s, int i)
{
	if (i <= 1)
		return (1);
	else if (*s == s[i - 1])
		return (palindrome_check(s + 1, i - 2));
	else
		return (0);
}
/**
 *is_palindrome-checks if a singly linked list is a palindrome.
 *
 *@head: pointer to linked list
 *
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
int i = 1, j = 0, x;
	while (tmp)
	{
		tmp = tmp->next;
		i++;
	}
	if (i <= 1)
		return (1);
tmp = *head;
char *array = malloc(sizeof(int) * i + 1);
	while (tmp)
	{
		array[j] = tmp->n;
		tmp = tmp->next;
		j++;
	}

		x = palindrome_check(array, j);

return (x);
}

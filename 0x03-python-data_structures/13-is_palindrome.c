#include "lists.h"
/**
 * check_palindrome - checks array to see if palindrome
 * @arr: array of integers
 * @length: length of palindrome
 *
 * Return: 1 if palindrome. 0 if not palindrome.
 */
int check_palindrome(int *arr, int len)
{
	unsigned int i = 0;

	while (arr[i] <= arr[len])
	{
		if (arr[i] != arr[len])
			return (0);
		i++;
		len--;
	}
	return (1);

}
/**
 * palindrome_length - finds length of palindrome
 * @head: pointer to linked list
 *
 * Return: length
 */
int palindrome_length(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}


/**
 * is_palindrome - checks a singly linked list to see if palindrome
 * @head: points to head of list
 *
 * Return: 1 if palindrome. Otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *list_arr;
	unsigned int len = 0;
	unsigned int i = 0;

	tmp = *head;
	if (*head == NULL)
		return (1);
    while (tmp != NULL)
	{
		tmp = tmp->next;
		len++;
	}

	if (len == 0)
		return (1);

	list_arr = malloc(sizeof(int) * len);
	if (list_arr == NULL)
		return (0);

	while (tmp != NULL)
	{
		list_arr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}

	if (check_palindrome(list_arr, len) == 0)
		return (0);
	return (1);

}
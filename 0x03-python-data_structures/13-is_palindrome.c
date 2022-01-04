#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - function to check if a SLL is palindrome
 * @head: head of the list
 * Return: 1 (Palindrome) 0 (Not palindrome)
 **/
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int array[5000];
	int i = 0;
	int j = 0;

	if (!(*head))
		return (1);
	for (i = 0; current; i++)
	{
		array[i] = current->n;
		current = current->next;
	}
	for (j = 0; j < i; i--, j++)
	{
		if (array[j] != array[i - 1])
			return (0);
	}
	return (1);
}

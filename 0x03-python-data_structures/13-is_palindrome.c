#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head pointer
 * Return: 1 (If palindrome 0 Otherwise)
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy;
	int count = 0, half, i, arr[3000] = {0};

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	copy = *head;
	for (count = 0; copy != NULL; count++)
		copy = copy->next;
	copy = *head;
	half = count / 2;
	for (i = 0; i < half; i++)
		copy = copy->next;
	if (count % 2 == 1)
		copy = copy->next;
	/*if (!arr)*/
	/*	exit(1);*/
	for (i = half - 1; i >= 0; i--)
	{
		arr[i] = copy->n;
		copy = copy->next;
	}
	copy = *head;
	for (i = 0; i < half; i++)
	{
		if (copy->n != arr[i])
		{
			/*free(arr);*/
			return (0);
		}
		copy = copy->next;
	}
	/*free(arr);*/
	return (1);
}
int main()
{
	listint_t *c = NULL;

	printf("%i", is_palindrome(&c));
	return (0);
}

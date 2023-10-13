#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: pointer to a struct
 * Return: number of elements in a linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t sum = 0;
	const dlistint_t *first = h;

	while (first != NULL)
	{
		printf("%d\n", first->n);
		first = first->next;
		sum++;
	}
	return (sum);
}

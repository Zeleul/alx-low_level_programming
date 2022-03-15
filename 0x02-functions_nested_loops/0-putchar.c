#include <unistd.h>
#include "main.h"
/**
 *main - entry point
 *
 *Description: prints _putchar followed by a newline
 *
 *Return: returns 0(successful)
 *
 */
int main(void)
{
	char putcharText[8] = "_putchar";
	int i;

	for (i = 0; i < 8; i++)
	{
		_putchar(putcharText[i]);
	}
	_putchar('\n');
	return (0);
}

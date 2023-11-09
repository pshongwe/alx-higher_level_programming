#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Print information
 * about a Python bytes object.
 * @p: A Python object to be examined.
 */
void print_python_bytes(PyObject *p)
{
long int size, lim, x;
char *buffer;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
bytes = ((PyVarObject *)(p))->ob_size;
buffer = ((PyBytesObject *)p)->ob_sval;
printf("  size: %ld\n", bytes);
printf("  trying string: %s\n", buffer);
printf("  first 10 bytes: ");
for (i = 0; i < 10 && i < bytes; i++)
{
printf("%02x", (unsigned char)bytes->ob_sval[i]);
if (i < size - 1)
printf(" ");
}
printf("\n");
}


/**
 * print_python_list - Print information
 * about a Python list object.
 * @p: A Python object to be examined.
 */
void print_python_list(PyObject *p)
{
PyListObject *list;
PyObject *elem;
long int x, size;

list = (PyListObject *)p;
size = ((PyVarObject *)(p))->ob_size;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);
for (x = 0; x < size; x++)
{
elem = ((PyListObject *)p)->ob_item[x];
printf("Element %ld: %s\n", x);
if (PyBytes_Check(elem))
			print_python_bytes(elem);
}
}


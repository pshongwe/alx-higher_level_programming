#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: A Python object to be examined.
 */
void print_python_bytes(PyObject *p)
{
long int bytes, lim, x;
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

lim = (bytes >= 10) ? 10 : bytes + 1;
printf("  first %ld bytes: ", lim);

for (x = 0; x < lim; x++)
{
printf("%02x", (unsigned char)buffer[x]);
if (x < lim - 1)
printf(" ");
}

printf("\n");
}

/**
 * print_python_list - Print information about a Python list object.
 * @p: A Python object to be examined.
 */
void print_python_list(PyObject *p)
{
long int x, size;
PyObject *elem;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = ((PyVarObject *)(p))->ob_size;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);

for (x = 0; x < size; x++)
{
elem = ((PyListObject *)(p))->ob_item[x];

printf("Element %ld: %s\n", x, elem->ob_type->tp_name);

if (PyBytes_Check(elem))
print_python_bytes(elem);
}
}

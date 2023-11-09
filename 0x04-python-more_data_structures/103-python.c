#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information
 * about a Python bytes object.
 * @p: A Python object to be examined.
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;

    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < PyBytes_Size(p); i++)
    {
        printf("%02x", (unsigned char)bytes->ob_sval[i]);
        if (i < PyBytes_Size(p) - 1)
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

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
    {
        PyObject *elem = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(elem))
        {
            print_python_bytes(elem);
        }
        else if (PyLong_Check(elem))
        {
            printf("int\n");
        }
        else if (PyFloat_Check(elem))
        {
            printf("float\n");
        }
        else if (PyTuple_Check(elem))
        {
            printf("tuple\n");
        }
        else if (PyList_Check(elem))
        {
            printf("list\n");
        }
        else if (PyUnicode_Check(elem))
        {
            printf("str\n");
        }
        else
        {
            printf("unknown\n");
        }
    }
}


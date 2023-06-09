#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the python object
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid object passed. Expected a list.\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyObject *pyobj;
	unsigned int idx = 0;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", (((PyListObject *)(p))->allocated));
	while (idx < size)
	{
		pyobj = PyList_GetItem(p, idx);
		printf("Element %i: %s\n", idx, Py_TYPE(pyobj)->tp_name);
		idx++;
	}
}

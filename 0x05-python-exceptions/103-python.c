#include <Python.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	char *str = ((PyBytesObject *)p)->ob_sval;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size + 1 < 10 ? size + 1 : 10);

	for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" %02hhx", str[i]);
	}

	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double value = ((PyFloatObject *)p)->ob_fval;
	printf("[.] float object info\n");
	printf("  value: %g\n", value);
}

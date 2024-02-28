#include <Python.h>


/**
 * Print a Python string object.
 *
 * This function takes a PyObject pointer as input and checks
 * if the object is a Unicode string.
 * If it is, the function retrieves the UTF-8 representation of the
 * string and prints it.
 * If the UTF-8 representation cannot be decoded, an error message is printed.
 * If the object is not a Python string, an error message is printed.
 *
 * @p (PyObject*): A pointer to the Python string object to be printed.
 *
 * Returns: None
 */
void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {  // Check if the object is a Unicode string
        const char *str = PyUnicode_AsUTF8(p);
        if (str != NULL) {
            printf("%s\n", str);  // Print the UTF-8 string
        } else {
            printf("Failed to decode UTF-8\n");
        }
    } else {
        printf("Object is not a Python string\n");
    }
}

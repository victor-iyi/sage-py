//
//  sagemodule.cc
//  C API For Python
//
//  Created by Victor I. on 3/23/18.
//  Copyright (c) 2018 V.I.C.T.O.R. All rights reserved.
//

#include <Python.h>
#include "sage.hpp"

// Help.
/*
SPECIAL METHODS TO NOTE:
 1. PyObject => Super class of all python objects, equivalent to `object` in
Python

 2. PyArg_ParseTuple => Parses arguments from Python into C or C++ Program.
    arg1 -> PyObject -> argument to be parsed.
    arg2 -> char -> "i" for integer, "d" for double, "l" for long, "s" for
string etc. arg3 -> other arguments you need in your function. In this case;
it'll be the number to be passed in, into our fibonacci function.

 3. Py_BuildValue -> Converts a regular C or C++ data type into a Python object
or PyObject arg1 -> char -> "i" for integer, "c" for char, "s" for string etc.
    arg2 -> The value you want to convert.
*/

static PyObject* SageError;

static int numargs = 0;

static PyObject* emb_numargs(PyObject* self, PyObject* args) {
  if (!PyArg_ParseTuple(args, ":numargs")) return NULL;

  return PyLong_FromLong(numargs);
}

/* Python Bindings for `method` function. */
static PyObject* method(PyObject* self, PyObject* args) {
  // Declare the integer argument.
  int n;

  // NOTE: i => integer, s => string, f => float etc.
  // Parse argument from Python into our C program.
  if (!PyArg_ParseTuple(args, "i", &n)) return NULL;

  // NOTE: i => integer, s => string, d => double etc.
  // Convert the result into a PyObject.
  return Py_None;
}

/* Versioning. */
static PyObject* sageVersion(PyObject* self) {
  // Version name (as a string).
  const char* versionName = "1.0.0";
  // Convert the result into a PyObject.
  return Py_BuildValue("s", versionName);
}

/*
 The Module's Method Table and Initialization Function

 Pattern: Python-function-name, Actual-C-function, Function-Type, Documentation.
 */
static PyMethodDef SageMethods[] = {

    // Expose API for method. -> function.
    {"method", method, METH_VARARGS, "Calculate the nth fibonacci number."},

    // Expose API for numargs -> function.
    {"numargs", emb_numargs, METH_VARARGS,
     "Return the number of arguments from command line."},

    // Expose API for version -> function.
    {"version", (PyCFunction)sageVersion, METH_NOARGS, "Returns the version."},

    // House-keeping: Null terminating entry.
    {NULL, NULL, 0, NULL} /* Sentinel marker. */
};

/* Module definition structure. */
static struct PyModuleDef SageModule = {
    PyModuleDef_HEAD_INIT, "sage", /* name of module. */
    PROJECT_DESCRIPTION,           /* module documentation, may be NULL. */
    -1,                            /* size of per-interpreter state of the module,
                                      or -1 if the module keeps state in global variables. */
    SageMethods                    /* method table. */
};

/* Module's Initialization function */
PyMODINIT_FUNC PyInit_sage(void) {
  PyObject* m;
  m = PyModule_Create(&SageModule);

  if (m == NULL) return NULL;

  SageError = PyErr_NewException("sage.error", NULL, NULL);
  Py_INCREF(SageError);
  PyModule_AddObject(m, "error", SageError);

  return m;
}

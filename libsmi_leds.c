#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdbool.h>
#include "rpi_pixleds_lib.h"


PyObject *smi_leds_leds_init(PyObject *self, PyObject *args)
{
    int num_leds;
    int brightness;
    bool ret;

    if (!PyArg_ParseTuple(args, "ii", &num_leds, &brightness))
        return NULL;

    ret = leds_init(num_leds, brightness);
    return PyBool_FromLong(ret);
}

PyObject *smi_leds_leds_brightness(PyObject *self, PyObject *args)
{
    int brightness;

    if (!PyArg_ParseTuple(args, "i", &brightness))
        return NULL;

    leds_brightness(brightness);
    Py_RETURN_NONE;   
}

PyObject *smi_leds_leds_clear(PyObject *self, PyObject *args)
{
    leds_clear();
    Py_RETURN_NONE;   
}

PyObject *smi_leds_leds_set(PyObject *self, PyObject *args)
{
    Py_buffer buffer;

    if (!PyArg_ParseTuple(args, "y*", &buffer))
        return NULL;

    leds_set((color_t *)buffer.buf);
    PyBuffer_Release(&buffer);

    Py_RETURN_NONE;   
}

PyObject *smi_leds_leds_send(PyObject *self, PyObject *args)
{
    leds_send();
    Py_RETURN_NONE;   
}

pypxlib
=======

| Python bindings for the `pxlib library`_ for reading and writing Paradox
  databases.

| The version of pxlib currently exposed by pypxlib is 0.6.8 (0.6.5 for 
  macOS).

.. _`pxlib library`: http://pxlib.sourceforge.net/

Installation
============
.. code:: bash

    pip install pypxlib

Usage
=====

pypxlib exposes a high-level API for reading Paradox databases. To use
this API, you need the following import:

.. code:: python

    from pypxlib import Table

Get the fields in a table:

.. code:: python

    >>> table = Table('data.db')
    >>> table.fields
    OrderedDict([('field1', <pypxlib.LongField object at 0x1072c6710>),
    ('field2', <pypxlib.AlphaField object at 0x10731ffd0>)]

Get the number of rows:

.. code:: python

    >>> len(table)
    123

Get the first row:

.. code:: python

    >>> row = table[0]
    >>> row
    Row(field1=13, field2='foo')

Access a row’s properties:

.. code:: python

    >>> row.field1
    13
    >>> row['field1']
    13

Iterate over all rows:

.. code:: python

    >>> for row in table:
    ...    print(row)
    ...
    Row(field1=13, field2='foo')
    Row(field2=87, field2='bar')
    ...

There is limited support for modifying tables:

.. code:: python

    >>> row = table[0]
    >>> row.field1 = 20
    >>> row.save()
    >>> table[0]
    20

Do note that you must call ``.save(...)`` on the exact ``Row`` object that you
modified. That is, the following *will not work*:

.. code:: python

    >>> # This does not work!
    >>> table[0].field1 = 20
    >>> table[0].save()

Rows can also be inserted. This is done by passing a tuple of objects to
``table.insert(...)``. The elements of the tuple must have exactly the types
given by the table's ``.fields`` property:

.. code:: python

    >>> table.fields
    OrderedDict([('field1', <pypxlib.LongField object at 0x1072c6710>),
    ('field2', <pypxlib.AlphaField object at 0x10731ffd0>)]
    >>> table.insert((50, 'Some text'))
    2
    >>> table[2]
    Row(field1=50, field2='Some text')

Deleting a row can be done via the ``del`` keyword:

.. code:: python

    >>> del table[2]

Finally, don't forget to close the table when you are done!

.. code:: python

    table = Table('data.db')
    try:
        # Process the table...
    finally:
        table.close()

Or use it as a context manager:

.. code:: python

    with Table('data.db') as table:
        # Process the table...

Access to pxlib via ctypes
--------------------------

pypxlib is esentially a thin wrapper around the pxlib C library. The
high-level API described above makes it easy to read tables but offers limited
support when it comes to writing tables. If you also need to write to a table,
or another more complicated use case, then you can fall back to the ctypes
bindings of pxlib exposed by this library:

.. code:: python

    from pypxlib.pxlib_ctypes import *

    pxdoc = PX_new()
    PX_open_file(pxdoc, b"test.db")

    num_fields = PX_get_num_fields(pxdoc)
    print('test.db has %d fields:' % num_fields)

    for i in range(num_fields):
        field = PX_get_field(pxdoc, i)
        print(field.contents.px_fname)

    # Close the file:
    PX_close(pxdoc)
    # Free the memory associated with pxdoc:
    PX_delete(pxdoc)

All the ``PX_...`` functions come directly from the `list of pxlibs functions`_.
Note that you do not need to call ``PX_boot()`` and ``PX_shutdown``, as these
functions are already called when importing ``pypxlib``, and via an
``atexit`` handler.

.. _`list of pxlibs functions`: http://pxlib.sourceforge.net/documentation.php

Platforms
=========

This library was tested on the following platforms:

* **Windows 10 (64 bit)**: 32 and 64 bit Python 2.7.17 and 3.8.2.
* **OS X**: Python 2.7.10 and 3.4.2.
* **Ubuntu 18.04.4**: 32 and 64 bit Python 2.7.17 and 3.7.5.

Dynamic libraries in this repository
====================================

The dynamic libraries ``libpx.so`` (``libpx_x64.so``) and ``pxlib.dll`` 
(``pxlib_x64.dll``) were obtained by building pxlib 0.6.8 on Ubuntu 18.04.4 LTS.
MinGW was used for cross-compiling to Windows.

The library ``libpx_x64.dylib`` was obtained by building pxlib 0.6.5 on 
Mac OS X 10.10.5.

See *Building pxlib* below.

Building pxlib
==============

This project contains dynamic libraries for version 0.6.8 / 0.6.5 of the pxlib
library. The steps that were necessary to compile the library on the various 
operating systems are documented in `BUILD.rst <BUILD.rst/>`_.


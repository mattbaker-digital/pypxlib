Building pxlib
==============

Ubuntu 18.04.4 LTS (64-bit)
---------------------------

Native 64-bit Library
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    sudo apt-get update
    sudo apt-get install build-essential intltool
    wget 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.8/pxlib-0.6.8.tar.gz?ts='`date +%s`'&use_mirror=freefr' -O pxlib-0.6.8.tar.gz
    tar -zxvf pxlib-0.6.8.tar.gz
    cd pxlib-0.6.8/
    ./configure
    make
    strip src/.lib/libpx.so.0.6.8

Copy ``src/.lib/libpx.so.0.6.8`` to the pypxlib module's ``pxlib_ctypes`` 
directory and rename to ``libpx_x64.so``.

Native 32-bit Library
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    sudo apt-get update
    sudo apt-get install build-essential intltool gcc-multilib
    wget 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.8/pxlib-0.6.8.tar.gz?ts='`date +%s`'&use_mirror=freefr' -O pxlib-0.6.8.tar.gz
    tar -zxvf pxlib-0.6.8.tar.gz
    cd pxlib-0.6.8/
    ./configure --host=i686-linux-gnu "CFLAGS=-m32" "LDFLAGS=-m32"
    make
    strip src/.lib/libpx.so.0.6.8

Copy ``src/.lib/libpx.so.0.6.8`` to the pypxlib module's ``pxlib_ctypes`` 
directory and rename to ``libpx.so``.

Cross-Compiled 64-bit Windows Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    sudo apt-get update
    sudo apt-get install gcc-mingw-w64 intltool make **winiconvthingy**
    wget 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.8/pxlib-0.6.8.tar.gz?ts='`date +%s`'&use_mirror=freefr' -O pxlib-0.6.8.tar.gz
    tar -zxvf pxlib-0.6.8.tar.gz
    cd pxlib-0.6.8/
    ./configure --host x86_64-mingw32
    make LDFLAGS="-no-undefined -Liconv"
    strip src/.lib/libpx-0.dll

Copy ``src/.lib/libpx-0.dll`` to the pypxlib module's ``pxlib_ctypes`` 
directory and rename to ``pxlib_x64.dll``.

Cross-Compiled 32-bit Windows Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    sudo apt-get update
    sudo apt-get install gcc-mingw-w64 intltool make
    wget 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.8/pxlib-0.6.8.tar.gz?ts='`date +%s`'&use_mirror=freefr' -O pxlib-0.6.8.tar.gz
    tar -zxvf pxlib-0.6.8.tar.gz
    cd pxlib-0.6.8/
    ./configure --host i686-mingw32 "CFLAGS=-m32" "LDFLAGS=-m32"
    make
    strip src/.lib/libpx-0.dll

Copy ``src/.lib/libpx-0.dll`` to the pypxlib module's ``pxlib_ctypes`` 
directory and rename to ``pxlib.dll``.



OS X 10.10.5
------------

.. code:: bash

    sudo brew install intltool
    sudo brew link xy
    sudo brew install gettext
    curl -L 'http://downloads.sourceforge.net/project/pxlib/pxlib/0.6.8/pxlib-0.6.8.tar.gz?ts='`date +%s`'&use_mirror=freefr' -o pxlib-0.6.8.tar.gz
    tar -zxvf pxlib-0.6.8.tar.gz
    cd pxlib-0.6.8/
    echo './configure --prefix=`pwd`/out' | brew sh
    sed -i '' 's/#define HAVE_LOCALE_H 1//' config.h
    sed -i '' "/^CFLAGS =/ s/$/ -mmacosx-version-min=10.5/" Makefile
    make
    make install-strip

Copy the d to the the pypxlib module's ``pxlib_ctypes`` 
directory and rename to ``libpx.so``.

Windows 7
---------

1. Download & install the `Microsoft Visual C++ Compiler for Python 2.7`_.
2. Download and install CMake.
3. Download the pxlib 0.6.5 sources from
   http://sourceforge.net/projects/pxlib/files/latest/download?source=files .
4. Extract the pxlib sources to *two* directories for 32 and 64 bit,
   respectively. Eg. ``C:\pxlib-0.6.5-x86`` and ``C:\pxlib-0.6.5-x64``.
5. Start the *Visual C++ 2008 32-bit Command Prompt*, cd to
   ``C:\pxlib-0.6.5-x86`` and execute the following commands:
.. code:: bash

    cmake -D CMAKE_CXX_FLAGS_RELEASE=/MT -DCMAKE_BUILD_TYPE=Release -D PX_HAVE_ICONV=0 -D PX_HAVE_RECODE=0 .
    nmake

6. Repeat step 5. with the *64*-bit Command Prompt and ``C:\pxlib-0.6.5-x64``.
7. That's it. You now have the 32 bit dll in ``C:\pxlib-0.6.5-x86\pxlib.dll``
   and the 64 bit dll in ``C:\pxlib-0.6.5-x64\pxlib.dll``.

.. _`Microsoft Visual C++ Compiler for Python 2.7`: http://www.microsoft.com/en-us/download/details.aspx?id=44266

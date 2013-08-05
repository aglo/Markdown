# Markdown Online Compiler

***

An Online Compiler for Markdown files

## functions

* Online Compiler for Markdown files writing and previewing.
* Uploading Markdown files for previewing and modifying.
* Convenient Tools helping for writing Markdown files.
* Downloading Markdown files finished on Online Compiler.

## Installation

1. Install virtualenv: `$ sudo easy_install virtualenv`
   or even better:`$ sudo pip install virtualenv`

   If you use Ubuntu, also try: `$ sudo apt-get install python-virtualenv`
2. Create your own environment.

   ```
   $ cd Markdown(or the name of which dir you put the source code in)
   $ virtualenv venv
   ```
3. Get into the virtualenv from the root of the code and run in development mode:

   ```
   $ . venv/bin/activate
   $ (venv) python setup.py develop
   ```

   **Confirming you are online**

## Run

* run the localhost for Markdown Online Compiler
  ```
   $ python Markdown/manage.py
  ```
* Use it with browser on `localhost:5000/markdown`

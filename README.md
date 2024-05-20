# Python Packaging Example

## Key Concepts

* Virtual Env - Use Virtual Env, so that this project uses its own python (init.sh)
* Activation - Virtual Env needs activating when used in command line, run a command to activate it (start.sh)
* Python Path - `sys.path` makes `.py` files visible to this project. It's changed after venv activation
* IDE Interpreter - set to the virtual env of this project, which adds project root to `sys.path`
* `__init__.py` - marks a folder as a package

## Summary
This project shows how to set up the package structure of a python project. It can be used as a python project template. The goal includes:
* to be able to run a single test file from where the test file is
* to be able to run all the tests in a project

## Virtual Env

### Use Virtual Env - Summary of scripts

* run `init.sh` - so that it creates a python environment for this project
* run `start.ps1` or `start.sh` - so that it activates the environment and install dependencies
* run `python ./check-syspath.py` - shows `sys.path`
* run `run_unit_tests.ps1` or `run_unit_tests.sh` - run all unit tests

### Activating a Virtual Env

* When you activate a virtual environment
  - `.\my-env\Scripts\activate.ps1`
  - the activation script modifies the `PATH` environment variable to include the virtual environment’s bin or Scripts
    directory at the beginning of the path
  - This ensures that the Python interpreter and `pip` from the virtual environment are used
  - `Lib/site-packages` is added to `sys.path`

### Deleting a Virtual Env
* simply just deactivate the env, and then delete the env folder
  - `.\my-env\Scripts\deactivate.bat`

### Setting environment variables for a virtual env
* when running python in different terminals, these terminals can activate different virtual envs without interfeering with each other
* so environment variables can just be supplied to a script used activates the environment
* before deactivating, unsetting these variables is optional if the terminal is dedicatedly used for a project

## Python Path

### How Python Path Works

* `sys.path` is a list of strings that specifies the search path for modules
  - When you import a module, Python searches through these directories
  - When activating a virtual env, it modifies the `sys.path` to prioritize the environment's site-packages directory
  - Lib/site-packages directory - a location where third-party Python packages and modules are installed
* if a folder is added to `sys.path`, this folder can be the root folder of a project
  - all folders inside, if `__init__.py` is present, can be an importable module
* if a folder is a sibling of the file to run, then it can be imported even if nothing is added to `sys.path`

### `__init__.py`

* package - The `__init__.py` file marks a directory as a Python package
  - This allows you to import modules from that directory as if it were a package
  - If a directory `directly` within `sys.path` contains an `__init__.py` file, Python recognizes it as a package
* init code - The `__init__.py` file can execute initialization code for the package
  - This code `runs` when `the package` or `a module` within the package is `imported`
* terminologies
  - `module` - a module is a single Python `file`
  - `package` - a package is a `directory` that has a `__init__.py` file
* virtual env
  - make sure IDE Python Interpreter is set to the virtual env of this project, which adds project root to `sys.path`
  - without venv, python by default doesn't know the root directory of the current project
  - so even if `__init__.py` is put in each subfolder, modules within cannot be found
  - e.g. it doesn't know your source root dir is `./src`
  - e.g. it doesn't know your test root dir is `./tests`

### IDE lint
* to allow multiple statements in one line, need to disable flake8 E701,E702

----

# Useful Resource
## Importing
* from folder1 import file1 - in this case, running func1 needs file1.func1()
* from folder1.file1 import func1 - in this case, running func1 needs func1()
* https://docs.python.org/3/tutorial/modules.html#packages


```
from . import current_directory_file
from .. import up_1_level_directory_file
from ..up_1_level_directory_folder import file_inside_up_1_level_directory_folder
```

## Keywords
### Variables

* `__name__`
  * when a module is imported, 
    * this variable is set to the name of the module
    * usually this is the name of the file without .py
  * when a module itself is run directly
    * the value of __name__ is '__main__'
* `'__main__'` -
  * `__main__` - there is no such a variable called `__main__`
  * `'__main__'` - to be used to check if a file is run directly
* `__file__` - the name of the current file, including the full absolute path

### Files

* `__main__.py`
* `__init__.py` - mark a directory to be a package
  * executed when this package is IMPORTED
  * so variables defined in this file are available to all the modules in the package
  * won't execute when a file in this package is run

## Code Execution

### Differentiating if a file is directly run

Differentiates if a file is directly run/executed

```python
if __name__ == '__main__':
    print "Run Directly"
else:
    print "Run by Import"
```

Typically used in a unit test file e.g. The below resolves adds root_path to sys.path only if this test file is run directly

```python test_value_util.py
import os, sys
if __name__ == '__main__':
    root_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)))
    sys.path.append(root_path)
```

## Path
### Paths that Python knows
* when running a python script
  * e.g. python c:/code/test_value_util.py, python knows the "code" directory
  * python also knows modules inside, so if there is a "sub" dir here, "import sub" works
  * in this case, "sub" doesn't even need a `__init__.py` file
* python also knows paths available in sys.path

### Paths that Python doesn't knows
python doesn't know where the root directory is
* so "from src.base_util import value_util" doesn't work, because src is not recognised
* to make sure python knows "src", we need to make sure parent folder of "src" is in path

### Sys Path
sys.path 
* is a list 
* contains all the directories that Python will look in when you try to import a module

```python
import sys
sys.path
```

### Current Directory

```python
import os
os.getcwd()
```

If `test_value_util` contains `os.getcwd()`
* `os.getcwd()` is `c:\code` when running the below
  * C:\code>python c:/code/util/test_value_util.py
* `os.getcwd()` is `c:\code\util` when running the below
  * C:\code\util>python c:/code/util/test_value_util.py

### Absolute Path of Parent Directory

```python
import os
os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
```

## Testing
* https://docs.python.org/3/library/unittest.html

## Tutorial - Syntax
* https://www.w3schools.com/python/python_conditions.asp

## Code Formatting
* https://realpython.com/python-pep8/

### Ref
* python project structure 1: https://realpython.com/python-application-layouts/
* python project structure 2: https://docs.python-guide.org/writing/structure/#structure-of-code-is-key
* python project structure 3: https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
* python project structure 4: https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
* aws serverless project example 1: https://dev.to/fwojciec/how-to-structure-a-python-aws-serverless-project-4ace
* aws serverless project example 2: https://informediq.com/python-src-layout-for-aws-lambdas/
* aws lambda good practice: https://dev.to/aws-builders/aws-lambda-best-practices-4chn

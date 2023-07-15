# Python Packaging Example

## Summary
This project shows how to set up the package structure of a python project. It can be used as a python project template. The goal includes:
* to be able to run a single test file from where the test file is
* to be able to run all the tests in a project

### Challenges
* python by default doesn't know the root directory of the current project
* so even if __init__ is put in each folder/module, the module cannot be found

### How Python Works
* if a folder is added to sys.path, this folder can be the root folder of a project
  * all folders inside, if __init__.py is present, can be a importable module
* if a folder is a sibling of the file to run, then it can be imported even if nothing is added to sys.path

### Proposal
Since a test is in an arbitrary folder, to run one test file directly, we need to make sure the root folder is added to `sys.path`. The following shows how to do so:

#### tests/base_util/__init__.py
Put `resolve_root` into `__init__.py`, which finds the `root_path` and add it to `sys.path`

```python
import os
import sys

def resolve_root():
    root_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)))
    sys.path.append(root_path)
```

#### tests/base_util/test_value_util.py
Before importing `src`, we `import __init__` and `resolve_root()` if this test file is run directly
* `if __name__ == '__main__'` - true if running this file directly

```python
import __init__
if __name__ == '__main__': __init__.resolve_root()
import unittest
from src.base_util import value_util

class Test_value_util(unittest.TestCase):

    def test_is_string(self):
        self.assertEqual(value_util.is_string("hello"), True)
```

#### src/base_util/value_util.py
The source file, which is in the `src/base_util` package. The test file can't find this file if it doesn't `resolve_root()`

```python
def is_string(v):
    return isinstance(v, str)
```

----

### Proposal2
If we don't want `src` and `tests` to be packages (because `from src.base_util import value_util` looks strange), then we need to
* add `src` to sys.path, and add `tests` to sys.path

An alternative is still using Proposal1, but changing `src` to the name of the project e.g.
* root_folder/util/base_util - contains utils
* root_folder/my_project - contains project logic
* root_folder/tests/util/base_util - `from util.base_util import value_util`
* root_folder/tests/my_project - `from my_project import project_logic`

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
* __name__ 
  * when a module is imported, 
    * this variable is set to the name of the module
    * usually this is the name of the file without .py
  * when a module itself is run directly
    * the value of __name__ is '__main__'
* '__main__' - 
  * __main__ - there is no such a variable called __main__
  * '__main__' - to be used to check if a file is run directly
* __file__ - the name of the current file, including the full absolute path

### Files
* __main__.py
* __init__.py - mark a directory to be a package
  * executed when this package is IMPORTED
  * so variables defined in this file are available to all the modules in the package
  * won't execute when a file in this package is run

## Code Execution
### Differenciating if a file is directly run
Differenciates if a file is run directly

```python
if __name__ == '__main__':
    print "Run Directly"
else:
    print "Run by Import"
```

Typically used in a unit test file e.g. The below resolves adds root_path to sys.path only if this test file is run directly

```python test_value_util.py
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
  * in this case, "sub" doesn't even need a __init__.py file
* python also knows paths available in sys.path

### Paths that Python doesn't knows
python doesn't know where the root directory is
* so "from src.base_util import value_util" doesn't work, because src is not recognised
* to make sure python knows "src", we need to make sure parent folder of "src" is in path

### Sys Path
sys.path 
* is a list 
* contains all the directories that Python will look in when you try to import a module

```
import sys
sys.path
```

### Current Directory

```
import os
os.getcwd()
```

If `test_value_util` contains `os.getcwd()`
* `os.getcwd()` is `c:\code` when running the below
  * C:\code>python c:/code/util/test_value_util.py
* `os.getcwd()` is `c:\code\util` when running the below
  * C:\code\util>python c:/code/util/test_value_util.py

### Absolute Path of Parent Directory

```
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

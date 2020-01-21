# Import Logger

Emit logs when imports take to much time

```python
import import_logger

# Log all imports taking more than a second
import_logger.register(threshold=1)
```

### Installation

```
pip install import_logger
```

### Example

For the code:
`debug.py`
```python
import logging
import import_logger

logging.basicConfig(level=logging.DEBUG)
import_logger.register(0)

import pathlib
```
Output would be:
```
DEBUG:import_logger:_io (0.0s)
└╴demo.py

DEBUG:import_logger:os (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/fnmatch.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:posixpath (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/fnmatch.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:re (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/fnmatch.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:functools (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/fnmatch.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:fnmatch (0.013s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:io (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:sys (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/ntpath.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:stat (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/ntpath.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:genericpath (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/ntpath.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:ntpath (0.01s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:_collections_abc (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:errno (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:operator (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:collections (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/urllib/parse.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:warnings (0.0s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/urllib/parse.py
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:urllib.parse (0.009s)
├╴/Users/iddan/.pyenv/versions/3.8.0/lib/python3.8/pathlib.py
└╴demo.py

DEBUG:import_logger:pathlib (0.055s)
└╴demo.py
```

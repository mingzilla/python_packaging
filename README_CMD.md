## Virtual Environment

### Create a virtual env

```shell
python -m venv python-packaging-env
```

### activate virtual env

```shell
.\my-env\Scripts\activate
```

It would then look like this `(my-env) $`

### deactivate virtual env

```shell
.\my-env\Scripts\deactivate
```

### Install a Package

* this package will only be installed to the activated environment

```shell
pip install xxx
```

### Delete a virtual envs

* after deactivating, simply just delete the venv directory

----

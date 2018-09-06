# polyglot

## What is This?

A skeleton python service to wrap calls made to Google Translate.


## pipenv

This project uses [pipenv](https://pipenv.readthedocs.io/en/latest/)

Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile
as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce
deterministic builds.

To install pipenv:
``` 
pip install pipenv
```

To install the dependencies mentioned in Pipfile.lock:
```
pipenv install
```

To generate Pipfile.lock and installs all packages in it:
```
pipenv update

```

To sync the dev requirements
```
pipenv sync --dev
```

To install a 3rd party package
```
pipenv install <name-of-package e.g flask==0.12.1> 
```

To install a package that is only needed for development but not in production.

Providing the --dev argument will put the dependency in a special `[dev-packages]` location in the Pipfile.

```
pipenv install <package-name> --dev
```

To enter the a shell with the pipenv:
```
pipenv shell
export PYTHONPATH="<root directory of this project>" # so it can find the library module
```
## Development

:construction: Under Construction

## Exploration 

[Goolge APIs explorer](https://developers.google.com/apis-explorer/#p/)

## Testing

The [pytest](https://docs.pytest.org/en/latest/) framework is being used for testing

```
pipenv install pytest --dev
```

The tests are organized into the `unit` and `integration` directories within the `test` directory.

To run all tests use
```
pipenv run pytest
``` 

[Selecting tests to run](https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests)

[Stopping after the first ( or N) failures](https://docs.pytest.org/en/latest/usage.html#stopping-after-the-first-or-n-failures)

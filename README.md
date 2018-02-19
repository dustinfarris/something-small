# something-small

An example of a package ready to upload.

## Quick Start

### Installation

```
pip install something-small
```

### Usage

```py
>>> from something_small import something
>>> something.small()
Something small
```

## Development

### Environment

Install prerequisites in a Python virtual env (not required for delivery).

```
make develop
```

### Delivery

Upload to a local repository:

```
python setup.py sdist upload -r local
```

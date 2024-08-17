# greg - a resume enhancement tool written in python

## Name

The original idea was to name the tool G.R.E.G. (Government Resume Enhancement Generator), using a classmate's name as a humorous acronym.

## Unit Tests
* `python -m unittest discover -s test`
* TODO: check whether I also need `set PYTHONPATH=%cd%`

## Code Coverage
* `python -m coverage run -m unittest`
* `python -m coverage report` or `python -m coverage html`

## Gotchas

* `python -m pip install fitz` will fail.
* Instead try `python -m pip install --upgrade pymupdf`

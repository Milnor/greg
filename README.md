# greg - a resume enhancement tool written in python

## Name

The original idea was to name the tool G.R.E.G. (Government Resume Enhancement Generator), using a classmate's name as a humorous acronym.

The primary function is to allow the user to hide keywords in an existing resume so they are invisible to a human, but will
get picked up by software scanning the PDF.

Example usage:

```bat
python greg.py MyResume.pdf JobDescription.txt MyBetterResume.pdf
```

The example above will insert the text of `JobDescription.txt` into `MyResume.pdf` as invisible (i.e. white on white)
text and save the result as `MyBetterResume.pdf`. Currently, it works, but contains a huge bug in that the "invisible"
text leaves ugly artifacts... the resulting PDF looks like it was sent via fax. 

## Linting

* `ruff check`
* `ruff format` - can often fix E501 line-too-long automagically

## Unit Tests

* `python -m unittest discover -s test`
* TODO: check whether I also need `set PYTHONPATH=%cd%`

## Code Coverage

* `python -m coverage run -m unittest`
* `python -m coverage report` or `python -m coverage html`

## Gotchas

* `python -m pip install fitz` will fail.
* Instead try `python -m pip install --upgrade pymupdf`

# Open Data Day Publicbodies.org Nepal

We've gathered on Saturday, 5th March 2022 in order to try and automate
the collection of data about Nepalese public organizations.

## Participants

* @augusto-herrmann
* @nikeshbalami
* (please add the names of the other paticipants here if you want)

## Data source

The data source used was the government directory at:

[mofaga.gov.np](https://mofaga.gov.np/local-contact)

It was not in machine readable format, so we had to use web scaping for
that.

## Code

The code is in [nepal-public-bodies.py](nepal-public-bodies.py). It is
a Jupyter Notebook in percent script format (requires Jupytext to open).
I used percent script because the notebook is stored in a Python file
format that plays nice with git version control, if and when we need to
evolve it

## Next steps

Some things we still need to do:

* transform the notebook into a simple scraping script
* map the fields of the [resulting csv](data) to the format used by
  publicbodies.org
* create a Github Actions job to automate collection by publicbodies.org

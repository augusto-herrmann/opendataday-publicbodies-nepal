# Open Data Day Publicbodies.org Nepal

We've gathered on Saturday, 5th March 2022 with
[Open Knowledge Nepal](https://oknp.org/) in order to try and automate
the collection of data about Nepalese public organizations.

## Participants

* @[augusto-herrmann](https://github.com/augusto-herrmann)
* @[nikeshbalami](https://github.com/nikeshbalami)
* (please add the names of the other paticipants here if you want)

## Data source

The data source used was the government directory at:

[mofaga.gov.np](https://mofaga.gov.np/local-contact)

It was not in machine readable format, so we had to use web scaping for
that.

## Code

The code is in [nepal-public-bodies.ipynb](nepal-public-bodies.ipynb). in
Jupyter Notebook format.

## Next steps

Some things we still need to do:

* transform the notebook into a simple scraping script
* map the fields of the [resulting csv](data) to the format used by
  publicbodies.org
* create a Github Actions job to automate collection by publicbodies.org

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Scraping public bodies info for Nepal

# %%
import pandas as pd

# %%
import requests

# %%
from bs4 import BeautifulSoup

# %%
url = 'https://mofaga.gov.np/local-contact'

# %%
response = requests.get(url)

# %%
soup = BeautifulSoup(response.content)

# %%
table = soup.find('table')

# %%
columns = [tag.text for tag in table.find_all('th')]
columns

# %%
rows = table.find('tbody').find_all('tr')

# %% [markdown]
# ## Exploring the first row

# %%
first_row = rows[0]
first_row

# %%
[cell.text for cell in first_row.find_all('td')]

# %%
len(columns)

# %% [markdown]
# ## Building the data frame

# %%
df = pd.DataFrame(columns=columns)

# %%
df

# %%
for row in rows:
    cells = [cell.text for cell in row.find_all('td')]
    entry = dict(zip(columns, cells))
    entry['वेवसाईट'] = row.find('a').attrs['href']
    df.loc[len(df.index)] = entry.values()

# %%
df


# %% [markdown]
# ### Scraping function

# %%
def scrape_table(url: str) -> pd.DataFrame:
    """Scrapes a table from html in the government directory at https://mofaga.gov.np/local-contact
    and returns a data frame.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    table = soup.find('table')
    columns = [tag.text for tag in table.find_all('th')]
    rows = table.find('tbody').find_all('tr')
    df = pd.DataFrame(columns=columns)
    for row in rows:
        cells = [cell.text for cell in row.find_all('td')]
        entry = dict(zip(columns, cells))
        entry['वेवसाईट'] = row.find('a').attrs['href']
        df.loc[len(df.index)] = entry.values()
    return df


# %% [markdown]
# ### Data extraction

# %% [markdown]
# Scrape the district government organizations.

# %%
df = scrape_table('https://mofaga.gov.np/local-contact/dcc-prov-1?_token=29tedmjpqp7lgXXFG7hP0rliFO5kijkX36jLRsFF&province_id=0&dist_id=&visible=500')
df

# %%
df.to_csv('data/nepal-district-govorgs.csv', index=False)

# %% [markdown]
# Scrape the local government organizations url.

# %%
df = scrape_table('https://mofaga.gov.np/local-contact?_token=29tedmjpqp7lgXXFG7hP0rliFO5kijkX36jLRsFF&province_id=&dist_id=&local_tpe=&visible=10000&q=')
df

# %%
df.to_csv('data/nepal-local-govorgs.csv', index=False)

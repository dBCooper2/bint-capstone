# Importing Data into Notebooks

All data for this project is located in a google drive folder (contact @dBCooper2 to gain access), and can be read using pandas, *without having to download the data*.

## Steps

1. Navigate to the Google Drive URL
2. Copy the link to the file you wish to use
3. The URL will have the format:

```html
https://drive.google.com/file/d/{`file_id`}/view?usp=drive_link
```

4. Create the following code block, and paste the file_id string in from the sharing URL

```python
file_id = 'Some String'
url = f'https://drive.google.com/uc?id={file_id}'

df = pd.read_csv(url, encoding='utf-8')
```

This should allow you to create a shareable notebook so we don't need to change the file path of our data each time the notebook is opened on a new computer.

## Cells to Import Data

Here are some code snippets to paste into notebooks to read in CSV data.

- Shot Data, 2004-2024

```python
file_id = '1OjPW-F_Km8G6MqJL65g-jX5YK2OQLCx0'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url, encoding='utf-8')
```

- Game-Level Data, 2004-2024 :: WE ARE USING THIS ONE

```python
file_id = '1U2UaHWRSkUXfJBn4kBHPYttd3dvw_CZF'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url, encoding='utf-8')
```

- Player Data by Season, 2004-2024

```python
file_id = '1zcPiiPv_NRu7UoWrjsUlZBkQZ-wIPlr6'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url, encoding='utf-8')
```

- Team Data by Season, 2004-2024

```python
file_id = '1kTpr2kThMD6_BVMAwoiv90bmg7S-A2p-'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url, encoding='utf-8')
```

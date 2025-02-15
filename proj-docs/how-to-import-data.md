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

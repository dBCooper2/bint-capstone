# Business Intelligence and Data Analytics Capstone - DS 4510

## Structure

- `projects/` contains all notebooks for the project.
- `proj-docs/` contains any documentation, like data dictionaries, todo-lists, pretty much anything that is not code.
- `notebooks/` contains class notes (will remove if needed)

**Please make sure to edit the gitignore to contain your data files if they are saved in the repo on your local machine! Not doing this can break your ability to push changes due to the size of the data files, and we do not have LFS (Large File Sharing) set up!**

## Using this repository

To pull this repository down and start working with it, first clone the git repo with:

```bash
git clone https://github.com/dBCooper2/bint-capstone
```

This project is using **Python 3.11**. Create a virtual environment using:

```bash
cd bint-capstone/
python3.11 -m venv .venv
```

and activate it with:

```bash
source .venv/bin/activate
```

Lastly, install the required packages for the Jupyter Notebooks:

```bash
pip install -r projects/requirements.txt
```

Now you should have a working project directory. If you need to install more packages or select a python kernel in VSCode, just make sure it is installing/selecting the `.venv` directory you created.

You can also deactivate the virtual environment at any time by running the command:

```bash
deactivate
```

###### For Windows Instructions or to learn more about Virtual Environments, click [here](<https://docs.python.org/3/library/venv.html>).

More docs coming soon...

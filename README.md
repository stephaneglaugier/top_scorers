# Top Scorers

This Python application reads a CSV file listing people and the scores they achieved in a test. It then outputs the top scorers along with their highest marks. If there are two or more top scorers, the application will output all of them in alphabetical order. The application avoids using standard CSV-parsing libraries, implementing the CSV parsing from string data instead.

## Table of Contents
- [Setup](/#setup)
- [Usage](/#usage)
- [Running Tests](/#Running-Tests)

## Setup

### Use a virtual environment (optional but recommended):

```shell
python -m venv .venv
```

###  Activate the virtual environment:

#### For Windows:

```shell
.venv\Scripts\activate
```

#### For macOS and Linux:

```shell
source .venv/bin/activate
```

### Install using pip
```bash
pip install -e .
```

### Install using setup.py
```bash
python setup.py install
```


## Usage
1. Open your terminal and navigate to the project directory.
2. Run the script by passing the path to the CSV file as an argument.
```bash
python run.py path/to/file
```

3. The output will be displayed on the STDOUT, showing the top scorers and their score.
```
George Of The Jungle
Sipho Lolo
Score: 78
```

### Changing Separator with --sep
You can specify a different separator for parsing the CSV file by using the optional `--sep` parameter. The default separator is a comma `','`.

To use a semicolon `';'`:

```bash
python run.py path/to/file --sep=';'
```

This flexibility allows you to work with a variety of CSV file formats.

## Running Tests
To ensure that the application is working as expected, run the test suite.

1. Open your terminal and navigate to the project directory.
2. Run the tests.
```bash
python -m unittest
```

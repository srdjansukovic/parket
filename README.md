# Parket: A Simple Parquet Viewer CLI Tool

Parket is a command-line interface (CLI) tool designed to make working with Parquet files quick and easy. It includes a set of commands commonly used in everyday data analysis workflows.

## Features

- **schema**: Display the schema of the file.
- **head N**: Display the first N rows of the file.
- **columns**: Display the columns of the file.
- **select col1,col2,col3 N**: Display the first N rows for specified columns (col1, col2, col3).
- **jsonl N**: Display the first N rows of the file as JSON lines.
- **exit**: Exit the program.

## Usage

You can use Parket in two ways:

### 1. Using the Binary File (Recommended)

Clone the Parket repository and create a Python virtual environment (tested with Python 3.11.4). Follow these steps:

1. **Clone the Repository**
    ```bash
    git clone git@github.com:srdjansukovic/parket.git
    cd parket
    ```

2. **Set Up the Virtual Environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create the Executable**
    ```bash
    pyinstaller --onedir --name parket --distpath ./dist main.py
    ```
    This command will create an executable file in the `dist` folder at `path/to/parket/dist/parket/`.

5. **Add to PATH**
    Add the `dist` directory to your `$PATH` for easier access:
    ```bash
    export PATH=$PATH:/path/to/parket/dist/parket
    ```

6. **Run the Parket Tool**
    You can now use the Parket tool from anywhere on your machine:
    ```bash
    parket <file_path> <n_rows (optional)>
    ```
    *Note: The first run may take a few seconds longer.*

### 2. Using as a Python Script

Clone the Parket repository and set up a Python virtual environment. Follow these steps:

1. **Clone the Repository**
    ```bash
    git clone git@github.com:srdjansukovic/parket.git
    cd parket
    ```

2. **Set Up the Virtual Environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install polars
    ```

4. **Run the Script**
    Execute the `main.py` script with the file path and an optional number of rows:
    ```bash
    python main.py <file_path> <n_rows (optional)>
    ```


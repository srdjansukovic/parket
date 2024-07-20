import sys
import logging
import polars as pl
from pprint import pprint


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(message)s')


def main():
    setup_logging()

    if len(sys.argv) != 2 and len(sys.argv) != 3:
        logging.error("Usage: parket <file_path> <n_rows (optional)>")
        sys.exit(1)

    file_path = sys.argv[1]
    n_rows = int(sys.argv[2]) if len(sys.argv) == 3 else None

    df = read_parquet(file_path, n_rows)

    print_manual()

    with pl.Config(fmt_str_lengths=1000):
        while True:
            command = input("Enter a command: ").strip()

            if command == "schema":
                handle_schema(df)
            elif command.startswith("head"):
                handle_head(command, df)
            elif command == "columns":
                handle_columns(df)
            elif command.startswith("select"):
                handle_select(command, df)
            elif command.startswith("jsonl"):
                handle_jsonl(command, df)
            elif command == "exit":
                logging.info("Exiting the program.")
                break
            else:
                logging.warning("Unknown command. Please try again.")

            print_manual()


def print_manual():
    manual = """
    Available commands:
        schema - Display the schema of the file
        head N - Display the first N rows of the file
        columns - Display columns of the file
        select col1,col2,col3 N - Display the first N rows for col1, col2 and col3
        jsonl N - Display the first N rows of the file as json lines
        exit - Exit the program
    """
    logging.info(manual)


def read_parquet(file_path, n_rows):
    try:
        df = pl.read_parquet(source=file_path, n_rows=n_rows)
        logging.info("\nParquet file successfully loaded.")
    except Exception:
        logging.exception(f"An error occurred while reading the parquet file")
        sys.exit(1)
    return df


def handle_schema(df):
    pprint(df.schema)


def handle_head(command, df):
    try:
        n_rows = int(command.split(" ")[1])
        pprint(df.head(n=n_rows))
    except Exception:
        logging.exception("Error while reading first N rows of the parquet file")


def handle_columns(df):
    pprint(df.columns)


def handle_jsonl(command, df):
    try:
        n_rows = int(command.split(" ")[1])
        for row in df.head(n=n_rows).iter_rows(named=True):
            print(row)
    except Exception:
        logging.exception("Error while reading first N rows of the parquet file as a dictionary")


def handle_select(command, df):
    try:
        parts = command.split(" ")
        columns = parts[1]
        n_rows = int(parts[2])
        columns_arr = columns.split(",")
        selected_columns = df.select(columns_arr)
        pprint(selected_columns.head(n=n_rows))
    except Exception as e:
        logging.exception(f"An error occurred while selecting columns {e}")


if __name__ == "__main__":
    main()

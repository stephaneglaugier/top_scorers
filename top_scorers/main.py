import argparse
import os

from top_scorers.csv_parser import parse_csv
from top_scorers.data_input import read_plain_text
from top_scorers.data_processing import process_data
from top_scorers.output import construct_output_str


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the input file.")
    parser.add_argument("--sep", default=",",
                        help="Field separator (default is ',').")

    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        raise FileNotFoundError(f"File does not exist: {args.file_path}")
    csv_string = read_plain_text(args.file_path)
    parsed_data = parse_csv(csv_string, separator=args.sep)
    top_scorers, top_score = process_data(parsed_data)
    output_str = construct_output_str(top_scorers, top_score)
    print(output_str)


if __name__ == '__main__':
    main()

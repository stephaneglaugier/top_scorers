from top_scorers.data_processing import SCORE


def is_header(first_row: str, separator: str = ",") -> bool:
    try:
        if first_row.split(separator)[SCORE].lower() == "score":
            return True
    except:
        pass
    return False


def parse_csv(csv_string: str, separator=',') -> list[list[str | int]]:

    lines = csv_string.strip().split('\n')

    data = []

    start_idx = 1 if is_header(lines[0], separator) else 0
    for line in lines[start_idx:]:
        row = [x.strip() for x in line.split(separator)]
        if len(row) != 3 or not row[SCORE].isdigit():
            raise ValueError(f"invalid entry: '{line}'")
        row[SCORE] = int(row[SCORE])
        data.append(row)

    return data

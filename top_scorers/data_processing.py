FIRST_NAME = 0
LAST_NAME = 1
SCORE = 2


def calculate_top_score(data: list[list[str | int]]) -> int:

    top_score = -1
    for student in data:
        if student[SCORE] > top_score:
            top_score = student[SCORE]

    return top_score


def idxs_with_score(data: list[list[str | int]], score: int) -> list[str]:

    idxs = []
    for i, student in enumerate(data):
        if student[SCORE] == score:
            idxs.append(i)

    return idxs


def names_from_idxs(data: list[list[str | int]], idxs: list[int]) -> list[str]:

    names = [None] * len(idxs)
    for i, idx in enumerate(idxs):
        student = data[idx]
        names[i] = f"{student[FIRST_NAME]} {student[LAST_NAME]}"

    return sorted(names)


def process_data(data: list[list[str | int]]) -> tuple[list[str], int]:

    top_score = calculate_top_score(data)

    top_scorers = names_from_idxs(data, idxs_with_score(data, top_score))

    return top_scorers, top_score

def construct_output_str(names: list[str], top_score: int) -> str:

    output = ""
    for name in names:
        output += f"{name}\n"

    output += f"Score: {top_score}"

    return output

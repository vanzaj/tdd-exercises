def count_lines(source: str = "") -> int:
    lines = filter(lambda x: x.strip() != "", source.split("\n"))
    return len(list(lines))


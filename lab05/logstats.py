from collections import Counter


def parse_event(line: str) -> dict:
    stripped = line.strip()
    if not stripped:
        raise ValueError("Empty line")

    parts = stripped.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"Invalid log line format: {line}")

    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Unknown log level: {level}")

    return {"time": time_str, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return dict(counts)

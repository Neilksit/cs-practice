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


def top_errors(lines, n: int) -> list:
    error_messages = []
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                error_messages.append(event["message"])
        except ValueError:
            continue

    counts = Counter(error_messages)

    sorted_errors = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    return [[msg, count] for msg, count in sorted_errors[:n]]


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу\n"]

    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("\nЧастые ошибки:")
    if errors:
        for msg, count in errors:
            lines.append(f"- {msg} — {count}")
    else:
        pass

    return "\n".join(lines) + "\n"
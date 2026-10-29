import sys
from logstats import count_levels, format_report, top_errors


def main():
    filename = sys.stdin.readline().strip()
    if not filename:
        return

    with open(filename, encoding="utf-8") as f:
        counts = count_levels(f)

    with open(filename, encoding="utf-8") as f:
        errors = top_errors(f, 3)

    total_lines = sum(counts.values())
    error_lines = counts.get("ERROR", 0)
    broken_lines = counts.get("BROKEN", 0)

    print(total_lines)
    print(error_lines)
    print(broken_lines)

    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report_text)


if __name__ == "__main__":
    main()
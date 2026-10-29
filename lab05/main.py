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

    


if __name__ == "__main__":
    main()
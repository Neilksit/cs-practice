from collections import Counter
from pathlib import Path


def count_by_extension(paths: list[str]) -> dict[str, int]:
    exts = []
    for p in paths:
        filename = Path(p).name
        if "." in filename and not filename.startswith("."):
            ext = filename.rsplit(".", 1)[1].lower()
            if not ext:
                ext = ""
        elif filename.count(".") > 1:
            parts = filename.split(".")
            if filename.startswith(".") and len(parts) > 2:
                ext = parts[-1].lower()
            else:
                ext = ""
        else:
            ext = ""

        exts.append(ext)

    return dict(Counter(exts))


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    max_depth = -1
    best_path = ""
    for p in sorted(paths):
        depth = p.count("/")
        if depth > max_depth:
            max_depth = depth
            best_path = p
    return best_path


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    unit_idx = 0

    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024
        unit_idx += 1

    if unit_idx == 0:
        return f"{int(size)} Б"
    else:
        return f"{size:.1f} {units[unit_idx]}"
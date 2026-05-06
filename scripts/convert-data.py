import json
from argparse import ArgumentParser


def convert(pkgsupdate: list[dict]) -> list[list]:
    keys = ["name", "before", "after", "warnings"]
    return [[pkg[key] for key in keys] for pkg in pkgsupdate]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--input", default="pkgsupdate.json", help="Input file (pkgsupdate)"
    )
    parser.add_argument(
        "-o", "--output", default="anicca-data.json", help="Output file (anicca-data)"
    )
    args = parser.parse_args()

    with open(args.input) as f:
        pkgsupdate = json.load(f)

    converted = convert(pkgsupdate)
    with open(args.output, "w") as f:
        f.write(
            "[\n"
            + ",\n".join([json.dumps(row, separators=(",", ":")) for row in converted])
            + "\n]"
        )

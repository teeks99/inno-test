import os
import csv
import json


def make_csvs(result_dir = "results"):
    start_dir = os.getcwd()
    try:
        os.chdir(result_dir)
        all_entries = os.listdir(".")
        valid_files = []
        for entry in all_entries:
            if os.path.isfile(entry):
                start, ext = os.path.splitext(entry)
                if ext == ".json":
                    valid_files.append(entry)

        for f in valid_files:
            make_csv(f)
    finally:
        os.chdir(start_dir)


def make_csv(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    headers = ["payload"]
    for test in data["payloads"][0]["tests"]:
        headers.append(test["name"])

    times_lines = []
    sizes_lines = []
    for payload in data["payloads"]:
        times = [payload["name"]]
        sizes = [payload["name"]]
        for test in payload["tests"]:
            times.append(test["elapsed"])
            sizes.append(test["size"])
        times_lines.append(times)
        sizes_lines.append(sizes)

    base, ext = os.path.splitext(filename)
    timesname = base + "-times.csv"
    sizesname = base + "-sizes.csv"

    with open(timesname, 'w', newline='') as timesfile:
        timeswriter = csv.writer(timesfile)
        timeswriter.writerow(headers)
        for row in times_lines:
            timeswriter.writerow(row)

    with open(sizesname, 'w', newline='') as sizesfile:
        sizeswriter = csv.writer(sizesfile)
        sizeswriter.writerow(headers)
        for row in sizes_lines:
            sizeswriter.writerow(row)


if __name__ == "__main__":
    make_csvs()

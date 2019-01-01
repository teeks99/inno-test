import json
import datetime
import subprocess
import os
from string import Template

template = "setup_template.iss"
test_set = "test_set.json"
results_file = "results.json"
#inno_cmd = r"C:\Program Files(x86)\Inno Setup 5\Compil32.exe"
inno_cmd = r"InnoSetup5\Compil32.exe"

def save_results(resultsfile, data):
    with open(resultsfile, "w") as r:
        json.dump(data, r)

def run_tests(test_set, template, results_file):
    with open(test_set, "r") as f:
        tests = json.load(f)

    results = {"run": str(datetime.datetime.now), "payloads": []}

    for payload in tests["payloads"]:
        data = {"name": payload["name"], "dir": payload["dir"], "tests": []}
        results["payloads"].append(data)

        for test in tests["tests"]:
            name = test["name"]
            print("Running payload: {} test: {}".format(payload["name"], name))
            setup_file = name + "_setup.iss"
            output_file = "test_1.0-" + name + ".exe"

            vars = ";Variable tests from test_set.json\n"
            for var in test["vars"]:
                vars += var + "\n"

            with open(template, "r") as innotemplate:
                stemplate = Template(innotemplate.read())
                replace = {"Config": name, "SourceDir": payload["dir"], "SetupVariables":vars}
                with open(setup_file, "w") as setupf:
                    setupf.write(stemplate.safe_substitute(replace))

            start = datetime.datetime.now()
            cmd = '"' + inno_cmd + '" /cc ' + setup_file
            print(cmd)
            subprocess.call(cmd, shell=True)
            stop = datetime.datetime.now()
            elapsed = stop - start

            size = os.path.getsize(output_file)

            test_data = {"name": name, "elapsed": elapsed.total_seconds(), "size": size}
            data["tests"].append(test_data)
            save_results(results_file, results)

if __name__=="__main__":
    run_tests(test_set, template, results_file)

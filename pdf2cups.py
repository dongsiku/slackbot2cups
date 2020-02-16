import subprocess


def pdf2cups(filename):
    command = "lp {}".format(filename)
    output = subprocess.run(
        command.split(),
        encoding='utf-8',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(output)
    if output.stderr == "lp: Error - No default destination.\n":
        pass


if __name__ == "__main__":
    pdf2cups("requirements.txt")

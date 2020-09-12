GENERATE_ODT = False  # Set to true if you don't want to use gLabels

import os

if GENERATE_ODT:
    from jinja2 import Environment, FileSystemLoader
    import zipfile

import re


def get_code_list(filename="codes.txt"):
    # Create a list with the codes from the file
    # Note: This file should contain the codes somewhere between parentheses
    with open(filename, "r") as file:
        data = file.read()
    data_codes = re.findall(r"\([A-Z0-9]+\)", data)
    codes = [code[1:-1] for code in data_codes]  # remove parentheses
    return codes


# Groups codes per 3 with their corresponding number (one row in the sticker sheet)
def make_trios(codes):
    trios = list()  # Final list of all rows (with 3 number-code-pairs per row)

    # Make sure the codes is a multiple of 3
    if len(codes) % 3:
        for i in range(3 - (len(codes) % 3)):
            codes.append("")

    counter = 1
    trio = list()
    for code in codes:
        current = (counter, code)  # lidnr, code tuple
        trio.append(current)

        if counter % 3 == 0:
            trios.append(trio)
            trio = list()

        counter += 1

    return trios


# Zip the contents
def zipdir(path, ziph):
    # src: https://stackoverflow.com/questions/42055873/zip-only-contents-of-directory-exclude-parent-python
    # ziph is zipfile handle
    length = len(path)

    for root, dirs, files in os.walk(path):
        folder = root[length:]  # path without "parent"

        for file in files:
            ziph.write(os.path.join(root, file), os.path.join(folder, file))


def create_codes_csv(codes):
    output = "lidnr,code\n"
    lidnr = 1
    for code in codes:
        output += f"{lidnr},{code}\n"
        lidnr += 1
    with open("codes.csv", "w+") as f:
        f.write(output)


def create_odt_file(codes, filename="Stickers.odt", template="template - content.xml"):
    # Render the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template)
    trios = make_trios(codes)
    output_from_parsed_template = template.render(codes=trios)

    # Write out the result
    with open("odt/content.xml", "w+") as f:
        f.write(output_from_parsed_template)

    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    zipdir('odt/', zipf)
    zipf.close()


def main():
    codes = get_code_list()
    create_codes_csv(codes)
    if GENERATE_ODT:
        create_odt_file(codes)


if __name__ == '__main__':
    main()

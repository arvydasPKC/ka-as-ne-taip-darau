import os
from dict import folderiai

count_project_files = 0
count_other_files = 0
count_folders = 0

inputted_text = input("Text: ")
inputted_folder = int(input("Folder: "))
template = f'  <PinRangeConnector>{inputted_text}</PinRangeConnector>\n'

zaltis = folderiai[inputted_folder]

# cwd = os.getcwd()
# cwd = 'C:\\Users\\arvga\\OneDrive - PKC Group Oyj\\Stuff\\src\\Tado frame projektas\\testuotojai_replace_line\\attempt4'
# print(f"zaltis - {zaltis}")
# print(f"file directory - {files_in_directory}")
files_in_directory = os.listdir(zaltis)

for file in files_in_directory:
    if os.path.isfile(file):
        if file.endswith('.project'):
            # print("found project file, let's do the work")
            count_project_files += 1

            with open(file, 'r') as opened_file:
                fileContent = opened_file.readlines()

            # Find line, where modification should be done
            for lineIndex in range(len(fileContent)):

                if '<PinRangeConnector>' in fileContent[lineIndex]:
                    fileContent[lineIndex] = template

                    with open(file, 'w') as tableFile:
                        tableFile.writelines(fileContent)
                    break
        else:
            count_other_files += 1
    else:
        count_folders += 1

print("\n!!!!!BAIGTA!!!!!\n"
      "Summary yra toks:\n")

print(f"pasirinkta dir buvo {zaltis}\n")
print(f"{count_project_files} .project failuose <PinRangeConnector> reiksme pakeista i '{inputted_text}'")
print(f'{count_other_files} ne .project failai, nepaliesti')
print(f"{count_folders} folderiai nepaliesti")

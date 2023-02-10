import os

count_project_files = 0
count_other_files = 0
count_folders = 0

inputted_text = input("Text: ")
template = f'  <PinRangeConnector>{inputted_text}</PinRangeConnector>\n'

# cwd = os.getcwd()
lala = 'C:\\Users\\arvga\\OneDrive - PKC Group Oyj\\Stuff\\src\\Tado frame projektas\\testuotojai_replace_line\\attempt4\\test_data\\one'
print(lala)
file_directory = os.listdir(lala)
print(file_directory)

for file in file_directory:
    if os.path.isfile(file):
        if file.endswith('.project'):
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
print(f"pasirinkta dir buvo {lala}")
print(f"pasirinktos dir content buvo {file_directory}")
print(f"{count_project_files} .project failuose <PinRangeConnector> reiksme pakeista i '{inputted_text}'")
print(f'{count_other_files} ne .project failai, nepaliesti')
print(f"{count_folders} folderiai nepaliesti")


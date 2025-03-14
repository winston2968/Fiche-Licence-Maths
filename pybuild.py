# ================================================================================================
#                              Python Script for build 
# ================================================================================================

from genericpath import isdir, isfile
from pathlib import Path
import os 
import shutil 
import json 

subject_repo = "./subjects"
config_file = "build_config.json"
main_file = "main.tex"

new_chapter_string = """

\\clearpage
\\setcounter{chapter}{0}
\\setcounter{section}{0}
\\setcounter{subsection}{0}
"""



"""
    Get all .tex files from a subdir 
"""
def get_tex_files(dir):
    # List containing folder files
    file_list = []
    entry= Path(dir)
    # Queue for folders traitment 
    F = [entry]
    while F:
        current = F.pop(0)
        if current.is_file() == False:
            for file in current.iterdir():
                F.append(file)
        else:
            if current.suffix == ".tex":
                file_list.append(current)

    return file_list

"""
    Return project specifications in build_config.json 
"""
def get_project_spec(config_file=config_file):
    with open(config_file, mode="r", encoding="utf-8") as read_file:
        frie_data = json.load(read_file)
    
    # Get values in .json file 
    project_name = frie_data["project_name"]
    chapters_order = frie_data["chapters_order"]
    hearder_file = frie_data["header_file"]

    return project_name, chapters_order, hearder_file


"""
    Create dictionnary containing fiels names to input on main
"""
def get_dict_files(chapters_order):
    # Content folder
    subject = Path(subject_repo)
    # Files name dictionnary
    dict_chapters = {}

    # Loop on courses folders
    for file in subject.iterdir():
        n = chapters_order.index(file.stem)
        # Adding all .tex files to the dictionnary
        dict_chapters[n] = get_tex_files(file)

    return dict_chapters

"""
    Create main_build.tex to build the project and 
    move needed files to build/ for building the project with latex
"""

def get_title_from_list(l):
    for line in l:
        if "title" in line.stem:
            return line.stem


def moove_files(dict_files, header_file):

    # Copying main.tex file to build 
    main_content = ""
    with open("main.tex", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line != "\\end{document}":
                main_content += line

    # Adding input lines to main_build.tex
    for num in sorted(dict_files.keys()):
        chapter = dict_files[0]
        # Break pages to change chapter
        if num != 0:
            main_content += new_chapter_string
        # Getting title 
        result = get_title_from_list(dict_files[num])
        # Adding title 
        main_content += "\\input{" + result + ".tex}\n"
        # Adding tableofcontent
        main_content += ("\\tableofcontents\n")
        # Adding files to include
        for file in sorted(dict_files[num])[1:-1]:
            if "main" not in file.stem:
                main_content += "\\input{" + file.stem + ".tex}\n"
        
    # Writing main.tex in /build 
    main_content += "\n\\end{document}\n"
    with open("build/main_build.tex", "w") as file:
        file.write(main_content)

    # Moove files to build folder
    destination_folder = Path("build")
    for num in dict_files:
        for file in dict_files[num]:
            destination_file = destination_folder / file.name
            shutil.copy(file, destination_file)





name, chapters, header_file = get_project_spec()

dict = get_dict_files(chapters)
moove_files(dict, header_file)

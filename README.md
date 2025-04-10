# pdf_merger

## SHORT DESCRIPTION

This Windows application allows for merging multiple PDF files into a single PDF file. All source PDF files should be located in the same folder.

## PREPARATIONS: HOW TO PRODUCE MAIN.EXE ON WINDOWS

- Clone the repo
- Initiate virtual environment
    - If poetry is not installed on your machine, install it:
    <code>pip install poetry</code>
    - Go to project directory:
    <code>cd /path/to/pdf_merger</code>
    - create virtual environment and install dependencies:
    <code>poetry install</code>
    - activate virtual environment:
    <code>poetry shell</code>
- Generate exe file:
    <code>pyinstaller --onefile main.py</code>
    This will create one executable file in dist folder of your project.

## HOW TO CREATE A MERGED PDF FILE

In order to generate a merged PDF file you have to execute main.exe with a number of parameters from command line.
- first argument: the path to the directory containing input pdf files; output pdf file will be created here as well;
- middle arguments (1 to N): the names of the input pdf files
- last argument: the name of the output file

Example of running from PowerShell console:
& "D:\333\main.exe" "D:\444\" "input_file_01.pdf" "input_file_02.pdf" "input_file_03.pdf" "input_file_04.pdf" "merge_result.pdf"
# pdf_merger

Merging multiple PDF-files to a single PDF file:
- first argument: the path to the directory containing input pdf files; output pdf file will be created here as well;
- middle arguments (1 to N): the names of the input pdf files
- last argument: the name of the output file

Example of running PowerShell console:
& "D:\333\main.exe" "D:\444\" "input_file_01.pdf" "input_file_02.pdf" "input_file_03.pdf" "input_file_04.pdf" "merge_result.pdf"

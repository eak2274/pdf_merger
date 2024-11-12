from PyPDF2 import PdfMerger
import argparse


def merge_pdfs(input_directory, input_files, output_file):
    """
    Merges multiple PDF documents into a single PDF document.

    Input parameters:
    input_directory (str) - the path to the directory containing input pdf files;
                            output pdf file will be created here as well
    input_files (list) - the names of the input pdf files
    output_file (str) - the name of the output file
    """
    merger = PdfMerger()

    # Adding every input PDF file to a resulting file
    for pdf_path in input_files:
        merger.append(f"{input_directory}\\{pdf_path}")

    # Writing the merged file
    with open(f"{input_directory}\\{output_file}", 'wb') as out_file:


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Merging multiple PDF-files to a single PDF file:
    first argument: the path to the directory containing input pdf files; output pdf file will be created here as well;
    middle arguments: the names of the input pdf files
    last argument: the name of the output file
    """)

    parser.add_argument("elements", type=str, nargs="+",
                        help="A list of arguments: dir, input pdf files, output pdf file.")
    args = parser.parse_args()

    if len(args.elements) < 3:
        print("Wrong number of arguments given. Please enter all necessary arguments.")
        exit(1)

    input_pdf_directory, input_pdf_files, output_pdf_file = args.elements[0], args.elements[1:-1], args.elements[-1]
    merge_pdfs(input_directory=input_pdf_directory, input_files=input_pdf_files, output_file=output_pdf_file)

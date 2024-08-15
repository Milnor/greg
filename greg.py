import argparse
import pymupdf

def extract_text(filename):
    ''' Extract text from file, e.g. job description, and return a string of keywords and phrases '''
    return "type 100wpm, fluent in Esperanto, Nobel Prize in customer service"

def validated_arguments(resume, hidden, output, force, verbose):
    ''' Return valid arguments for main() or raise error '''

    if verbose:
        print(f"[!] validated_arguments(resume={resume}, hidden={hidden}, output={output}, force={force}, verbose={verbose})")

    # resume must be a valid path to a PDF
    # hidden must be a valid PDF file, TXT file, or string of text
    # output must be a valid pathname to a PDF or autogenerate one based on input file
    # error if output name already exists if not used with force


def main(original, insertion, output):
    ''' Insert hidden text into a PDF and save it under a new name '''

    # Workflow in this block adapted from ChatGPT response
    with pymupdf.open(original) as doc:
        page = doc[0] # Insert into first page by default
        page.insert_text((72, 72), insertion, fontsize=12, color=(1, 1, 1)) 
        doc.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='greg', description='Insert hidden text into a PDF')
    parser.add_argument('resume', type=str, help='Original resume as PDF')
    parser.add_argument('hidden', type=str, help='PDF file, TXT file, or quote delimited string containing text to insert')
    parser.add_argument('output', type=str, help='Name of output file, must be PDF', default='autogenerate')
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite output file if it already exists')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode for testing and debugging')
    args = parser.parse_args()
    original, hidden_text, output, verbose = validated_arguments(args.resume, args.hidden, args.output, args.force, args.verbose)
    main(original, hidden_text, output, verbose)

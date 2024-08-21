"""Stuff invisible keywords into a resume PDF."""

import argparse
import sys
from pathlib import Path

import pymupdf


def string_from_file(filename):
    """Return text contents of file as a string."""
    match Path(filename).suffix:
        case ".pdf":
            # TODO: parse this with pymypdf
            raise NotImplementedError(
                "PDF is correct type, but not implemented yet"
            )
        case ".txt":
            with open(filename, "r") as data:
                return data.read()
        case _:
            raise TypeError(
                f"Expected PDF or TXT, not {Path(filename).suffix}"
            )


def validated_arguments(resume, hidden, output, force, verbose):
    """Return valid arguments for main() or raise error."""
    if verbose:
        print(
            f"[!] validated_arguments(resume={resume}, hidden={hidden}, "
            "output={output}, force={force}, verbose={verbose})"
        )

    resume = Path(resume)
    hidden = Path(hidden)
    output = Path(output)

    # resume must be a valid path to a PDF
    if not Path.exists(resume):
        raise FileNotFoundError(f"{resume} does not exist")

    # hidden must be a valid PDF file, TXT file, or string of text
    if Path.exists(hidden):
        hidden = string_from_file(hidden)

    # error if output name already exists if not used with force
    if Path.exists(output) and not force:
        raise FileExistsError(
            f"{output} exists. Use -f or --force to overwrite"
        )

    # output must be a valid pathname to a PDF or autogenerate one
    # based on input filename
    if output == "autogenerate":
        for x in range(1, 10000):
            possible_path = f"{resume}_{x}.pdf"
            if not Path.exists(possible_path):
                output = possible_path
                break
    if output == "autogenerate":
        raise FileExistsError(
            f"Sorry. I couldn't devise an unused output path {resume}_X.pdf"
        )

    return resume, hidden, output, verbose


def main(args):
    """Insert hidden text into a PDF and save it under a new name."""
    parser = argparse.ArgumentParser(
        prog="greg", description="Insert hidden text into a PDF"
    )
    parser.add_argument("resume", type=str, help="Original resume as PDF")
    parser.add_argument(
        "hidden",
        type=str,
        help="PDF file, TXT file, or string containing text to insert",
    )
    parser.add_argument(
        "output",
        type=str,
        help="Name of output file, must be PDF",
        default="autogenerate",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite output file if it already exists",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose mode for testing and debugging",
    )
    args = parser.parse_args()
    original, hidden_text, output, verbose = validated_arguments(
        args.resume, args.hidden, args.output, args.force, args.verbose
    )

    # Workflow in this block adapted from ChatGPT response
    with pymupdf.open(original) as doc:
        page = doc[0]  # Insert into first page by default
        page.insert_text((72, 72), hidden_text, fontsize=12, color=(1, 1, 1))
        doc.save(output)


if __name__ == "__main__":
    main(sys.argv[1:])

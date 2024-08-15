import argparse
import pymupdf

def extract_text(filename):
    ''' Extract text from file, e.g. job description, and return a string of keywords and phrases '''
    return "type 100wpm, fluent in Esperanto, Nobel Prize in customer service"

def main(original, insertion, output):
    ''' Insert hidden text into a PDF and save it under a new name '''

    # Workflow in this block adapted from ChatGPT response
    with pymupdf.open(original) as doc:
        page = doc[0] # Insert into first page by default
        page.insert_text((72, 72), insertion, fontsize=12, color=(1, 1, 1)) 
        doc.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='greg')
    # TODO: actual argument parsing
    original = "resume.pdf"
    hidden_text = extract_text("job_description.txt")
    output = "modified.pdf"
    main(original, hidden_text, output)

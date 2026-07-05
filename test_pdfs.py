import pdfplumber
from pathlib import Path

# Test if the newly created PDFs are readable
sample_dir = Path('samples')
candidates = ['candidate_A.pdf', 'candidate_B.pdf', 'candidate_C.pdf']

for candidate_file in candidates:
    file_path = sample_dir / candidate_file
    print(f'\nTesting: {candidate_file}')
    try:
        with pdfplumber.open(file_path) as pdf:
            print(f'  Pages: {len(pdf.pages)}')
            total_text_length = 0
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ''
                total_text_length += len(text)
                if i == 0:
                    print(f'  First page text length: {len(text)}')
                    if text:
                        print(f'  First 200 chars: {text[:200]}')
            print(f'  Total text length: {total_text_length}')
    except Exception as e:
        print(f'  Error: {e}')

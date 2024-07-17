# Title: clean_queries.py
# Date: Summer 2024
# Author: Anika Kathuria (ak4748@columbia.edu)

import re
import sys

def clean_company_names(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    company_suffixes = re.compile(
        r'\b(LLC|Ltd|plc|Inc|Corp|Corporation|Co|Company|LLP|P.C.|P.L.C.|S.A.|S.A.S|S.L.|S.R.L|AG|GmbH|S.p.A|BV|NV|Oy|ApS|A/S|SA|SARL|PLC|LP)\b',
        re.IGNORECASE
    )
    parentheses_content = re.compile(r'\((.*?)\)')

    cleaned_lines = []
    all_paren_terms = []

    for line in lines:
        paren_terms = parentheses_content.findall(line)
        all_paren_terms.extend(paren_terms)
        
        content_no_parens = parentheses_content.sub('', line)
        cleaned_content = company_suffixes.sub('', content_no_parens)
        
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()
        cleaned_content = re.sub(r'\sOR\s', ' OR ', cleaned_content)
        
        cleaned_lines.append(cleaned_content)

    paren_terms_string = ' OR '.join(f'"{term.strip()}"' for term in all_paren_terms)

    with open(output_file, 'w') as file:
        file.write('\n'.join(cleaned_lines) + '\n')
        if paren_terms_string:
            file.write('\n' + paren_terms_string)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_queries.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        clean_company_names(input_file, output_file)


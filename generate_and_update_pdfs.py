# usr/bin/env python 
# 
# pip install docx2pdf
#

import os
from docx2pdf import convert

for (dir_path, dirnames, file_names) in os.walk('.'):
    for file_name in file_names:
        if file_name.endswith('.docx'): 
            if dir_path.endswith('/edit'):
                docx_path = os.sep.join([dir_path, file_name])
                pdf_path = os.sep.join([os.path.split(dir_path)[0], file_name.replace('docx', 'pdf')])
                convert(docx_path, pdf_path)
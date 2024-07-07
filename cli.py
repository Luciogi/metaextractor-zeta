import sys
from lib import *
import magic
import os
from fpdf import FPDF

OUTPUT_DIR = "results"

def print_help():
	help_text = f"""Zeta Metadata Extractor - Extract metadata from various files
Usage:
	python cli.py <file>
Note:
	Results will be available in ./{OUTPUT_DIR}
Options:
	-h, --help		Show this help message and exit
"""
	print(help_text)

def create_result_folder():
	if not os.path.exists(OUTPUT_DIR):
		os.makedirs(OUTPUT_DIR)

def write_pdf(file_name, metadata):
	base_name = os.path.basename(file_name)
	result_file = f"{OUTPUT_DIR}/{base_name}.pdf"
	counter = 1

	while os.path.exists(result_file):
		result_file = f"{OUTPUT_DIR}/{base_name}-{counter}.pdf"
		counter += 1

	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size=12)
	pdf.cell(200, 10, txt=f"Metadata for {base_name}", ln=True, align='C')
	pdf.ln(10)

	for k, v in metadata.items():
		if isinstance(v, dict):
			pdf.cell(200, 10, txt=f"{k}:", ln=True)
			pdf.ln(5)
			for sub_k, sub_v in v.items():
				if sub_v:
					pdf.cell(90, 10, txt=f"{sub_k}:", border=1)
					pdf.cell(100, 10, txt=f"{sub_v}", border=1, ln=True)
		else:
			if v:  # Only print if the value exists
				pdf.cell(90, 10, txt=f"{k}:", border=1)
				pdf.cell(100, 10, txt=f"{v}", border=1, ln=True)

	pdf.output(result_file)

def main():
	if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
		print_help()
		return

	file = sys.argv[1]
	file_type = magic.from_file(file, mime=True)
	print("File Type:",file_type)
	metadata = extract_metadata_file(file)

	print_data(metadata)

	# Append meta-metadata
	metadata = add_meta_metadata(metadata, file)

	create_result_folder()
	write_pdf(file, metadata)

if __name__ == "__main__":
	main()

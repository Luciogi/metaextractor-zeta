import os
from fpdf import FPDF

OUTPUT_DIR = "results"


def create_result_folder():
	os.makedirs(OUTPUT_DIR, exist_ok=True)

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

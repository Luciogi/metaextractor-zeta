import sys
from lib import *
import magic
def main():
	file = sys.argv[1]
	file_type = magic.from_file(file, mime=True)
	print(file_type)
	metadata = {}
	match file_type:
		case "image/jpeg" | "image/png" | "image/tiff":
			metadata = extract_metadata_raster_image(file)
		case "application/pdf":
			metadata = extract_metadata_pdf(file)
		case "image/svg+xml":
			metadata = extract_metadata_svg(file)
		case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
			metadata = extract_metadata_xlsx(file)
		case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
			metadata = extract_metadata_docx(file)
	if "video/" in file_type or "audio/" in file_type:
		metadata = extract_metadata_media(file)

	print_data(metadata)
if __name__ == "__main__":
	main()

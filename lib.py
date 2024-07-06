from pypdf import PdfReader # pdf
from ffmpeg import FFmpeg # audio/video
import xml.etree.ElementTree as ET  # xml
from PIL import Image, ExifTags
from docx import Document
from openpyxl import load_workbook

def extract_metadata_pdf(in_file) -> {}:
	reader = PdfReader(in_file)
	return reader.metadata

# audio and video
def extract_metadata_media(in_file) -> {}:
	ffprobe = FFmpeg(executable="ffprobe")
	ffprobe.input(in_file, print_format="xml", show_streams=None)

	metadata = ffprobe.execute()
	metadata_string = media.decode() # Convert Bytes to String

	tree = ET.fromstring(metadata_string) # Parse xml tree
	root = tree[0][0] # Set root node i.e (ffprobe -> Streams -> Stream)
	# 														Root--^
	return root.attrib

# FIXME: return proper name instead of number as key
def extract_metadata_raster_image(in_file) -> {}:
	image = Image.open(in_file)
	exif = image._getexif()
	return exif

def extract_metadata_svg(in_file) -> {}:
	tree = ET.parse(in_file)
	root = tree.getroot()
	return root.attrib

def extract_metadata_xlsx(in_file) -> {}:
	workbook = load_workbook(in_file)
	properties = workbook.properties
	metadata = {
		'creator': properties.creator,
		'title': properties.title,
		'description': properties.description,
		'subject': properties.subject,
		'identifier': properties.identifier,
		'language': properties.language,
		'created': properties.created,
		'modified': properties.modified,
		'lastModifiedBy': properties.lastModifiedBy,
		'category': properties.category,
		'contentStatus': properties.contentStatus,
		'version': properties.version,
		'revision': properties.revision,
		'keywords': properties.keywords,
		'lastPrinted': properties.lastPrinted
	}
	return metadata

def extract_metadata_docx(in_file) -> {}:
	document = Document(in_file)
	properties = document.core_properties
	metadata = {
		'title': properties.title,
		'subject': properties.subject,
		'identifier': properties.identifier,
		'language': properties.language,
		'created': properties.created,
		'modified': properties.modified,
		'last_modified_by': properties.last_modified_by,
		'category': properties.category,
		'content_status': properties.content_status,
		'version': properties.version,
		'revision': properties.revision,
		'keywords': properties.keywords,
		'last_printed': properties.last_printed,
		'comments': properties.comments
	}
	return metadata

def print_data(dictionary) -> None:
	items = dictionary.items()
	for k, v in items:
		print(k, ":", v)


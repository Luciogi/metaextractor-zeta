import zipfile
import xml.etree.ElementTree as ET
import pprint
import re
class OdfMeta:
    def __init__(self,in_file):
        self.loadFile(in_file)
        xml_str = self.readMetaXml()

        self.root = ET.fromstring(xml_str)

    def loadFile(self,in_file):
        self.zip_file = zipfile.ZipFile(in_file, mode="r")

    def readMetaXml(self):
        meta_xml = self.zip_file.read("meta.xml")
        return meta_xml

    def Properties(self) -> dict:
        meta_tag = self.root[0]
        output = {}
        # Remove namespaces
        for tag in meta_tag:
            cleaned_tag = re.sub(r"\{.*\}","", tag.tag)
            output[cleaned_tag] = tag.attrib or tag.text
        stats = {}

        # Remove namespaces
        for k,v in output["document-statistic"].items():
            cleaned_key = re.sub(r"\{.*\}", "", k)
            stats[cleaned_key] =  v

        output.pop("document-statistic")
        for k,v in stats.items():
            output[k] = v
        return output

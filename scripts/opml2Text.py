import xml.etree.ElementTree as ET

# Using this python script to extract the Feed title and Feed URL from RAW.opml to pure text. Put the RAW.opml in the same directory.

tree = ET.parse('RAW.opml')
root = tree.getroot()
if __name__ == '__main__':
    for child in root[1]:
        print(child.attrib['title'])
        for child2 in child:
            print("\t"+child2.attrib['title']+': '+child2.attrib['xmlUrl'])

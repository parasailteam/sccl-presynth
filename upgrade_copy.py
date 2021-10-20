import argparse
import pathlib
from lxml import etree as ET

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upgrade SCCL-EF file from old <copy/> tags to cpy instructions')
    parser.add_argument('file')
    args = parser.parse_args()

    tree = ET.parse(str(args.file))
    root = tree.getroot()
    for gpu in root.findall('gpu'):
        maxid = -1
        for tb in gpu.findall('tb'):
            maxid = max(maxid, int(tb.get('id')))
        new_tb = f'<tb id="{maxid+1}" send="-1" recv="-1" chan="0">\n'
        copy_indices = []
        had_copy = False
        for s, copy in enumerate(gpu.findall('copy')):
            new_tb += f'<step s="{s}" type="cpy" srcbuf="i" srcoff="{copy.get("i_off")}" dstbuf="o" dstoff="{copy.get("o_off")}" cnt="1" depid="-1" deps="-1" hasdep="0"/>\n'
            gpu.remove(copy)
            had_copy = True
        new_tb += '</tb>'
        if had_copy:
            gpu.append(ET.fromstring(new_tb))
    ET.indent(tree, '  ')
    tree.write(str(args.file))

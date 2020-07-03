import os
import PyPDF2

def parse_page(filepath, page_index):
    pdf = 'fst_undergraduate_handbook_2019-2020.pdf'
    with open(os.path.join(filepath, pdf),'rb') as handbook:
        read_handbook = PyPDF2.PdfFileReader(handbook)
        page_obj = read_handbook.getPage(page_index)
        page_content = page.extractText()

    return f"Page no. {page_index-3} {page_content}"


if __name__ == '__main__':
    with open('raw_handbook.txt','w+') as raw:
        # Parse Biochem
        for page in range(13,27):
            data = parse_page('C:\\Users\\Andrew\\Desktop\\SciTechGuideBot',page)
            raw.write(data)



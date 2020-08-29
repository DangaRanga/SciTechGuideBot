import os
import PyPDF2

def parse_page(file_path, page):
    """Parses a page from sci tech's handbook

    Args:
        file_path: The path to the pdf
        page: The page being parsed

    Returns:
        A formatted string with the page content and the page number

    """
    # Initialize key variables
    pdf = 'fst_undergraduate_handbook_2019-2020.pdf'
    with open(os.path.join(file_path, pdf),'rb') as handbook:
        read_handbook = PyPDF2.PdfFileReader(handbook)
        page_obj = read_handbook.getPage(page)
        page_content = page_obj.extractText()

    return f"Page no. {page-3} {page_content}"


if __name__ == '__main__':
    # Create file to store raw data
    with open('raw_handbook.txt','w+') as raw:
        # Parse Biochem
        for page_no in range(13,27):
            data = parse_page('C:\\Users\\Andrew\\Desktop\\SciTechGuideBot', page_no)
            raw.write(data)



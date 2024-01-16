# -*- coding: UTF-8 -*-
import os
from PIL import Image
from PyPDF4 import PdfFileReader, PdfFileWriter
import img2pdf

from fileOperation.osFileOperation.search_mkdir_rmdir_in_computer import SearchMkdirRmdirInComputer


class ImageToPdf(object):
    def imgtopdf(seft, input_paths, outputpath):
        """
        将单张图片转成单页的pdf
        :param input_paths:
        :param outputpath:
        :return:
        """
        image = Image.open(input_paths)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(outputpath, "wb")
        file.write(pdf_bytes)
        image.close()
        print("Successfully made pdf file")

    def image_to_pdf(seft, image_folder, pdf_folder):
        output_pdf_dir = pdf_folder
        output_image_dir = image_folder

        # 遍历img的文件夹，获取所有的image
        for image_page_file in os.walk(output_image_dir):
            file_list = image_page_file[2]
            for file in file_list:
                file_name = file.split(".")[0]
                suffix = file.split(".")[1]
                if suffix != "png" and suffix != "jpg" and suffix != "jpeg" and suffix != "gif":
                    continue
                page_pdf_file = os.path.join(output_pdf_dir, file_name) + ".pdf"
                page_img_file = os.path.join(output_image_dir, file)

                # 开始进行pdf 到 image的转换
                print('开始image到pdf的转换', file)
                seft.imgtopdf(page_img_file, page_pdf_file)

    def pdf_to_pdfs(seft, pdf_folder):
        """
        将单页的pdf文件合并成整个文件
        :param pdf_folder:
        :return:
        """
        # 创建一个pdf空白文档
        pdf_writer = PdfFileWriter()
        pdf_file_path = os.path.join(pdf_folder, 'combine') + ".pdf"
        # 读取每页的pdf
        for file_list in os.walk(pdf_folder):
            for file in file_list[2]:
                file_name = file.split(".")[0]
                page_pdf_file = os.path.join(pdf_folder, file_name) + ".pdf"
                # 读取单页的pdf
                # 开始进行pdf 到 image的转换
                reader = PdfFileReader(page_pdf_file, strict=False)
                pdf_writer.addPage(reader.getPage(0))
            # 保存
            pdf_writer.write(open(pdf_file_path, 'wb'))
            print("Successfully combine the PDF file")


if __name__ == '__main__':
    # 指定图片的文件夹，合成的pdf会放在下面的文件夹里面
    output_image_dir = "E:\Desktop\document\image"
    # 转换成PDF后存储的目录
    output_pdf_dir = "E:\Desktop\document"
    output_pdf_dir = os.path.join(output_pdf_dir, 'temp-pdf')
    SearchMkdirRmdirInComputer().mkDir(output_pdf_dir)

    ImageToPdf().image_to_pdf(output_image_dir, output_pdf_dir)
    ImageToPdf().pdf_to_pdfs(output_pdf_dir)

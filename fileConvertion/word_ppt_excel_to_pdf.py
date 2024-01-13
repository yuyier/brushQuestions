import os
from win32com import client

class WordPptExcelToPDF(object):
    origin_type={"word_type":1,"ppt_type":2,"excel_type":3}
    #word文档转成PDF
    def wordToPDF(self,pdf_name,doc_name):
        word = client.DispatchEx('Word.Application')
        try:
            worddoc = word.Documents.Open(doc_name, ReadOnly=1)
            worddoc.SaveAs(pdf_name, FileFormat=17) #Word另存为PDF为17
            worddoc.Close(True)
            word.Quit()
            print("save pdf file success:", pdf_name)
        except Exception as e:
            print(e)
    # PPT转成PDF
    def pptToPDF(self,pdf_name,ppt_name):
        powerpoint = client.Dispatch('Powerpoint.Application')  # WPS改为Kwpp.Application
        try:
            ppt = powerpoint.Presentations.Open(ppt_name)
            ppt.SaveAs(pdf_name, FileFormat=32)  # PPT另存为PDF为32
            ppt.Close()
            powerpoint.Quit()
        except Exception as e:
            print(e)

    def excelToPDF(self,pdf_name,excel_name):
        excel = client.Dispatch('Excel.Application')  # WPS改为Ket.Application
        try:
            xls =  excel.Workbooks.Open(excel_name)
            xls.SaveAs(pdf_name,FileFormat=57) # Excel另存为PDF为57
            xls.Close()
            excel.Quit()
        except Exception as e:
            print(e)



    def fileToPDF(self,origin_path,dirct_path,origin_type):
        for root,dirs,files in os.walk(origin_path,topdown=False):
            for name in files:
                origin_file_name=os.path.join(root,name)
                file_name,extension=os.path.splitext(name)
                suffix=extension.split(".")[1]
                dirct_file_name=os.path.join(dirct_path,file_name)+'.pdf'
                if os.path.exists(dirct_file_name):
                    os.remove(dirct_file_name)
                    print("remove exist pdf file success,", dirct_file_name)
                if origin_type==1:
                    if suffix !="docx" and suffix != "doc":
                        print("the file no need to convert:",name)
                        continue
                    self.wordToPDF(dirct_file_name,origin_file_name)
                elif origin_type==2:
                    if suffix !="ppt" :
                        print("the file no need to convert:",name)
                        continue
                    self.pptToPDF(dirct_file_name,origin_file_name)
                elif origin_type == 3:
                    if suffix !="xlsx" :
                        print("the file no need to convert:",name)
                        continue
                    self.excelToPDF(dirct_file_name,origin_file_name)




if __name__=="__main__":
    word_path="E:\Desktop\document\word"
    pdf_path="E:\Desktop\document\pdf"
    # word_to_pdf=17
    WordPptExcelToPDF().fileToPDF(word_path,pdf_path,WordPptExcelToPDF().origin_type["word_type"])
import os
from win32com import client

# word、ppt文档转PDF文档
class WordPptToPDF(object):
    origin_type={"word_type":1,"ppt_type":2,"excel_type":3}
    #word文档转成PDF
    def removeExistFile(self,dirct_file_name):
        if os.path.exists(dirct_file_name):
            os.remove(dirct_file_name)
            print("remove exist pdf file success,", dirct_file_name)
    def wordToPDF(self,pdf_name,doc_name):
        word = client.DispatchEx('Word.Application')
        try:
            self.removeExistFile(pdf_name)
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
            self.removeExistFile(pdf_name)
            ppt = powerpoint.Presentations.Open(ppt_name)
            ppt.SaveAs(pdf_name, FileFormat=32)  # PPT另存为PDF为32
            ppt.Close()
            powerpoint.Quit()
            print("save pdf file success:", pdf_name)
        except Exception as e:
            print(e)

    # def excelToPDF(self,pdf_name,excel_name):
    #     excel = client.Dispatch('Excel.Application')  # WPS改为Ket.Application
    #     try:
    #         self.removeExistFile(pdf_name)
    #         xls =  excel.Workbooks.Open(excel_name, ReadOnly=1)
    #         xls.SaveAs(pdf_name,56) # Excel另存为PDF为57
    #         excel.Quit()
    #         print("save pdf file success:", pdf_name)
    #     except Exception as e:
    #         print(e)
    #         excel.Quit()



    def fileToPDF(self,origin_path,dirct_path,origin_type):
        for root,dirs,files in os.walk(origin_path,topdown=False):
            for name in files:
                origin_file_name=os.path.join(root,name)
                file_name,extension=os.path.splitext(name)
                suffix=extension.split(".")[1]
                dirct_file_name=os.path.join(dirct_path,file_name)+'.pdf'
                if origin_type==1:
                    if suffix !="docx" and suffix != "doc":
                        print("the file no need to convert:",name)
                        continue
                    self.wordToPDF(dirct_file_name,origin_file_name)
                elif origin_type==2:
                    if suffix !="ppt" and suffix !="pptx"  :
                        print("the file no need to convert:",name)
                        continue
                    self.pptToPDF(dirct_file_name,origin_file_name)
                # elif origin_type == 3:
                #     if suffix !="xlsx" :
                #         print("the file no need to convert:",name)
                #         continue
                #     self.excelToPDF(dirct_file_name,origin_file_name)




if __name__=="__main__":
    word_path="E:\Desktop\hub文档\\2024年面试准备"
    pdf_path="E:\Desktop\hub文档\\2024年面试准备"
    WordPptToPDF().fileToPDF(word_path,pdf_path,WordPptToPDF().origin_type["word_type"])
    # WordPptToPDF().fileToPDF(word_path, pdf_path, WordPptToPDF().origin_type["ppt_type"])
    # WordPptExcelToPDF().fileToPDF(word_path, pdf_path, WordPptExcelToPDF().origin_type["excel_type"])
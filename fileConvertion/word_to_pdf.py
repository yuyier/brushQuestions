import os
from win32com import client

class WordToPDF(object):
    def wordToPDF(self,word_path,pdf_path,word_to_pdf):
        for root,dirs,files in os.walk(word_path,topdown=False):
            for name in files:
                doc_name=os.path.join(root,name)
                file_name,extension=os.path.splitext(name)
                if extension !=".docx" and extension != ".doc":
                    print("the file no need to convert:",name)
                    continue
                pdf_name=os.path.join(pdf_path,file_name)+'.pdf'
                try:
                    word=client.DispatchEx('Word.Application')
                    if os.path.exists(pdf_name):
                        os.remove(pdf_name)
                        print("remove exist pdf file success,",pdf_name)
                    worddoc=word.Documents.Open(doc_name,ReadOnly=1)
                    worddoc.SaveAs(pdf_name,FileFormat=word_to_pdf)
                    worddoc.Close(True)
                    word.Quit()
                    print("save pdf file success:",pdf_name)
                except Exception as e:
                    print(e)




if __name__=="__main__":
    word_path="E:\Desktop\document\word"
    pdf_path="E:\Desktop\document\pdf"
    word_to_pdf=17
    WordToPDF().wordToPDF(word_path,pdf_path,word_to_pdf)
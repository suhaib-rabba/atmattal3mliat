import docx
from docx import Document

suhaib=Document()

def sum(citizenName,x,y):
    p = suhaib.add_paragraph(citizenName +'/n'+ x + y)
    docName="home\\suhaibRabba\\mywork_github\\mywork3\\projectOne\\staticprojectOne\\static\\"+ citizenName+".docx"


    suhaib.save(docName)
    return citizenName


# docName="projectOne\\static\\"+ citizenName+".docx"



#关于上传form的设计:
#sex:male or female
#name:
#childnum:
#childtoparent:none,male,female
#housenum:
#carnum:
#newsaving:0 1
#othersaving 0 1
#gongtongzhaiwu 0 1


def main_algo_generate(form):
    from docx import Document

    document = Document()
    if form['sex'] == 1:
        paragraph = document.add_paragraph('男方:{}'.format(form["name"]))
    else :
        pass
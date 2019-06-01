# -*-coding:Utf-8 -*
import os
head = HEAD()
head <= LINK(rel="Stylesheet",href="../doc.css")
head <= TITLE('Collection de disques')+stylesheet
 
body = BODY()
body <= H1('Ma collection de disques')
 
table = TABLE(Class="content")
table <= TR(TH('ligne_')+TH('column_'))
for rec in records:
    table <= TR(TD(rec.titre,Class="ligne_",rec)+TD(rec.artiste,Class="column_",rec)
body <= table
 
print HTML(head+body)
os.system("pause")
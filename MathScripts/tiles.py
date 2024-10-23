# theformula is =  Area= Length* width, total boxes= (length * width)/12
length=8
width=5
Area= length * width
title_per_box= 12
Total_Boxes=(length * width)/12
print(format(Total_Boxes, ".2f"))
#for the 10% question
additional_tiles= Area * 0.10
Total_Boxes= (additional_tiles + Area)/title_per_box
print(format(Total_Boxes, ".2f"))
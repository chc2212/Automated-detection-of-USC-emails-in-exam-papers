from pytesser import *
import math
import os.path


input_range = 0
output_index=0   
with open("input/input.txt","r") as ins:
    input_text = []
    for line in ins:
        input_range =  input_range+1     
        input_text.append(line)

#for letter
break_check = 0
for x in range(1, 40):

    recogniztionString = ""
    for y in range (0,7):
        fileName = "input/e" 
        fileName = fileName + str(x)
        fienametemp = fileName
        fileName = fileName + "/"
        fileName = fileName + str(y)
        fileName = fileName + ".png"
        print fileName

       
        if os.path.isfile(fileName) == 0:
           print recogniztionString
           break_check = 1
           break    
      
        image = Image.open(fileName)
        text=image_to_string(image)     # Run tesseract.exe on image
        recogniztionString = recogniztionString + text[0]
 
    #matching the id
    if break_check == 1:
        break    

    print recogniztionString
    print input_text[1]

    break_check2=0
    for i in range(0,input_range):
        if break_check2 == 1:
            break
        matched_number=0
        length=0;
              
        if len(recogniztionString) < len(input_text[i]):
            length = len(recogniztionString)
        else :
            length = len(input_text[i])
            
        for j in range (0,length):           
           if recogniztionString[j].upper() == input_text[i][j].upper():
               matched_number=matched_number+1
           if matched_number >=2:
               print "success"  + str(matched_number)
               output_index = output_index+1
               fo = open("output/output.txt", "a")
               fo.write(str(output_index) + ": " + input_text[i])       
               fo.close()
               break_check2=1
               break
            
    if break_check2 == 0:
         output_index = output_index+1
         fo = open("output/output.txt", "a")
         fo.write(str(output_index) + ": " + "None\n")       
         fo.close()

            
break_check =0
output_index=0
#for number
for x in range(1, 40):   
    recogniztionString = ""
    for y in range (0,9):
        fileName = "input/s" 
        fileName = fileName + str(x)
        fienametemp = fileName
        fileName = fileName + "/"
        fileName = fileName + str(y)
        fileName = fileName + ".png"
        print fileName

       
        if os.path.isfile(fileName) == 0:
           print recogniztionString
           break_check = 1
           break    
      
        image = Image.open(fileName)
        text=image_to_string(image)     # Run tesseract.exe on image
        recogniztionString = recogniztionString + text[0]
 
    #matching the id

    print recogniztionString
    print input_text[1]

    if break_check == 1:
       break

    break_check2=0
    for i in range(0,input_range):
        if break_check2 == 1:
            break
        matched_number=0
        length=0;
              
        if len(recogniztionString) < len(input_text[i]):
            length = len(recogniztionString)
        else :
            length = len(input_text[i])
            
        for j in range (0,length):           
           if recogniztionString[j].upper() == input_text[i][j].upper():
               matched_number=matched_number+1
           if matched_number >=2:
               print "success"  + str(matched_number)
               output_index = output_index+1
               fo = open("output/output.txt", "a")
               fo.write(str(output_index) + ": " + input_text[i])       
               fo.close()
               break_check2=1
               break
    if break_check2 == 0:
         output_index = output_index+1
         fo = open("output/output.txt", "a")
         fo.write(str(output_index) + ": " + "None\n")       
         fo.close()

         
        
               
           
             

   
        
    
    
    

  
        
        
        


        

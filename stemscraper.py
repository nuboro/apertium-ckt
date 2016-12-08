with open("ChukchiParsing/lexemes.txt", 'r') as data:
  plaintext = data.read()

words=plaintext.split("-lexeme")


for i in range(len(words)-1):
    word=words[i+1][words[i+1].index("lex:")+4:words[i+1].index("gramm:")]
    #print(word)
    word=word.replace('\n', '')
    word=word.replace(' ', '')
    para=words[i+1].split("paradigm: ")
    #print(para)   
    for j in range(len(para)-1):
        para[j+1]=para[j+1].replace('\n', '')
        #print("!"+para[j+1])
        #print("\n")
        if para[j+1]=='adv':
            print(word+":"+word+" adv-0 ; ! # <"+ str(i) +"> stem")
        elif "N-pers" in para[j+1]:
            #print("!"+word)
            #print(word[-1:]) 
            #print(word[-2:-1]) н
            if word[-1:]not in "бвгджзкқмңпстфхцшщ'ъь": 
                if word[-2:-1] in "аояё":       
                    print(word+":"+word+" N-pers-0-1 ; ! # <"+ str(i) +"> stem") 
                elif word[-1:] in "иуюеэы":   
                    print(word+":"+word+" N-pers-0-3 ; ! # <"+ str(i) +"> stem") 
                elif  word[-1:] in "аояёеэы":
                    print(word+":"+word+" N-pers-0-4 ; ! # <"+ str(i) +"> stem")  
            elif word[-1:] in "бвгджзкқмңпстфхцшщ'ъь":  
                if word[-2:-1] in "иую": 
                    print(word+":"+word+" N-pers-0-2 ; ! # <"+ str(i) +"> stem")  


        elif "N-nom-0" in para[j+1]:
            print(word+":"+word+" N-nom-0-0-1 ; ! # <"+ str(i) +"> stem")
            print(word+":"+word+" N-nom-0-0-2  ; ! # <"+ str(i) +"> stem")
 
        elif "N-nom-n" in para[j+1]:
            print(word+":"+word+" N-nom-n-0-1 ; ! # <"+ str(i) +"> stem")
            print(word+":"+word+" N-nom-n-0-2 ; ! # <"+ str(i) +"> stem")
        elif "N-pl" in para[j+1]:
            print(word+":"+word+" N-pl ; ! # <"+ str(i) +"> stem")



        elif "N-obl" in para[j+1]:
            #print("!"+word)
            #print(word[-1:])
            #print(word[-2:-1])
            #print(word[-3:-2])
            if word[-1:]not in "бвгджзйкқлмнңпрстфхцчшщ'ъь": 
                if word[-2:-1] in "иую":
                    if word[-3:-2] in "аеёиоуыэюя":       
                        print(word+":"+word+" N-obl-0-1 ; ! # <"+ str(i) +"> stem") 
                    elif word[-3:-2] not in "аояёеэы":
                        print(word+":"+word+" N-obl-0-2 ; ! # <"+ str(i) +"> stem")        
                elif word[-2:-1] in "аояё": 
                    if word[-3:-2] in "аеёиоуыэюя": 
                        print(word+":"+word+" N-obl-0-3 ; ! # <"+ str(i) +"> stem")  
                    elif word[-3:-2] not in "иуюеэы":
                        print(word+":"+word+" N-obl-0-4 ; ! # <"+ str(i) +"> stem")  
            elif word[-1:] in "бвгджзйкқлмнңпрстфхцчшщ'ъь":  
                if word[-2:-1] in "иую":
                    if word[-3:-2] in "аеёиоуыэюя": 
                        print(word+":"+word+" N-obl-0-5 ; ! # <"+ str(i) +"> stem")  
                    elif word[-3:-2] not in "аояёеэы":
                        print(word+":"+word+" N-obl-0-6 ; ! # <"+ str(i) +"> stem")
                elif word[-2:-1] in "аояё":
                    if word[-3:-2] in "аеёиоуыэюя":
                        print(word+":"+word+" N-obl-0-7 ; ! # <"+ str(i) +"> stem")
                    elif word[-3:-2] not in "иуюеэы":
                        print(word+":"+word+" N-obl-0-8 ; ! # <"+ str(i) +"> stem")

        elif "intj" in para[j+1]:
            print(word+":"+word+" intj-0 ; ! # <"+ str(i) +"> stem") 
        elif "conj" in para[j+1]:   
            print(word+":"+word+" conj-0 ; ! # <"+ str(i) +"> stem") 

        elif "PPron-poss" in para[j+1]:   
            print(word+":"+word+" PPron-poss-0 ; ! # <"+ str(i) +"> stem") 
        elif "Pron" in para[j+1]:     
            print(word+":"+word+" Pron-0 ; ! # <"+ str(i) +"> stem") 
        elif "PART" in para[j+1]:     
            print(word+":"+word+" PART-0 ; ! # <"+ str(i) +"> stem") 
        elif "PPron-case" in para[j+1]:   
            print(word+":"+word+" PPron-case-0 ; ! # <"+ str(i) +"> stem")    
        elif "N-HA" in para[j+1]:    
            if word[-1:] not in "аеёиоуыэюя":  
                if word[-2:1] in "иую":
                    print(word+":"+word+" N-HA-0-1 ; ! # <"+ str(i) +"> stem")
                if word[-2:1] in "аояё":
                    print(word+":"+word+" N-HA-0-2 ; ! # <"+ str(i) +"> stem")   
            elif word[-1:] in "аеёиоуыэюя":
                if word[-2:1] in "иую":
                    print(word+":"+word+" N-HA-0-3 ; ! # <"+ str(i) +"> stem")
                if word[-2:1] in "аояё":
                    print(word+":"+word+" N-HA-0-4 ; ! # <"+ str(i) +"> stem")   
               
          



 


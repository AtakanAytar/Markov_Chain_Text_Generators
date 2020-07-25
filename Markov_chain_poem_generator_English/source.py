from random import randint







def remove_chars_and_html_from_text(inputt,outputt,no_of_lines):
    in_file=open(inputt,"r",encoding='utf-8')
    out_file=open(outputt,"w+",encoding='utf-8')
    line_no=0
    for line in in_file:
        forbidden=["&","\xa0","[","]","2oo*","<p>","</p>",".",",","?","<br/>","<br />",";","?",":","*","'","1","2","3","4","5","6","7","8","9","0","<",">","!","(",")"]
        for char in forbidden:
            line=line.replace(char,"")
        line_no=line_no+1
        if line_no>no_of_lines:
            return None
            
        #line=line.lstrip()
        #line=line.rstrip()
        
        out_file.write(line)
    in_file.close()
    out_file.close()
    return None

def create_chain(inputt):
    Chain={}
    in_file=open(inputt,"r",encoding='utf-8')
    for line in in_file:
        line=line.lstrip()
        line=line.rstrip()
        line=line.lower()

        
        temp_list=[]
        temp_list=line.split(" ")
        index=0
        for word in temp_list:
            lock=True
            test=word.replace(" ","")
            if test==""or test=="\n":
                lock=False

 
            if index+1!=len(temp_list) and lock: 
                
                if word in Chain:
                    next_words=Chain[word]
                    next_words=next_words+","+temp_list[index+1]
                    Chain[word]=next_words
                else:
                    Chain[word]=temp_list[index+1]
            index=index+1
                    
                
                
            
    #if word in chain:

    #else:


    return Chain

def create_text(chain,word,linecount,wordcount,frq):
    
    for b in range(linecount):
        line=""
        for a in range(wordcount):
                
            if word not in chain:
                value=randint(0,len(frq)-1)
                word=frq[value]


            possible_words=chain[word]
            possible_word_list=possible_words.split(",")
            value=randint(0,len(possible_word_list)-1)
            word=possible_word_list[value]
            line=line+word+" "
        print(line)
            
        
    return None

def merge_text_into_one_data_set(name_one,name_two,out_file):
    in_file1=open(name_one,"r",encoding='utf-8')
    in_file2=open(name_two,"r",encoding='utf-8')
    final_file=open(out_file,"a+",encoding='utf-8')
    for line in in_file1:
        final_file.write(line)
    for line in in_file2:
        final_file.write(line)
    return None
def main():
    most_freq_words=["i","you","he","she"]	
    remove_chars_and_html_from_text("poem_dataset.csv","poem_clean.txt",51000)
    Markov_Chain=create_chain("poem_clean.txt",)
    create_text(Markov_Chain,"hey",4,5,most_freq_words)   
    return None

main()
file1_path="//afx.local/dfs/home/Phylactoum/Downloads/python projects/file1.txt"
file2_path="//afx.local/dfs/home/Phylactoum/Downloads/python projects/file2.txt"
merged_path="//afx.local/dfs/home/Phylactoum/Downloads/python projects/merged.txt"

from tkinter import filedialog
from tkinter import *
file1_array = []
file2_array = []
merged_array = []  




def load_file1():
    file1_path = filedialog.askopenfilename()
    print("File 1 "+file1_path+" loaded ")
    #root.withdraw()    
    with open(file1_path) as my_file:
        for line in my_file:
            file1_array.append(line)

def load_file2():
    file2_path = filedialog.askopenfilename() 
    print("File 2 "+file1_path+" loaded ")
    #root.withdraw()  
    with open(file2_path) as my_file:
        for line in my_file:
            file2_array.append(line)
        

def merge_results():
    merged_path=filedialog.askdirectory()
    merged_path=merged_path+"/merged.txt"
    array_size_1=len(file1_array)  
    array_size_2=len(file2_array)  
    max_array=max(array_size_1,array_size_2)
    for i in range(max_array):
        if (i<array_size_1):
            merged_array.append(file1_array[i].replace("\n",""))
        if (i<array_size_2):
            merged_array.append(file2_array[i].replace("\n","")) 
       
    with open(merged_path, 'w') as the_file:
        for i in range(len(merged_array)):
            the_file.write(merged_array[i]+"\n")
    print("Files Merged") 
    
root = Tk()
root.title("Txt Merger")
load_ordersButton=Button(root,text="Load File 1",command=load_file1).pack()
load_historyButton=Button(root,text="Load File 2",command=load_file2).pack()
merge_Button=Button(root,text="Merge",command=merge_results).pack()
root.mainloop()
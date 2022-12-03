from docx import Document
import glob
import os
import yaml
import shutil
from PyPDF2 import PdfReader
from collections import OrderedDict

chars_to_remove = [".", ",", "-", "=", ";", ":", "'", "?", "(", ")", "-", "'", '"', '\u2083', '\u2192', '\u2084', '\u2081', '\u2082', '\u2085', '\u2086', '\u2087', '\u2088', '\u2089', '\u2080', '\ufb01', '\ufb02']
word_frequency={}
word_frequency_all={}
for root, dirs, files in os.walk("."):
    for name in files:
        file_name = os.path.join(root, name)
        if name.lower().endswith((".docx")):
            # print(f'Now processing {file_name}')
            # Convert the document to a list of words
            text = ""
            document = Document(file_name)
            for paragraph in document.paragraphs:
                text += ( paragraph.text +" ")
            for char in chars_to_remove:
                text = text.replace(char, "")
            words = text.split()
        elif name.lower().endswith((".pdf")):
            reader = PdfReader(file_name)
            text = ""
            for page in reader.pages:
                text += (page.extract_text()+" ")
            for char in chars_to_remove:
                text = text.replace(char, "")
            words = text.split()
        else:
            print(f'ERROR: The file {file_name} does not end with "docx" or "pdf"')
            continue
        # Count who many occurences of each word are present
        word_frequency[file_name]={ "root_folder": root}
        for word in words:  
            if word not in word_frequency[file_name].keys():
                word_frequency[file_name][word] = 0
            word_frequency[file_name][word] += 1
            if word not in word_frequency_all.keys():
                word_frequency_all[word] = 0
            word_frequency_all[word] += 1	
				
# Save the word list to an anonimous file name
word_frequency_all_sorted = OrderedDict()
for k in sorted(word_frequency_all, key=word_frequency_all.get, reverse=True):
    word_frequency_all_sorted[k] = word_frequency_all[k]
#yaml.dump(word_frequency_all_sorted, open("Word_Frequency_All_Sorted.yaml", 'w'),allow_unicode=True)
#yaml.dump(word_frequency, open("Word_Frequency.yaml", 'w'),allow_unicode=True)
              
os.mkdir("No_match")
classifiers = []
classifier = "dummy"
while classifier:
    classifier = input("Enter classifier to sort by or press Enter to finish > ")
    if classifier:
        classifiers.append(classifier)
        os.mkdir(classifier)

for file_name in word_frequency.keys():
    words =  word_frequency[file_name].keys()
    matches = 0
    for classifier in classifiers:
        found = False
        for word in words:
            if classifier in word:
                found = True
                found_classifier = classifier
        if found:		
            matches +=1
    if matches ==1:
        # Move the folder w/the matching file to under the classifier
        #print(word_frequency[file_name]["root_folder"], found_classifier)
        shutil.move(word_frequency[file_name]["root_folder"], found_classifier)
    else:
        print(f'ERROR: The file {file_name} matched { matches} classifers')
        shutil.move(word_frequency[file_name]["root_folder"], "No_match")
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk.data
import pypyodbc
import re
import os
import nltk
import string
from string import punctuation
import numpy as np
import itertools
import math
import datetime
import spacy

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

MeaningPercent = input("Anlamlı kelime yüzdesi (25/50/100)? ")

start = datetime.datetime.now()
spacy.load('en_core_web_sm')
stopWords = stopwords.words('english')
#DocumentSet =
#"C:\\Users\\Gorkem\\Source\\Repos\\MultinominalNaiveBayes\\SmallWord Eğitim
#Verileri"
DocumentSet = "D:\\Git Repos\\MultinominalNaiveBayes\\MultinominalNaiveBayes\\SmallWord Eğitim Verileri"
connection = pypyodbc.connect('Driver={SQL Server};'
                                              'Server=DESKTOP-TMO951D\GORKEMPC;'
                                               'Database=SmallWordsEducation;'
                                                 'uid=sa;pwd=1') 
cursor = connection.cursor() 

def ClearDatabase():
    SQLCommand = ("EXEC sp_MSForEachTable 'TRUNCATE TABLE ?'")
    cursor.execute(SQLCommand)
    connection.commit() 
    
#Get Content 1-gram, 2-gram, 3-gram Freqs
def GetContentFreq(content):
    #Read Words
    translator = str.maketrans('', '', string.punctuation)
    words = nltk.word_tokenize(content)
    words = [word.translate(translator) for word in words]
    #Remove one letters
    words = [word for word in words if len(word) > 1]
    #Remove numbers
    words = [word for word in words if not word.isnumeric()]
    #Convert lowercase
    words = [word.lower() for word in words]
    #Remove stop-words
    words = [word for word in words if word not in stopwords.words('english')]  

    tempWords = []
    #for word in words:
    #    word = re.sub(r'(\w)\1+', r'\1', word)
    #    tempWords.append((word))
    #words = tempWords
    tempWords = []
    for word in words:
        if word != "" and len(word) > 1:
            tempWords.append((word))
    words = tempWords
    return words

tallyTableCount = 10000



def InsertTallyTable():
    SQLCommand = ("EXEC InsertTally ?")
    Values = [tallyTableCount]
    cursor.execute(SQLCommand,Values)
    connection.commit()


def SeparateWordAndSaveDB():
    counts = dict()
    paraghraphId = 0
    ClearDatabase() #TruncateSelectedDatabase()
    InsertTallyTable()
    path = DocumentSet
    sortlist = sorted(os.listdir(path))   
    if len(sortlist) == 0:
        FillPathIfFolderPathIsEmpty()
        sortlist = sorted(os.listdir(path))
    i = 0
    while(i < len(sortlist)):
        dna = open(path + "\\" + sortlist[i],encoding='utf8',errors='ignore')
        soup = BeautifulSoup(dna,"html.parser")
        paragraphs = soup.find_all("p")
        paraghraphId = 1
        stemmer = PorterStemmer()
        for paragraph in paragraphs:           
            tokens = GetContentFreq(paragraph.text)
            tagged = pos_tag(tokens)
            nouns = [word for word,pos in tagged \
                if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
            for word in nouns:
                originalWord = word
                stems = stemmer.stem(word)
               
                if stems in counts.keys():
                    shortest,count = counts[stems]
                    counts[stems] = (shortest,count + 1)
                else:
                    counts[stems] = (stems,1)
            for kok in counts:       
                try:
                    shortest,count = counts[kok]
                    SQLCommand = ("INSERT INTO Words (DocumentId,Word, Count,StemWord,Paragraph)  VALUES (?,?,?,?,?)")
                    Values = [i,shortest,count,kok,paraghraphId]
                    cursor.execute(SQLCommand,Values)  
                    connection.commit() 
                except:
                    pass
            
        
            counts.clear()
            tokens.clear()
            nouns.clear()
            paraghraphId+=1
        try:
            SQLCommand = ("INSERT INTO Documents (Id,DocumentName,Topic,SubTopic)  VALUES (?,?,?,?)")
            Values = [i,sortlist[i],sortlist[i].split("_")[0],sortlist[i].split("_")[1]]
            cursor.execute(SQLCommand,Values)  
            connection.commit() 
            i+=1
        except:
            pass

def LastCheckMeaningWords():
    cursor.execute("SELECT StemWord FROM [SmallWordsEducation].[dbo].[MeaningWord] (nolock)")
    meaningWordList = cursor.fetchall()
    for meaningWord in meaningWordList:
        if not wordnet.synsets(meaningWord[0]):
            SQLCommand = ("DELETE FROM [SmallWordsEducation].[dbo].[MeaningWord] WHERE StemWord=?")
            Values = [meaningWord[0]]
            cursor.execute(SQLCommand,Values)  
            connection.commit() 

SeparateWordAndSaveDB()
LastCheckMeaningWords()

SQLCommand = ("EXEC InsertMeaningValue")
cursor.execute(SQLCommand)  
connection.commit() 

if MeaningPercent == '50':
   SQLCommand = ("DELETE FROM [SmallWordsEducation].[dbo].[MeaningWord] WHERE StemWord IN  (SELECT TOP (50) PERCENT StemWord FROM [SmallWordsEducation].[dbo].[MeaningWord] ORDER BY MeaningValue asc)")
   cursor.execute(SQLCommand)  
   connection.commit()
   DropWordIdCommand = ("ALTER TABLE [SmallWordsEducation].[dbo].[MeaningWord] DROP Column WordId")
   cursor.execute(DropWordIdCommand)  
   connection.commit()
   AddWordIdCommand = ("ALTER TABLE [SmallWordsEducation].[dbo].[MeaningWord] ADD  WordId INT IDENTITY(0,1)")
   cursor.execute(AddWordIdCommand)  
   connection.commit()

if MeaningPercent == '25':
   SQLCommand = ("DELETE FROM [SmallWordsEducation].[dbo].[MeaningWord] WHERE StemWord IN (SELECT TOP (75) PERCENT StemWord FROM [SmallWordsEducation].[dbo].[MeaningWord] order by MeaningValue asc)") 
   cursor.execute(SQLCommand)  
   connection.commit()
   DropWordIdCommand = ("ALTER TABLE [SmallWordsEducation].[dbo].[MeaningWord] DROP Column WordId")
   cursor.execute(DropWordIdCommand)  
   connection.commit()
   AddWordIdCommand = ("ALTER TABLE [SmallWordsEducation].[dbo].[MeaningWord] ADD  WordId INT IDENTITY(0,1)")
   cursor.execute(AddWordIdCommand)  
   connection.commit()

SelectMeaningWordCommand = ("SELECT COUNT(*) FROM MeaningWord")
cursor.execute(SelectMeaningWordCommand)
V = list(map(int,cursor.fetchall()[0]))
print("Toplam Meaning Word Sayısı:" + str(V))
#Toplam kelime sayısını bul
TotalWordsCommands = ("SELECT COUNT(*) FROM Words")
cursor.execute(TotalWordsCommands)
total_words = list(map(int,cursor.fetchall()[0]))
print("Toplam Kelime Sayısı:" + str(total_words))
def GetDocumentList():
    AllDocumentCommand = ("SELECT * FROM Documents")
    cursor.execute(AllDocumentCommand)
    return cursor.fetchall()

document_list = GetDocumentList()

def CheckContains(document,word):
    document = document[0]
    word = str(word[1]) # Stemword'ü alabilmek için word index'i 2 seçiliyor.
    IsContains = "SELECT Count(*) FROM Words WHERE DocumentId = ? and StemWord =" + "'" + word + "'" 
    documentId = [document]
    cursor.execute(IsContains,documentId)
    founded = cursor.fetchone()
    if(founded[0] > 0):
        return 1
    else:
        return 0
#Doküman vektörleri veri tabanına yazılıyor.
def WriteDocumentVectorToDB(document,document_vector,meaning_words):
    b = ",".join(str(i) for i in document_vector)
    
    InsertDocumentVector = ("INSERT INTO DocumentVector(DocumentId,Vector) VALUES(?,?) ")
    
    params = [int(document[0]),str(b)]
    
    cursor.execute(InsertDocumentVector,params)

def VectorizeDocument(document_list):
     SelectMeaningWordLoop = ("SELECT * FROM MeaningWord")
     cursor.execute(SelectMeaningWordLoop)
     meaning_words = cursor.fetchall()
     for document in document_list:
         IsDocumentContainWord = []
         for word in meaning_words:
             IsDocumentContainWord.append(CheckContains(document,word))
         WriteDocumentVectorToDB(document,IsDocumentContainWord,meaning_words)

def CalculateSingleWordProbabilityForDocuments(document):
    documentId = document[0]
    query = "SELECT TOP (1000) [DocumentId],[StemWord],[MeaningValue] FROM [SmallWordsEducation].[dbo].[MeaningWord] WHERE DocumentId=" + str(documentId)
    cursor.execute(query)
    results = cursor.fetchall()
    for r in results:
        CalculateSingleProp(r,documentId)
        
def CalculateSingleProp(r,documentId):
    singleProp = 0 
    document_list = GetDocumentList()
    vectors = GetAllVectors()
    for vector in vectors:
        if vector[r[0]] == '1':
            singleProp = singleProp + 1

    InsertSingleWordProb = ("INSERT INTO SingleWordProp(DocumentId,Word,Probability) VALUES(?,?,?) ")
    SingleWordValues = [int(documentId),r[1], singleProp / len(document_list)]
    cursor.execute(InsertSingleWordProb,SingleWordValues)

def GetDocumentVector(document):
    query = "SELECT Vector FROM [SmallWordsEducation].[dbo].[DocumentVector] WHERE DocumentId=" + str(document)
    cursor.execute(query)
    results = cursor.fetchall()
    vector = str(results[0])
    vector = vector[2:-3]
    vector_elements = vector.split(',')
    return vector_elements

def GetAllVectors():
    query = "SELECT Vector FROM [SmallWordsEducation].[dbo].[DocumentVector] "
    cursor.execute(query)
    results = cursor.fetchall()
    vector_array = []
    for idx in results:
        vector = str(idx)
        vector = vector[2:-3]
        vector_elements = vector.split(',')     
        vector_array.append(vector_elements)
    
    return vector_array

def GetWord(index):
    query = "SELECT StemWord FROM MeaningWord WHERE WordId=" + str(index)
    cursor.execute(query)
    results = cursor.fetchall()
    return str(results)

meaningwordlist = []
def GetMeainingWords():
    query = "SELECT StemWord FROM MeaningWord"
    cursor.execute(query)
    results = cursor.fetchall()
    meaningwordlist = results
    return meaningwordlist

def GetWordBag(index):
    query = "SELECT * FROM MeaningWord WHERE WordId=" + str(index)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def WriteAssociationPropToDB(word1index,word2index,prop):
    word1 = GetWord(word1index)
    word1 = word1[3:-4]
    word2 = GetWord(word2index)
    word2 = word2[3:-4]
    InsertProbs = ("INSERT INTO ProbabilitiesOfAssociation(Word1,Word1Index,Word2,Word2Index,AssociationProp) VALUES(?,?,?,?,?) ")
    InsertionValues = [word1,word1index,word2,word2index,prop]
    cursor.execute(InsertProbs,InsertionValues)

def CalculateTwoWordAssociation(i,j,documentCount):
    association = 0
    vector_list = GetAllVectors()

    for vector in vector_list:
        if vector[i] == "1" and vector[j] == "1":
            association = association + 1
    #   association = 0 ise laplace düzeltmesi uygulanacak
    association_prop = association / documentCount
    WriteAssociationPropToDB(i,j,association_prop)

def GetSingleProb(word):
    query = "SELECT Probability FROM SingleWordProp WHERE Word=" + "'" + word + "'"
    cursor.execute(query)
    prop = cursor.fetchall()
    return prop[0][0]

def GetAssociatiedProb(word1,word2):
    query = "SELECT AssociationProp FROM ProbabilitiesOfAssociation WHERE Word1=" + "'" + word1 + "'" + "AND Word2=" + "'" + word2 + "'"
    cursor.execute(query)
    prop = cursor.fetchall()
    return prop[0][0]

def CalculatePMIFinalization(i,j,document):
    documentId = document[0]
    word1 = GetWord(i)
    word1 = word1[3:-4]
    word2 = GetWord(j)
    word2 = word2[3:-4]

    TotalWordsCommands = ("SELECT COUNT(*) FROM MeaningWord")
    cursor.execute(TotalWordsCommands)
    V = list(map(int,cursor.fetchall()[0]))
    word1Bag = GetWordBag(i)
    word2Bag = GetWordBag(j)
    p1 = GetSingleProb(word1)
    p2 = GetSingleProb(word2)
    p12 = GetAssociatiedProb(word1,word2)
    PMI2 = math.log2(((float(p12)) / ((float(p1) * float(p2)))))
    print("P(" + word1 + "," + word2 + ") =" + str(PMI2))
    InsertPMI = ("INSERT INTO DocumentsPMI(WordOne,WordOneId,WordTwo,WordTwoId,DocumentId,PMI) VALUES(?,?,?,?,?,?) ")
    InsertionPMIValues = [word1,int(word1Bag[0][3]),word2,int(word2Bag[0][3]),documentId,float(PMI2)]
    cursor.execute(InsertPMI,InsertionPMIValues)

def WriteSimilarityToDB(document1,document2,result,document_list):
    topic1 = document_list[document1][2]    
    topic2 = document_list[document2][2]
    subtopic1 = document_list[document1][3]
    subtopic2 = document_list[document2][3]

    InsertSimilarity = ("INSERT INTO DocumentSimilarity(DocumentOne,DocumentOneTopic,DocumentOneSubTopic,DocumentTwo,DocumentTwoTopic,DocumentTwoSubTopic,SimilarityResult) VALUES(?,?,?,?,?,?,?) ")
    InsertionSimilarityValues = [document1,topic1,subtopic1,document2,topic2,subtopic2,float(result)]
    cursor.execute(InsertSimilarity,InsertionSimilarityValues)

def Calculate(i,j,document_list):
    s = 0
    print("D(" + str(i) + "," + str(j) + ")")
    i_vals = [] 
    D1Vector = GetDocumentVector(document_list[i][0])
    D2Vector = GetDocumentVector(document_list[j][0])
    #Dokümanlara ait vektörler çekilip, iki dokümanda da yer alan kelimeleri
    #toplam benzerliğe ekliyoruz.
    for index in range(0,len(D1Vector)):
        if(int(D1Vector[index]) == 1 and int(D2Vector[index]) == 1):
            query = "SELECT PMI FROM [SmallWordsEducation].[dbo].[DocumentsPMI] WHERE WordOneId = ?  OR WordTwoId = ?"
            params = [i,j]
            cursor.execute(query,params)
            results = cursor.fetchone()
            i_vals.append(float(results[0]))
            s = sum(i_vals)
    WriteSimilarityToDB(i,j, s,document_list)
    

def CalculateSimilarities():
    document_list = GetDocumentList()
    i_vals = []
    for i in range(0,len(document_list)): 
        i_vals.append(i) 
        for j in range(0,len(document_list)):
             if i != j :
                  Calculate(i,j,document_list)
                  
def CalculatePMI():
    document_list = GetDocumentList()
    for document in document_list:
        vectors = GetDocumentVector(document[0])

        i_vals = []
        for i in range(0,len(vectors)): 
           i_vals.append(i) 
           for j in range(0,len(vectors)):

              if i == j :
                   print("P(" + str(i) + "," + str(j) + ")")
                   CalculateTwoWordAssociation(i,j,len(document_list))
                   CalculatePMIFinalization(i,j,document)
                   
              if not j in i_vals:
                  if vectors[i] == "1" and vectors[j] == "1":
                      print("P(" + str(i) + "," + str(j) + ")")
                      CalculateTwoWordAssociation(i,j,len(document_list))
                      CalculatePMIFinalization(i,j,document)


#cosine similarity
sortlist = sorted(os.listdir(DocumentSet)) 
documentlist = []
if len(sortlist) == 0:
    FillPathIfFolderPathIsEmpty()
    sortlist = sorted(os.listdir(path))
    
i = 0

while(i < len(sortlist)):
        dna = open(DocumentSet + "\\" + sortlist[i],encoding='utf8',errors='ignore')
        soup = BeautifulSoup(dna,"html.parser")
        documentlist.append(soup)
        i+=1


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def CalculateCosineSimilarity(train_set):
    nlp = spacy.load('en')
    for i in range(0,len(document_list)): 
        for j in range(0,len(document_list)):
             if i != j :
                InsertCosineSimilarityToDB(i,j,cosine_sim(str(train_set[i].contents),str(train_set[j].contents)))
                print("D[" +  str(i) + "]" + "D[" +str(j)+"]", cosine_sim(str(train_set[i].contents),str(train_set[j].contents)))

def InsertCosineSimilarityToDB(i,j,similarity):

    topic1 = document_list[i][2]    
    topic2 = document_list[j][2]
    subtopic1 = document_list[i][3]
    subtopic2 = document_list[j][3]
    InsertSimilarity = ("INSERT INTO CosineSimilarity(DocumentOneId,DocumentOneTopic,DocumentOneSubTopic, DocumentTwoId,DocumentTwoTopic,DocumentTwoSubTopic,Similarity) VALUES(?,?,?,?,?,?,?) ")
    InsertionSimilarityValues = [i,topic1,subtopic1,j,topic2,subtopic2,float(similarity)]
    cursor.execute(InsertSimilarity,InsertionSimilarityValues)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')  
def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

CalculateCosineSimilarity(documentlist)
                 
#Dokümanların vektör olarak ifade edilmesi
VectorizeDocument(document_list)
#Kelimelerin herbir doküman içerisinden tek olarak geçme olasılıkları
for document in document_list:
    CalculateSingleWordProbabilityForDocuments(document)  
#Birlikteliklerin hesaplanması
CalculatePMI()
##Doküman benzerliklerinin hesaplanması
CalculateSimilarities()
connection.commit()
cursor.close()
end = datetime.datetime.now()
print("Elapsed Time: " + str(end - start))
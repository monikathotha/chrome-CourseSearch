import string

def remove_puncts(input_string, string):
    return input_string.translate(str.maketrans('', '', string.punctuation)).lower()

stopwordsFile = 'stopwords.txt'
dataFileCoursera = 'AlldataFileCoursera.txt'
cleanDataFileCoursera = 'cleanDataFileCoursera.txt'

dataFileCampuswire = 'AlldataFileCampuswire.txt'
cleanDataFileCampuswire = 'cleanDataFileCampuswire.txt'

def Clean_data(dataFile, cleanDataFile):
    with open(stopwordsFile, 'r') as f:
        stopwords = f.read().split()

    tokenized_corpus = []

    df = open(dataFile, "r")
    clean_df = open(cleanDataFile, "w")
    for doc in df:
        cleaned_doc = remove_puncts(doc, string)
        tokenized_doc = " ".join([word for word in cleaned_doc.lower().split() if word not in stopwords])

        clean_df.write(tokenized_doc)
        clean_df.write('\n')

Clean_data(dataFileCoursera, cleanDataFileCoursera)
Clean_data(dataFileCampuswire, cleanDataFileCampuswire)
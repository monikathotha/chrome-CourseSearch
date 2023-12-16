from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
from rank_bm25 import BM25Okapi
from flask_cors import CORS
import json
import string
from flask import request


app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route('/jsPythonCall', methods=['POST'])

def jsPythonCall():
    
    #print("Params: ", request.json)
    query = request.json
    #query = "BM25!"

    stopwordsFile = 'stopwords.txt'
    cleanDataFile = 'cleanDataFileCoursera.txt'
    allURLFile = 'AllURLFileCoursera.txt'
    topNUrlsCoursera = searchBM25(query, cleanDataFile, allURLFile)

    cleanDataFile = 'cleanDataFileCampuswire.txt'
    allURLFile = 'AllURLFileCampuswire.txt'
    topNUrlsCampuswire = searchBM25(query, cleanDataFile, allURLFile)

    AllURLs = "|".join(topNUrlsCoursera) + '|~|' + "|".join(topNUrlsCampuswire)
    print("FINAL OUTPUT: ", AllURLs)
    return AllURLs


def remove_puncts(input_string, string):
    return input_string.translate(str.maketrans('', '', string.punctuation)).lower()



def searchBM25(query, cleanDataFile, allURLFile):
    stopwordsFile = 'stopwords.txt'

    urlFile = open(allURLFile, "r")
    urlList = []
    for url in urlFile:
        urlList.append(url.replace("\n", ""))

        
    with open(stopwordsFile, 'r') as f:
        stopwords = f.read().split()

    ####    QUERY   ######
    #query = "BM25!"
    #Clean
    cleaned_query = remove_puncts(query, string)
    #TOKENIZE
    tokenized_query = [word for word in cleaned_query.lower().split() if word not in stopwords]
    print("TOKENIZED QUERY: ", tokenized_query)

    tokenized_corpus = []
    clean_df = open(cleanDataFile, "r")
    for doc in clean_df:
        #print('DOC: ', doc.split())
        tokenized_corpus.append(doc.split())
        #print('TK: ',tokenized_corpus)
    
    bm25 = BM25Okapi(tokenized_corpus)

    doc_scores = bm25.get_scores(tokenized_query)
    #print("doc_scores: ", doc_scores)
    topNUrls = bm25.get_top_n(tokenized_query, urlList, n=3)

    print("RESULT: ", bm25.get_top_n(tokenized_query, urlList, n=3))
    return topNUrls




#jsPythonCall()
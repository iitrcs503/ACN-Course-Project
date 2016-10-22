from __future__ import print_function, division
import nltk
import easygui
import os
import random
import Tkinter
import tkMessageBox
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer,sent_tokenize
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify


stoplist = stopwords.words('english')
curPath=os.path.dirname(os.path.abspath(__file__))

def init_lists(folder):
    #curPath=os.path.dirname(os.path.abspath(__file__))
    a_list = []
    file_list = os.listdir(curPath+folder)
    for a_file in file_list:
        print(str(a_file))
        f = open(curPath+folder + a_file, 'r')
        a_list.append(f.read())
        f.close()
    return a_list

def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(sentence, errors='ignore'))]
 
def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in preprocess(text) if not word in stoplist}
 
def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:] 
    print ('Training set size = ' + str(len(train_set)) + ' Tweets')
    print ('Test set size = ' + str(len(test_set)) + ' Tweets')
    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier
 
def evaluate(train_set, test_set, classifier):
    # check how the classifier performs on the training and test sets
    print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
    # check which words are most informative for the classifier   
    classifier.show_most_informative_features(20)
    
def resultDisplay(test_set,classifier):
    outputFile=open("nbOutput.txt",'w+')
    outputFile.write("Original Type\tClassified type\t\tResult Type\n")
    total=len(test_set)
    tp=tn=fp=fn=0
    for tweet in test_set:
        type=str(classifier.classify(tweet[0]))
        if str(tweet[1])==type:
             part1="True"
        else:
             part1="False"          
        if type=="spam":
             part2="Positive"
        else :
             part2="Negative"
        result=part1+" "+part2 
        outputFile.write(tweet[1]+"\t\t"+type+"\t\t\t"+result+"\n")
        if result=="True Positive" :
              tp+=1
        elif result=="True Negative":
              tn+=1
        elif result=="False Positive":
              fp+=1
        else:
              fn+=1
    outputFile.write("True Positive :"+str(float(tp/total)*100)+"%"+"\n"+"True Negative :"+str(float(tn/total)*100)+"%"+"\n"+"False Positive :"+str(float(fp/total)*100)+"%"+"\n"+"False Negative :"+str(float(fn/total)*100)+"%"+"\n")
    outputFile.write("Accuracy :"+str(float((tp+tn)/total)*100)+"%\n")
    outputFile.close()               

#collecting spams and hams from folders
spam = init_lists("/Spams/")
ham = init_lists("/NormalTweets/")

#gathering all datas
all_tweets = [(tweet, 'spam') for tweet in spam]
all_tweets += [(tweet, 'ham') for tweet in ham]
#shuffling all datasets
random.shuffle(all_tweets)

#all_words = set(word.lower() for passage in all_tweets for word in word_tokenize(passage[0]))
#for storing train features
f_out=open(curPath+"/featuresNB.txt",'w+')
all_features = [(get_features(tweet, 'bow'), label) for (tweet, label) in all_tweets] #now we got BOW style word count for each tweet with their label
f_out.write(str(all_features))

print ('Collected ' + str(len(all_features)) + ' feature sets')


train_set, test_set, classifier = train(all_features, 0.8)
print(classifier)
evaluate(train_set, test_set, classifier)
resultDisplay(test_set,classifier)

#Testing against user data
print("Please Choose tweet file..")
#top = Tkinter.Tk()
tkMessageBox.showinfo("Choose Tweet","Browse to the Tweet file Please!")
path=easygui.fileopenbox()
user_file=open(path,'r+')
test=user_file.read()
#print("Now enter the test text:\n")
#test=str(raw_input())
test_features = {word: count for word, count in Counter(preprocess(test)).items() if not word in stoplist}  #work on the text_file
#to test test data :
tkMessageBox.showinfo("Output","This tweet is "+str(classifier.classify(test_features)))

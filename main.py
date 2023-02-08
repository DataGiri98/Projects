#Cleaning text:
# 1) creating a text file
# 2) convert all the word into lowercase to compare the words
# 3) remove punctuations
import string
from collections import Counter
import matplotlib.pyplot as plt
text = open('read.text', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))


# tokenizing text
tokenized_words = cleaned_text.split()


#irrelevent words
stop_words= ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)


# Apply NLP Algorithm
# 1) Chek if the word in the final word list is present in emotion text file
# 2) if word is present then add the emotion in a list i.e. emotion list
# 3) finally count each emotion in the emotion list

# remove "," and whitespace from emotions.text
emotion_list = []
with open('emotions.text','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'","").strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w= Counter(emotion_list)
print(w)

fig, axis = plt.subplots()
axis.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show
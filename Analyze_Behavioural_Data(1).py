#for dataset importing and visualization
import pandas as pd
import matplotlib.pyplot as plt
## for cleaning purpose
import re 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv('c_history.csv')

## cleaning
cleaned_data = []
for i in range(0, len(dataset)):
  review = re.sub('[^a-zA-Z]', ' ', str(dataset['texts'][i]))
  # review = str(dataset['texts'][i])
  review = review.lower()
  review = review.split()
  #Stemming the data
  stemmer = PorterStemmer()
  review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  cleaned_data.append(review)


cv = CountVectorizer(max_features = 1500)
x = cv.fit_transform(cleaned_data).toarray()

y = dataset.iloc[:, -1] ## last column will be taken which consists of the interests
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)




classifier1 = GaussianNB()
classifier1.fit(X_train, y_train)

y_pred = classifier1.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

string = input("Enter a string -->")
new = []
new.append(string)
new = cv.transform(new).toarray()
print(type(new))
custom_predict = classifier1.predict(new)
if custom_predict == 0:
 print("Entertainment")
else:
 print("Study")
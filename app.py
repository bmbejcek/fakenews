from flask import Flask
from newspaper import Article
from requests import get
from flask import request
from flask import render_template
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#initiate app
app = Flask(__name__)

#render html (sold separately)
@app.route('/')
def my_form():
    return render_template("my-form.html")

#get url, scrape article text, feed into model, return prediction
@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['text'] #get url
    a = Article(url)
    a.download()
    a.parse() #scrape article text
    test = [a.text]

    #unpack and deploy trained count vectorizer
    count_vect = joblib.load('vectorizer.pkl')
    X_train_counts = count_vect.fit_transform(test)
    tf_transformer = TfidfTransformer()
    X_train_tfidf = tf_transformer.fit_transform(X_train_counts)

    #unpack and run trained model
    clf = joblib.load('mnnb_model.pkl')
    pred = clf.predict(X_train_tfidf)
    prob = clf.predict_proba(X_train_tfidf)

    pred_out  = str(pred[0].decode('utf-8'))
    prob_out = round(prob[0][0], 2)
    if prob[0][0] < .5:
        prob_out = 1-prob_out

    return render_template("results.html", pred = pred_out, prob = str(prob_out))

@app.route('/model')
def my_model():
    return render_template("model.html")
#run app
if __name__ == '__main__':
    app.run()

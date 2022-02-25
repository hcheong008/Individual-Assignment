#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask


# In[7]:


app = Flask(__name__)


# In[8]:


from flask import request, render_template
import joblib


# In[9]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("Income")
        age = request.form.get("Age")
        loan = request.form.get("Loan")
        print(income, age, loan)
        model = joblib.load("bc3409_elizabeth")
        pred = model.predict([[float(income), float(age), float(loan)]])
        s = "Predicted Credit Default is " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Predict Credit Default"))


# In[10]:


if __name__=="__main__":
    app.run()


# In[ ]:





from flask import Flask, render_template, request
app = Flask(__name__)
from algoliasearch.search_client import SearchClient
client = SearchClient.create('52ONG898NR', '03ab1cd7b25cef85ba00f6ad75c26954')
index = client.init_index('single')

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      
      bookmark_data = {
         
         "url": request.form["url"],
         "tags": request.form["tags"],
         "description":request.form["desc"]

      }
     
      index.save_object(bookmark_data, {'autoGenerateObjectIDIfNotExist': True})

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)

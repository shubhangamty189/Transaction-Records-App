# Import libraries
from flask import Flask, request, url_for, redirect,render_template
import requests
# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id':1, "date" : '2024-01-03','amount':60000,'firmName':'ms builders'},
    {'id':2, "date" : '2024-02-08','amount':10980,'firmName':'DIY Store'},
    {'id':3, "date" : '2024-03-23','amount':18900,'firmName':'XYZ Components'},
]


# Read operation
@app.route("/",methods = ['GET'])
def get_transactions():
    return render_template('transactions.html',transactions = transactions)
    
# Create operation
@app.route("/add",methods = ['GET',"POST"])
def add_transaction():
    if request.method =='POST':
        new_transaction = {
            "id":len(transactions)+1,
            "date": request.form['date'],
            "amount": float(request.form['amount']),
            'firmName': request.form['firmName']
        }
        transactions.append(new_transaction)
        return redirect(url_for('get_transactions'))
    return render_template("form.html")    



# Update operation
@app.route("/edit/<int:transaction_id>",methods = ["GET","POST"])
def edit_transaction(transaction_id):
    if request.method =="POST":
        date = request.form['date']
        amount = request.form['amount']
        firmName = request.form['firmName']
        for transaction in transactions:
            if(transaction['id']==transaction_id):
                transaction["date"] = date
                transaction['amount'] = amount
                transaction['firmName'] = firmName
                break
        return redirect(url_for("get_transactions"))
    for transaction in transactions:
        if transaction['id']==transaction_id:
            return render_template("edit.html",transaction = transaction) 
             

               
    

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if(transaction['id']==transaction_id):
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))    

# Search Transactions
@app.route("/search",methods = ['GET','POST']) 
def search_transactions():
    if(request.method =="POST"):
        filtered_transactions =[]
        amount1 = float(request.form['min_amount'])
        amount2 = float(request.form['max_amount'])
        for transaction in transactions:
            if(transaction["amount"]<=amount2 and transaction["amount"]>=amount1):
                filtered_transactions.append(transaction)
        return render_template("transactions.html", transactions = filtered_transactions)    
    return render_template("search.html")        




# Run the Flask app
if __name__=="__main__":
    app.run(debug = True)

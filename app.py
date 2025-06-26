from flask import Flask, render_template, request, redirect
import mysql.connector
import os

connectionPool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    host = "localhost",
    user="root",
    password="",
    database="db_shoplift"
)

app = Flask(__name__)


@app.route('/')
def Home():
    mydb = connectionPool.get_connection()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM products")
    myresult = mycursor.fetchall()
    title = "Home"
    return render_template("views/index.html",title=title, myresult=myresult)

@app.route('/products')
def Products():
    title = "Products"
    return render_template("views/products.html",title=title)

@app.route('/about')
def About():
    title = "About Us"
    return render_template("views/about.html",title=title)

@app.route('/account')
def Account():
    title = "Account"
    return render_template("views/account.html",title=title)

@app.route('/wishlist')
def Wishlist():
    title = "Wishlist"
    return render_template("views/wishlist.html",title=title)

@app.route('/cart')
def Cart():
    title = "Cart"
    return render_template("views/cart.html",title=title)

@app.route('/category')
def Category():
    title = "Categories"
    return render_template("views/category.html",title=title)

@app.route('/handleData', methods = ['POST','GET'])
def handleData():
    mydb = connectionPool.get_connection()
    mycursor = mydb.cursor(dictionary=True)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']
        address = request.form['address']
        contactNumber = request.form['contactNumber']
        sql = ("INSERT INTO users (fname,lname,password,address,contactNumber) VALUES (%s,%s,%s,%s,%s)")
        val = (fname,lname,password,address,contactNumber)
        mycursor.execute(sql,val)
        mydb.commit()
    return "SUCESSFULLY REGISTERED"

@app.route('/addProduct', methods = ['POST','GET'])
def addProduct():
    mydb = connectionPool.get_connection()
    mycursor = mydb.cursor(dictionary=True)
    if request.method == 'POST':
        productName = request.form['productName']
        productPrice = request.form['productPrice']
        sql = ("INSERT INTO products (productName,productPrice) VALUES (%s,%s)")
        val = (productName,productPrice)
        mycursor.execute(sql,val)
        mydb.commit()
    
    os.makedirs('static/images', exist_ok=True)
    existing_files = [f for f in os.listdir('static/images') if f.endswith('.png')]
    next_number = len(existing_files) + 1 

    filename = f"{next_number}.png"


    if 'fileIMG' not in request.files:
        return 'No File Part'
    file = request.files['fileIMG']
    if file.filename == '':
        return 'No Selected file'
    if file:
        file.save(os.path.join('static/images',filename))
    return Home()


if __name__ == "__main__":
    app.run(debug=True)
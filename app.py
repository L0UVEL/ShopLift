from flask import Flask, render_template
import mysql.connector

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

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template as render, request, url_for, redirect, flash, session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt 
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
blogname = "NextGen"
upload_folder = os.path.join('static', 'uploads')
app.config["UPLOAD_FOLDER"] = upload_folder

# Connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

app.secret_key = "abc123"

@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = 'SELECT * FROM posts ORDER BY update_at DESC'
    con.execute(sql)
    post = con.fetchall()
    con.close()
    return render('index.html', post=post, name=blogname)

@app.route('/article/<string:id>')
def article(id):
    con=mysql.connection.cursor()
    sql="SELECT * from posts where id=%s"
    con.execute(sql,(id,))
    article=con.fetchall()
    return render('userarticle.html',name=blogname,article=article)
@app.route("/dashboard")
def dashboard():
    con = mysql.connection.cursor()
    sql = 'SELECT * FROM posts ORDER BY update_at DESC'
    con.execute(sql)
    post = con.fetchall()
    con.close()
    if 'loggedin' in session:
        return render('dashboard.html', post=post, name=blogname)
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        con = mysql.connection.cursor()
        con.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = con.fetchone()
        if user and bcrypt.check_password_hash(user['password'], password):
            session['loggedin'] = True
            session['username'] = user['username']
            con.close()
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect username or password")
        con.close()
    return render("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashedpassword = bcrypt.generate_password_hash(password).decode('utf-8')
        con = mysql.connection.cursor()
        con.execute("SELECT * FROM users WHERE username = %s", [username])
        existing_user = con.fetchone()
        if existing_user:
            flash("Username already exists. Try a new username.")
            con.close()
            return redirect(url_for('signup'))
        sql = "INSERT INTO `users`(`username`, `password`) VALUES (%s,%s)"
        con.execute(sql, [username, hashedpassword])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("login"))
    return render("signup.html")

@app.route("/insertpost", methods=["GET", "POST"])
def insertpost():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        file = request.files['img']
        if file:
            filename = secure_filename(file.filename)
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(img_path)
            img_url = url_for('static', filename=f'uploads/{filename}')
            con = mysql.connection.cursor()
            sql = "INSERT INTO `posts`(`title`, `content`, `img_path`) VALUES (%s,%s,%s)"
            con.execute(sql, [title, content, img_url])
            mysql.connection.commit()
            con.close()
            flash("Post created successfully!")
            return redirect(url_for("dashboard"))
        else:
            flash("Please upload an image.")
    return render('insert.html', name=blogname)

@app.route("/deletepost/<string:id>", methods=["GET", "POST"])
def deletepost(id):
    con = mysql.connection.cursor()
    sql = "DELETE FROM posts WHERE id=%s"
    con.execute(sql, (id,))
    mysql.connection.commit()
    con.close()
    return redirect(url_for('dashboard'))

@app.route("/fullarticle/<string:id>")
def fullarticle(id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    con = mysql.connection.cursor()
    sql = "SELECT * FROM posts WHERE id=%s"
    con.execute(sql, (id,))
    articles = con.fetchall()
    con.close()
    return render('fullarticle.html', article=articles, name=blogname)

@app.route('/updatepost/<string:id>', methods=["GET", "POST"])
def updatepost(id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    con = mysql.connection.cursor()
    sql = "SELECT * FROM posts WHERE id=%s"
    con.execute(sql, (id,))
    article = con.fetchall()
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        file = request.files['img']
        if file:
            filename = secure_filename(file.filename)
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(img_path)
            img_url = url_for('static', filename=f'uploads/{filename}')
            con = mysql.connection.cursor()
            sql = "UPDATE posts SET title=%s, content=%s, img_path=%s WHERE id=%s"
            con.execute(sql, [title, content, img_url, id])
            mysql.connection.commit()
            con.close()
            return redirect(url_for('fullarticle', id=id))
    con.close()
    return render('update.html', article=article, name=blogname)

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

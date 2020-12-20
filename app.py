from flask import Flask, request, render_template, redirect
from functools import wraps
import MySQLdb
import re

app = Flask(__name__)

class DB:
    def __init__(self):
        self.db = MySQLdb.connect(unix_socket='/app/mysql/mysql.sock', db='lab', user='root')

    def query(self, sql):
        try:
            cur = self.db.cursor()
            cur.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            self.db = MySQLdb.connect(unix_socket='/app/mysql/mysql.sock', db='lab', user='root')
            cur = self.db.cursor()
            cur.execute(sql)

        return cur

db = DB()

blacklist = ["information", "table", "column", "schema", "=", "<", ">", "schema", "or", "and", "-", "#", "/*", "*/", "flag", ";", "'", "\"", ".", "+", "!", "\\", "order", "concat", "hex", "@", "sleep", "|", "&", "join", "like", "regexp", "if", "else", "case", "benchmark", "then", "load", "file", "_", "match", "not", "null", "glob", "in", "as", "by", "offset", "limit", "having", "intersect", "except", "false", "true", "json"]

# No where anymore bro !
blacklist += ["where"]

def check(v):
    v = v.lower()
    for b in blacklist:
        if b in v:
            return False

    m = re.search(r"\s+", v)
    return not bool(m)

def waf(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        for k in request.args:
            v = request.args[k]
            if not check(v):
                return redirect('/')

        for k in request.form:
            v = request.form[k]
            if not check(v):
                return redirect('/')

        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@waf
def hello():
    did = request.args.get("id")

    cur = db.query("select id, name from dinosaur")
    names = []
    for row in cur.fetchall():
        names.append((row[0], row[1]))

    img = "https://picsum.photos/1920/1080/?random"
    title = "Home"
    show_query = "?debug=1"

    if did:
        query = "select * from dinosaur where id = " + str(did)
        cur = db.query(query)
        dinosaur = cur.fetchone()
        title = dinosaur[1]
        img = dinosaur[2]

        if request.args.get("debug"):
           show_query = query

    return render_template("index.html", title=title, img=img, names=names, query=show_query)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

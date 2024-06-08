import sqlite3
from flask import Flask, render_template, request
db = sqlite3.connect('database.db')
cursor = db.cursor()

#  Статусы:
#    0 - нейтральный
#    1 - экзамен начат
#    11 - экзамен закончен
#    2 - старт печати
#    21 - конец печати
#    55 - хотим техника
# blyat
# suka commit?
# push & commit suka

cursor.execute("""CREATE TABLE IF NOT EXISTS kabinets (number INTEGER, kabinet TEXT UNIQUE, status TEXT)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (1,200,0)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (2,201,1)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (3,202,11)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (4,203,2)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (5,204,21)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (6,205,55)""")

cursor.execute("SELECT * FROM kabinets")
print(cursor.fetchall())

db.commit()
db.close()

app = Flask(__name__)

@app.route('/')
def main():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    all = cursor.execute("SELECT * FROM kabinets").fetchall()
    db.commit()
    db.close()
    return f"{all}"


@app.route('/<string:kab>', methods = ['POST', 'GET'])
def magic(kab):
    if request.method == 'POST':
        print("POST ROBE")
        if request.form.get('btn') == 'Dolbaeb':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Хотим Техника'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ",(st,a,))
            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()

            return render_template("kab.html", kb=kb, st=st)
        else:
            a = kab
            print(kab)
            db = sqlite3.connect('database.db')
            cursor = db.cursor()

            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? " , (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()
            return render_template("kab.html", kb = kb, st = st)
            #return f"kabpage of {kb[0]} | status: {st[0]} "
    else:
        a = kab
        print('hui')
        db = sqlite3.connect('database.db')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM kabinets").fetchall()
        kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
        st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
        db.commit()
        db.close()
        return render_template("kab.html", kb=kb, st=st)



if __name__ == "__main__":
    app.run(debug=True)
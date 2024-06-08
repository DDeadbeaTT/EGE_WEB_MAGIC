import sqlite3
from flask import Flask, render_template, request
db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS kabinets (number INTEGER, kabinet TEXT UNIQUE, status TEXT)""")
cursor.execute("""REPLACE INTO kabinets  VALUES (1,200,"нейтрал" )""")
cursor.execute("""REPLACE INTO kabinets  VALUES (2,201,"нейтрал")""")
cursor.execute("""REPLACE INTO kabinets  VALUES (3,202,"нейтрал")""")
cursor.execute("""REPLACE INTO kabinets  VALUES (4,203,"нейтрал")""")
cursor.execute("""REPLACE INTO kabinets  VALUES (5,204,"нейтрал")""")
cursor.execute("""REPLACE INTO kabinets  VALUES (6,205,"нейтрал")""")

cursor.execute("SELECT * FROM kabinets")
print(cursor.fetchall())

db.commit()
db.close()

app = Flask(__name__)

@app.route('/')
def main():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    all = cursor.execute("SELECT kabinet, status FROM kabinets").fetchall()
    db.commit()
    db.close()
    return render_template("main_page.html", all = all)


@app.route('/<string:kab>', methods = ['POST', 'GET'])
def magic(kab):
    if request.method == 'POST':
        print("POST ROBE")
        if request.form.get('btn') == 'Вызвать техника':
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
        elif request.form.get('btn') == 'Начать экзамен':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Экзамен начат'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ", (st, a,))
            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()

            return render_template("kab.html", kb=kb, st=st)
        elif request.form.get('btn') == 'Завершить экзамен':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Экзамен завершен'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ", (st, a,))
            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()

            return render_template("kab.html", kb=kb, st=st)
        elif request.form.get('btn') == 'Печать запущена':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Идет печать'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ", (st, a,))
            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()

            return render_template("kab.html", kb=kb, st=st)
        elif request.form.get('btn') == 'Печать завершена':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Печать завершена'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ", (st, a,))
            cursor.execute("SELECT * FROM kabinets").fetchall()
            kb = cursor.execute("SELECT kabinet FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            st = cursor.execute("SELECT status FROM kabinets WHERE kabinet = ? ", (a,)).fetchone()
            db.commit()
            db.close()

            return render_template("kab.html", kb=kb, st=st)
        elif request.form.get('btn') == 'Вызвать Члена ГЭК':
            print('goodlike log 1')
            db = sqlite3.connect('database.db')
            a = kab
            cursor = db.cursor()
            print(a)
            st = 'Хотим член'
            cursor.execute("UPDATE kabinets SET status = ? WHERE kabinet = ? ", (st, a,))
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
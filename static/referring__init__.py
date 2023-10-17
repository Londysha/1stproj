import os
from flask import Flask
import sqlite3
import pandas as pd
from flask import redirect, render_template, request, session
from pyecharts.charts import Bar
from pyecharts import options as opts



def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_object('config.Config')

    def get_db():
        return sqlite3.connect(app.config['DATABASE'], check_same_thread=False)

    def close_db():
        sqlite3.connect(app.config['DATABASE'], check_same_thread=False).close()

    @app.route("/")
    def login():
        session.clear()
        return render_template("login.html")

    @app.route("/query", methods=["GET", "POST"])
    def query():

        db = get_db()
        CNList = list(pd.read_sql('select distinct customer from emails', db)['customer'])

        if request.method == 'POST':
            if request.form.get('password') == '000':
                session['password'] = 'registered'

                return render_template("query.html", customernamelist=CNList)
            return redirect('/')

        if session:
            if request.method == "GET":
                name = request.args.get('customer')
                if name in CNList:
                    df = pd.read_sql(
                        f"select * from customerinfo join emails on lower(收件人邮箱地址)=lower(email) where customer like \'{name}\'",
                        db)
                    df = df.astype(
                        { '账单日期': 'datetime64', '上次付款日期': 'datetime64', '状态': 'string',
                         '收件人邮箱地址': 'string', '账单号': 'string', '账单总额': 'float64', '应付金额': 'float64',
                         'PayPal账单号': 'string'})
                    lpdate = df['上次付款日期'].max()
                    paidinv = df.loc[(df['状态'] == '已付款') | (df['状态'] == '已部分退款'), '账单总额']
                    avgttl = round(paidinv.sum() / paidinv.count(), 2) if paidinv.count() != 0 else 0
                    cnlinv = df.loc[df['状态'] == '已取消', '账单总额']
                    cnlratio = round(cnlinv.count() / df['账单号'].count(), 2) if df['账单号'].count() != 0 else 0
                    total = df['账单总额'].sum()
                    balance = df['应付金额'].sum()

                    args = {'name': name, 'total': total, 'avgttl': avgttl, 'balance': balance,
                            'customernamelist': CNList, 'cnlratio': cnlratio, 'lpdate': lpdate}

                    return render_template("query.html", **args)

                return render_template("query.html", customernamelist=CNList)

        else:

            return redirect('/')


    @app.route("/logout")
    def logout():
        session.clear()
        close_db()
        print(session)
        return redirect('/')


    @app.route("/result")
    def result():
        bar = (
            Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        )
        return render_template("result.html", bar_options=bar.dump_options())



    return app

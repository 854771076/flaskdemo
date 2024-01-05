from flask import Flask,render_template,redirect,url_for,request,flash,Markup
from flask_wtf import CSRFProtect
from forms import *
from flask_bootstrap import Bootstrap4

#数据库
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
#使用bootstrap4
bootstrap = Bootstrap4(app)
csrf = CSRFProtect(app)
app.secret_key = 'secret'

class Astock(db.Model):
    __tablename__ = 'astock'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stockid = db.Column(db.String(64))
    stockname = db.Column(db.String(64))
    company = db.Column(db.String(64))
    createtime = db.Column(db.String(64))
    category = db.Column(db.String(64))
    desc = db.Column(db.Text)
    baseInfo = db.relationship("Basicinfo", back_populates="name")

class Basicinfo(db.Model):
    __tablename__ = "basicinfo"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Province = db.Column(db.String(256))
    company_id = db.Column(db.Integer,db.ForeignKey("astock.id"))
    name = db.relationship("Astock", back_populates="baseInfo")

@app.route('/')
def hello():
    return 'Hello 2020'

@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    if form.validate_on_submit():
        flash('Form validated!')
        return redirect(url_for('index'))
    return render_template(
        'bootstrap_form.html',
        form=form,
        telephone_form=TelephoneForm(),
        contact_form=ContactForm(),
        im_form=IMForm(),
        button_form=ButtonForm(),
        example_form=ExampleForm()
    )
@app.route('/chart', methods=['GET', 'POST'])
def test_chart():
    data=[3000, 2800, 900, 1000, 800, 700, 1400, 1300, 900, 1000, 800, 600]
    return render_template('echarts.html',data=data)
@app.route('/nav', methods=['GET', 'POST'])
def test_nav():
    return render_template('bootstrap_nav.html')

@app.route('/flash', methods=['GET', 'POST'])
def test_flash():
    flash('A simple default alert—check it out!')
    flash('A simple primary alert—check it out!', 'primary')
    flash('A simple secondary alert—check it out!', 'secondary')
    flash('A simple success alert—check it out!', 'success')
    flash('A simple danger alert—check it out!', 'danger')
    flash('A simple warning alert—check it out!', 'warning')
    flash('A simple info alert—check it out!', 'info')
    flash('A simple light alert—check it out!', 'light')
    flash('A simple dark alert—check it out!', 'dark')
    flash(Markup('A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.'),'success')
    return render_template('bootstrap_flash.html')

@app.route('/pagination', methods=['GET', 'POST'])
def test_pagination():
    page = request.args.get('page', 1, type=int)
    pagination = Astock.query.paginate(page=page, per_page=10)
    messages = pagination.items
    return render_template('bootstrap_pagination.html', pagination=pagination, messages=messages)

@app.route('/table')
def test_table():
    page = request.args.get('page', 1, type=int)
    pagination = Astock.query.paginate(page=page, per_page=20)
    messages = pagination.items
    titles = [('id', '#'), ('stockid', '股票代码'), ('stockname', '股票名称'), ('company', '公司名称'), ('createtime', '上市时间'),('category', '行业分类'), ('desc', '主营业务')]
    return render_template('bootstrap_table.html', messages=messages, titles=titles, Astock=Astock)

@app.route('/table/<int:message_id>/view')
def view_message(message_id):
    message = Basicinfo.query.get(message_id)
    print(message)
    if message:
        return render_template('company.html',message=message)
    return f'Could not view message {message_id} as it does not exist. Return to <a href="/table">table</a>.'


if __name__ == '__main__':
    app.run()

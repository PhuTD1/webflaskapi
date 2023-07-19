from flask import  render_template ,redirect,url_for ,flash,request

from flaskblog import app 
from flaskblog.forms import Search 
from flaskblog.models import Student
from flask_login import login_user , current_user
import pandas as pd

data = pd.read_csv('datathpt2022f.csv')
data['SBD'] = data['SBD'].astype(str).str.zfill(8)
rank_2022 = pd.read_csv('diemcackhoi_2022.csv')



def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/tracuu/2022',methods=['GET','POST'])
def tracuu_2022():
    form = Search()
    student = None
    if form.validate_on_submit():
        student = data.loc[data['SBD'] == form.sbd.data]
        if student.empty == False:
            return render_template('tracuu.html',title = 'Tra cứu' , form = form,student = student )
        else:
            flash('không tồn tại sbd này , hãy nhập lại sbd khác' , 'danger')
    return render_template('tracuu.html',title = 'Tra cứu' , form = form ,student = student)


@app.route('/tracuu/thuhang',methods=['POST','GET'])
def tracuu_thuhang():
    rank = None
    rank_same = None
    if request.method == "POST":
        print('sucssess')
        vung = request.form['vung']
        block_code = request.form['block_code']
        total_mark = request.form['total_mark']
        if is_float(total_mark):
        
            rank = 0
            rank_same = 0
            total_mark = float(total_mark)
            if vung != 'CN' :
                rank = len(rank_2022.loc[(rank_2022['Miền'] == vung ) & (rank_2022[block_code] > total_mark)])
                rank_same = len(rank_2022.loc[(rank_2022['Miền'] == vung ) & (rank_2022[block_code] == total_mark)])
                
            else :
                rank = len(rank_2022.loc[ (rank_2022[block_code] > total_mark)])
                rank_same = len(rank_2022.loc[ (rank_2022[block_code] == total_mark)])
            print(f"{rank} : {rank_same} : {total_mark} :{vung}")
            return render_template('thuhangdiem.html',title = 'KẾT QUẢ' ,rank = rank  , rank_same = rank_same ,total_mark = total_mark,block_code = block_code , vung = vung )
    return render_template('thuhangdiem.html',title = 'Tra cứu' )
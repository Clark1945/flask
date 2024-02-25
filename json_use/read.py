import json,os,glob,datetime
from flask import Flask
import shutil

data = {'people':[{'name': 'Superman', 'website': 'superman.com', 'from': 'Mars'}]}

app = Flask(__name__)

def dump_json(dic_data):
    j_file = json.dumps(dic_data, indent=2)
    print(f'Wiil output: {j_file}')
    return j_file
def read_from_json(json_url):
    """讀取json資料"""
    json_file = open(json_url, 'r')
    # json_use.loads(json_file) #json_use.loads()用於將str型別的資料轉成Python字典
    j = json.loads(json_file.read())
    json_file.close()
    return j
@app.route("/json_use",methods=['GET'])
def json_use():
    json_dump_output = dump_json(data) # dict轉成json
    print(json_dump_output)
    config_path=os.path.join('.', 'config.json')
    json_read_output = read_from_json(config_path) # 讀取路徑並轉json
    print(json_read_output)
    return "Success"

def mytime():
    now = datetime.date.today()
    return str(now)

def backup_file(src_file, des):
    f =os.path.splitext(src_file)
    bk_file = f[0]+"_bk_"+mytime()+f[1]
    backup = os.path.join(des,bk_file)
    shutil.copy(src_file,backup)

@app.route("/glob_use",methods=['GET'])
def glob_use():
    print(glob.glob("*.json")) # 篩選檔名
    url = os.path.join(os.curdir, 'csv') # 該路徑下所有檔案名稱
    print(os.listdir(url))
    print(os.path.basename(url))
    print(os.path.abspath(url)) # 相對路徑轉絕對路徑

    WORK_PATH = os.path.join('.', 'csv')
    os.chdir(WORK_PATH)
    backup_file('xxx.html', '../target/')

    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
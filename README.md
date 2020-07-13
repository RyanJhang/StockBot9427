# StockBot9427

## GitHub
https://github.com/RyanJhang/StockBot9427

## Download and Install

### Vscode
若不會安裝請上網找安裝說明
https://code.visualstudio.com/download

#### Vscode EXTENSIONS
##### python 寫python一定要安裝
##### GitLens 

### Anaconda 為將需要的python和python module一次安裝
記得勾選增加為環境變數
https://www.anaconda.com/products/individual

#### 安裝後重開機
#### 安裝完成後，打開 powershell/cmd，輸入python，確定python版本

### GitKraken
記得刪除Update.exe
https://drive.google.com/file/d/1Ks7MMeyg_KqIe80zuh6fo9b641Wp0zBc/view?usp=sharing


## install pipenv
pipenv 是用來管理python module，也可以說成管理pip有點像虛擬環境，是為了應對不同專案可能會需要不同的環境設定module，所延伸出的虛擬pip管理
```
安裝pipenv
pip install pipenv
```
```
產生python3的虛擬環境
pipenv --three
pipenv shell
```

如果失敗請手動刪除產生出來的檔案 .virtualenvs\StockBot9427
```
pipenv --rm
```

可以進入虛擬機環境，並確認虛擬環境可以使用
```
pipenv shell
```

安裝所有 Pipfile.lock 中指定的版本套件。
```
pipenv sync
```

列出套件安裝的 dependency tree (把 Pipfile.lock 以 dependency tree 方式倒出)。
```
pipenv graph 
```

## install ngrok
流程請參照網址中流程
https://ngrok.com/download
```
https://<ngrok_uuid>.ngrok.io/is-server-alive
```

## vscode's setting
### File->Preferences->Settings-> find "python.pythonPath"
```
    "python.pythonPath": "C:\\Users\\jhang\\.virtualenvs\\StockBot9427-a5qWSRp8\\Scripts\\python.exe"
```






line 官方的開發者後台
```
https://developers.line.biz/console/provider/1654206852
```



``` run service
python app.py 9427
```


## 部屬到Heroku流程
```
# 請使用 powershell
powershell

# 切換到專案路徑
cd WORKING_DIRECTORY

# 登入 heroku
heroku login

# 改成heroku app名稱
$env:HEROKU_APP=<your_heroku_app>

# 確認是否正確
echo $env:HEROKU_APP

# 確認遠端是否正確
heroku git:remote -a $env:HEROKU_APP

# 定義 LINE的資訊到 Heroku 環境變數中
heroku config:set --app $env:HEROKU_APP LINE_USER_ID=<your_id>
heroku config:set --app $env:HEROKU_APP LINE_CHANNEL_SECRET=<your_secret_key> 
heroku config:set --app $env:HEROKU_APP LINE_CHANNEL_ACCESS_TOKEN=<your_access_token_key>

# 確認是否定義成功，有出現才是成功
heroku config --app $env:HEROKU_APP
```


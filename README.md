# Backlog APIを利用する

## Python

pip3 install requests  
pip3 install pyyaml  

## Backlog API

Web APIを使うサンプル

### ユーザー一覧を取得する

```
curl -G \
  -d apiKey=[BacklogのAPI KEY] \
  -d achieved=false \
  https://iridge.backlog.jp/api/v2/users \
| python3 -c '
from sys import stdin; import json;
print(json.dumps(json.loads(stdin.readline()), indent=2, ensure_ascii=False))
'
```

### プロジェクトIDを取得する

#### プロジェクトリストを受け取る

```
curl -G \
  -d apiKey=[BacklogのAPI KEY] \
  -d achieved=false \
  https://iridge.backlog.jp/api/v2/projects 
```

#### JSONを読みやすい形式にする

```
curl -G \
  -d apiKey=[BacklogのAPI KEY] \
  -d achieved=false \
  https://iridge.backlog.jp/api/v2/projects \
| python3 -m json.tool
```

Unicodeを日本語表示する

```
curl -G \
  -d apiKey=[BacklogのAPI KEY] \
  -d achieved=false \
  https://iridge.backlog.jp/api/v2/projects \
| python3 -c '
from sys import stdin; import json;
print(json.dumps(json.loads(stdin.readline()), indent=2, ensure_ascii=False))
'
```

### 課題を取得する

```
curl -G \
  -d apiKey=[BacklogのAPI KEY] \
  -d achieved=false \
  https://iridge.backlog.jp/api/v2/issues/JR_SHIKOKU-322
```

# This is a repository to host an endpoint which is backed by a ChatAgent

# general development tips
## generate the dependencies into requirements file
pip freeze > requirements.txt

## remove the venv files from git
git rm --cached -r /venv

# common commands for testing the application
## start the application, app.main is the package/main.py file path
uvicorn app.main:app --reload

## test get method
curl http://127.0.0.1:8000

curl http://127.0.0.1:8000/test

## test post method
curl -X 'POST' 'http://127.0.0.1:8000/chatagent' -H 'accept: application/json' -H 'Content-Type: application/json'  -d '{
  "human_input": "help me to summary for the storyline between 相柳 and 小夭 in 1000 words in Chinese"
}'


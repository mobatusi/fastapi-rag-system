curl -X 'POST' 'http://127.0.0.1:8000/uploadfile/' -F 'file=@/Users/dolu/Library/CloudStorage/OneDrive-Personal/Projects/Github/fastapi-rag-system/obama.txt'

curl -X 'POST' 'http://127.0.0.1:8000/ask/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "What is the capital of France?"
}'

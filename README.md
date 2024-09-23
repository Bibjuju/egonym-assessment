# WebUI supported image annotation

### Terminal 1 : run server on docker.
- from root directory (./) run the following commands:
  - run docker build -t annotator .
  - docker run -p 5000:5000 annotator
 
### Terminal 2 : run react web ui.
- from react-web-ui directory (./react-web-ui) run the following commands:
  - npm install
  - npm start
 
### Rest API
Endpoint: `/predict`
Method: POST
Headers: 
- `Content-Type: application/json`

Request Body:
```json
{
  "image": "<base64_encoded_image>"
}
```

Response Body:
```json
{
  "image": "<base64_encoded_image>",
  "raw_result": "<prediction_result>"
}
```


### Demo video.


https://github.com/Bibjuju/egonym-assessment/assets/33256010/4a50996b-dbf7-4c6b-88a9-7feaa43bf187




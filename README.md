# tech-interview

A test for a technical interview with JoyJet

## How to install and this app in your machine

To install this app in your machine it is necessary to have a Docker and Docker-Compose installed.

Follow these steps to install and execute it:

1. Clone the repository
1. Change to the directory of the application
1. Create a `.env` and `project.env` with the examples in `/contrib`
1. Build the application
1. Up the application
1. Run the tests stack
1. Test the application sending to it a POST request with a payload (in the code an example of the level 1)

The steps before in code:

```bash
git clone git@github.com:Riverfount/tech-interview.git
cd tech-interview
cp env-sample .env && cp sample-project-env project.env
docker-compose build --no-cash
docker-compose up -d
docker-compose run web pytest -cov
curl --request POST \
  --url http://localhost:8000/api/v1/level1/ \
  --header 'Content-Type: application/json' \
  --data '{
  "articles": [
    { "id": 1, "name": "water", "price": 100 },
    { "id": 2, "name": "honey", "price": 200 },
    { "id": 3, "name": "mango", "price": 400 },
    { "id": 4, "name": "tea", "price": 1000 }
  ],
  "carts": [
    {
      "id": 1,
      "items": [
        { "article_id": 1, "quantity": 6 },
        { "article_id": 2, "quantity": 2 },
        { "article_id": 4, "quantity": 1 }
      ]
    },
    {
      "id": 2,
      "items": [
        { "article_id": 2, "quantity": 1 },
        { "article_id": 3, "quantity": 3 }
      ]
    },
    {
      "id": 3,
      "items": []
    }
  ]
}'
```

## Football Player Transfer API

As part of the Python course, I developed a Flask API to manage football player transfers between teams. This API allows the creation of players and teams, as well as reading their information.

### Technologies Used

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- Docker

### Installation Steps

To set up and run the application using Docker, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/JeanPhilippeCaetano/transferfoot-api.git
   cd transferfoot-api/
   ```

2. Build and run the Docker containers:
   ```sh
   docker-compose up --build
   ```

### API Routes

| Route             | Method | Description                                                   |
|-------------------|--------|---------------------------------------------------------------|
| `/teams`          | POST   | Create a new team                                             |
| `/teams`          | GET    | List all existing teams                                       |
| `/teams/<id>`     | GET    | Get details of a specific team by its ID                      |
| `/players`        | POST   | Create a new player                                           |
| `/players`        | GET    | List all existing players                                     |
| `/players/<id>`   | GET    | Get details of a specific player by its ID                    |
| `/transfer`      | POST   | Transfer a player from one team to another                    |

### Example Usage

#### Create a New Team

```sh
curl -X POST http://localhost:5000/teams -H "Content-Type: application/json" -d '{
    "name": "Real Madrid",
    "city": "Madrid",
    "country": "Spain",
    "creation_date": "2022-05-01"
}'
```

#### List All Teams

```sh
curl -X GET http://localhost:5000/teams
```

#### Get Details of a Specific Team

```sh
curl -X GET http://localhost:5000/teams/1
```

#### Create a New Player

```sh
curl -X POST http://localhost:5000/players -H "Content-Type: application/json" -d '{
    "fullname" : "Jean-Philippe CAETANO",
    "birthdate" : "2003-12-13",
    "position" : "Attaquant",
    "value" : 50000000,
    "country" : "Portugal",
    "number" : 7,
    "team_id":1
}'
```

#### List All Players

```sh
curl -X GET http://localhost:5000/players
```

#### Get Details of a Specific Player

```sh
curl -X GET http://localhost:5000/players/1
```

#### Transfer a Player

```sh
curl -X POST http://localhost:5000/transfer -H "Content-Type: application/json" -d '{
    "team_id" : 1,
    "player_id" : 1,
    "transfer_date" : "2024-05-24",
    "amount" : 50000000
}'
```

### MCD

![mcd](https://github.com/JeanPhilippeCaetano/transferfoot-api/blob/main/mcd-bdd.png)

### Notes

- Ensure Docker and Docker Compose are installed on your machine.
- Update the `compose.yml` and database configuration in `config.py` as needed.

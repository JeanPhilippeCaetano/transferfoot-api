from flask import Flask, jsonify, request
from sqlalchemy.exc import OperationalError
from config import Config
from src.Models import db
from src.Models.Team import Team
from src.Models.Player import Player
from datetime import datetime

from src.Models.Transfer import Transfer


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/teams', methods=['POST'])
    def create_team():
        try:
            data = request.json
            new_team = Team(
                name=data['name'],
                city=data['city'],
                country=data['country'],
                creation_date=datetime.strptime(data['creation_date'], '%Y-%m-%d').date(),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.session.add(new_team)
            db.session.commit()
            return jsonify({'message': 'Team created successfully!'}), 201
        except OperationalError:
            return jsonify({'error': 'Database connection error'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/teams', methods=['GET'])
    def get_teams():
        teams = Team.query.all()
        return jsonify([{
            'team_id': team.team_id,
            'name': team.name,
            'city': team.city,
            'country': team.country,
            'creation_date': team.creation_date,
            'created_at': team.created_at,
            'updated_at': team.updated_at
        } for team in teams])

    @app.route('/teams/<int:team_id>', methods=['GET'])
    def get_team(team_id):
        team = Team.query.get(team_id)
        if team:
            return jsonify({
                'team_id': team.team_id,
                'name': team.name,
                'city': team.city,
                'country': team.country,
                'creation_date': team.creation_date,
                'created_at': team.created_at,
                'updated_at': team.updated_at
            })
        else:
            return jsonify({'message': 'Team not found'}), 404

    @app.route('/players', methods=['POST'])
    def create_player():
        try:
            data = request.json
            new_player = Player(
                fullname=data['fullname'],
                birthdate=datetime.strptime(data['birthdate'], '%Y-%m-%d').date(),
                position=data['position'],
                value=data['value'],
                team_id=data['team_id'],
                country=data['country'],
                number=data['number'],
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.session.add(new_player)
            db.session.commit()
            return jsonify({'message': 'Player created successfully!'}), 201
        except OperationalError:
            return jsonify({'error': 'Database connection error'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/players', methods=['GET'])
    def get_players():
        players = Player.query.all()
        if not players: return jsonify({'error': 'No players'}), 404
        return jsonify([{
            'player_id' : player.player_id,
            'fullname' : player.fullname,
            'birthdate' : player.birthdate,
            'position' : player.position,
            'value' : player.value,
            'country' : player.country,
            'number' : player.number,
            'team_id' : player.team_id,
            'created_at' : player.created_at,
            'updated_at' : player.updated_at
        } for player in players])

    @app.route('/players/<int:player_id>', methods=['GET'])
    def get_player(player_id):
        player = Player.query.get(player_id)
        if player:
            return jsonify({
            'player_id' : player.player_id,
            'fullname' : player.fullname,
            'birthdate' : player.birthdate,
            'position' : player.position,
            'value' : player.value,
            'country' : player.country,
            'number' : player.number,
            'team_id' : player.team_id,
            'created_at' : player.created_at,
            'updated_at' : player.updated_at
        })
        else:
            return jsonify({'message': 'Player not found'}), 404

    @app.route('/transfer', methods=['POST'])
    def transfer_player():
        data = request.json
        new_transfer = Transfer(
            team_id=data['team_id'],
            player_id=data['player_id'],
            transfer_date=data['transfer_date'],
            amount=data['amount'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_transfer)

        player = Player.query.get(data['player_id'])
        player.team_id = data['team_id']

        db.session.commit()
        return jsonify({'message': 'Player transferred successfully!'}), 201

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
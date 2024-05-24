from flask import Flask, jsonify, request
from sqlalchemy.exc import OperationalError
from config import Config
from src.Models import db
from src.Models.Team import Team
from datetime import datetime


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

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
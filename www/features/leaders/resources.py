from flask import jsonify, request
from flask_restful import Resource
from hfdb.queries import get_regular_season_leaders, get_player_data, get_regular_season_stat_by_player_key_and_category
from . serializers import compile_leaders_and_player_data


class LeagueLeadersRegular(Resource):
  def get(self, date=None):
    leader_data = get_regular_season_leaders(date)
    player_keys = []

    for entry in leader_data:
      player_keys_and_stats = entry.player_keys_and_stats
      player_keys += [pks['player_key'] for pks in player_keys_and_stats]

    player_data = get_player_data(list(set(player_keys)))
    serialized = compile_leaders_and_player_data(leader_data, player_data)

    return jsonify({
      'leaderboard_type': 'regular',
      'leaders': serialized
    })

class LeagueLeaderComparisonRegular(Resource):
  def get(self, player_key):
    season = request.args.get('season')
    category = request.args.get('category')

    comparison_stat_model = get_regular_season_stat_by_player_key_and_category(player_key, category, season)[0]
    comparison_stat_value = getattr(comparison_stat_model, category)

    player_data = get_player_data([player_key])[0]

    return jsonify({
      'category': category,
      'player': {
        'player': player_data.serialize(),
        'stat': comparison_stat_value
      }
    })
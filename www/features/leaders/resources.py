from flask import jsonify
from flask_restful import Resource
from hfdb.queries import get_regular_season_leaders, get_player_data
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
      'leaders': serialized
    })
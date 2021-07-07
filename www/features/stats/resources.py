from flask import jsonify
from flask_restful import Resource
from hfdb.queries import get_regular_season_stats_by_player_key


class PlayerStatsRegular(Resource):
  def get(self, player_key):
    stats_for_player = get_regular_season_stats_by_player_key(player_key)

    return jsonify({
      'stats_type': 'regular',
      'stats': [s.serialize() for s in stats_for_player]
    })
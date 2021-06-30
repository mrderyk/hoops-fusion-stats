def compile_leaders_and_player_data(leader_data=[], player_data=[]):
  player_lookup_table = create_player_lookup_table(player_data)
  serialized = []
  for l in leader_data:
    player_keys_and_stats = l.player_keys_and_stats
    serialized_leaders_for_category = [{
      'player': player_lookup_table[pks['player_key']],
      'stat': pks['stat']
    } for pks in player_keys_and_stats]

    serialized.append({
      'category': l.category,
      'leaders': serialized_leaders_for_category
    })

  return serialized

def create_player_lookup_table(player_data=[]):
  lookup_table = {}

  for p in player_data:
    lookup_table[p.key] = p.serialize()

  return lookup_table

import datetime as dt
from peewee import fn
from .. models import Player

def get_player_data(player_keys=[]):
  return Player.select().where(Player.key << player_keys)

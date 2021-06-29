import datetime as dt
from peewee import fn
from .. models import LeagueLeadersPlayoff, LeagueLeadersRegular


# TODO: Can probably DRY all these up

def get_latest_playoff_leaders():
  max_date = LeagueLeadersPlayoff.select(fn.MAX(LeagueLeadersPlayoff.date))
  return LeagueLeadersPlayoff.select().where(LeagueLeadersPlayoff.date == max_date)

def get_latest_regular_season_leaders():
  max_date = LeagueLeadersRegular.select(fn.MAX(LeagueLeadersRegular.date))
  return LeagueLeadersRegular.select().where(LeagueLeadersRegular.date == max_date)

def get_playoff_leaders(date=None):
  if date:
    try:
      d = dt.datetime.strptime(date, '%Y-%m-%d')
      return LeagueLeadersPlayoff.select().where(LeagueLeadersPlayoff.date.between(d, d + dt.timedelta(days=1)))
    except ValueError:
      return get_latest_playoff_leaders()
  else:
    return get_latest_playoff_leaders()


def get_regular_season_leaders(date=None):
  if date:
    try:
      d = dt.datetime.strptime(date, '%Y-%m-%d')
      return LeagueLeadersRegular.select().where(LeagueLeadersRegular.date.between(d, d + dt.timedelta(days=1)))
    except ValueError:
      return get_latest_regular_season_leaders()
  else:
    return get_latest_regular_season_leaders()
from www.features.health_check.resources import HealthCheck
from www.features.leaders.resources import LeagueLeadersRegular
from www.features.stats.resources import PlayerStatsRegular
from www.global_dependencies import global_dependencies

global_dependencies.api.add_resource(HealthCheck, '/health-check')
global_dependencies.api.add_resource(LeagueLeadersRegular, '/leaders/regular')
global_dependencies.api.add_resource(PlayerStatsRegular, '/stats/regular/player/<player_key>')
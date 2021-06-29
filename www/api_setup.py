from www.features.health_check.resources import HealthCheck
from www.global_dependencies import global_dependencies

global_dependencies.api.add_resource(HealthCheck, '/health-check')
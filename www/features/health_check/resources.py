from flask_restful import Resource


class HealthCheck(Resource):
  def get(self):
    formatted_service_name = '{service_name} ({app_name})'.format(
      service_name='SERVICE_NAME',
      app_name='APP_NAME'
    )

    return {
      'service': {
        'name': formatted_service_name,
        'version': 'SERVICE_VERSION'
      }
    }
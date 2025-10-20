import asana
import logging

logger = logging.getLogger(__name__)

def get_user_info(api_client: asana.ApiClient):
    try:
        user_api_instance = asana.UsersApi(api_client)
        user_info = user_api_instance.get_user(user_gid="me")
        return user_info
    except Exception as e:
        logger.error(f"Failed to get user info: {e}") 
        raise e 
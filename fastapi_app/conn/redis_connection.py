import logging

from redis import StrictRedis


def get_redis_client():
    try:
        redis_client = StrictRedis(
            host="redis", port=6379, decode_responses=True)
        logging.info("Redis is connected successfully.")
        return redis_client
    except:
        logging.exception("Redis is not connected successfully.")

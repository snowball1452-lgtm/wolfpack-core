"""Redis Bus — Connection manager for Wolf Pack.

Redis runs on port 6380 (NOT default 6379).
Provides connection pooling, health checks, and reconnection logic.
"""
import os
import logging

logger = logging.getLogger("wolfpack.redis_bus")

REDIS_PORT = int(os.environ.get("REDIS_PORT", 6380))
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")


def get_connection(decode_responses=True):
    """Get a Redis connection from the pool."""
    import redis
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=decode_responses)


def health_check():
    """Check Redis connectivity."""
    try:
        conn = get_connection()
        return conn.ping()
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        return False

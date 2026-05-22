"""Agent Communications — Redis pub/sub bus for Wolf Pack.

Channels:
  wolfpack:commands  — agent-to-agent instructions
  wolfpack:status    — heartbeat and health reports
  wolfpack:build     — build/deploy notifications
  wolfpack:intel     — research findings and alerts
  wolfpack:alert     — critical system alerts

Bus runs on Redis port 6380 (NOT default 6379).
All scripts use os.environ.get("REDIS_PORT", 6380).
"""
import os
import json
import logging

logger = logging.getLogger("wolfpack.agent_comms")

REDIS_PORT = int(os.environ.get("REDIS_PORT", 6380))
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")

CHANNELS = {
    "commands": "wolfpack:commands",
    "status":   "wolfpack:status",
    "build":    "wolfpack:build",
    "intel":    "wolfpack:intel",
    "alert":    "wolfpack:alert",
}


def publish(channel: str, message: dict, redis_client=None):
    """Publish a message to a Wolf Pack channel."""
    if redis_client is None:
        import redis
        redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    return redis_client.publish(CHANNELS.get(channel, channel), json.dumps(message))


def subscribe(channels: list, callback, redis_client=None):
    """Subscribe to Wolf Pack channels with a callback."""
    if redis_client is None:
        import redis
        redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pubsub = redis_client.pubsub()
    mapped = [CHANNELS.get(c, c) for c in channels]
    pubsub.subscribe(*mapped)
    for message in pubsub.listen():
        if message["type"] == "message":
            callback(json.loads(message["data"]))

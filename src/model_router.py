"""Model Router — Two-axis routing for Wolf Pack LLM fleet.

Axis 1: Time-of-day (train switch)
  - Green zone (off-peak): local Ollama primary
  - Yellow zone (moderate): auto-offload L3+ to NVIDIA free tier
  - Red zone (peak): NVIDIA primary, local fallback

Axis 2: Ollama budget zone
  - Tracks GPU-seconds spent on Ollama Cloud
  - NVIDIA free tier = unlimited escape hatch

Agent routing:
  - Hermes chat: L1 local, code: NVIDIA qwen3-coder
  - Hrim/Alfred/CoPAW: NVIDIA heavy always
  - Image/video: pending xAI key

API endpoints:
  /api/fuel         — current budget status
  /api/train        — current time-of-day zone
  /api/fuel/usage   — usage history
"""
import os
import logging

logger = logging.getLogger("wolfpack.model_router")

# NVIDIA fleet (free tier)
NVIDIA_MODELS = {
    "qwen3-coder":   "qwen/qwen3-coder-480b-a35b-instruct",
    "step-3.5-flash": "stepfun-ai/step-3.5-flash",
    "llama-4":       "meta/llama-4-maverick-17b-128e-instruct",
    "mistral-nemotron": "mistralai/mistral-nemotron",
    "dracarys":      "abacusai/dracarys-llama-3.1-70b-instruct",
}


def get_nvidia_base_url():
    return "https://integrate.api.nvidia.com/v1"

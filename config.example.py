"""Example configuration.

Copy this file to config.py (repository root) and fill in your own keys.
config.py is git-ignored; never commit real credentials.
"""
import os

# OpenAI-compatible LLM endpoint (Doubao, OpenAI, DeepSeek, ...)
LLM_CONFIG = {
    "api_key": os.getenv("LLM_API_KEY", ""),
    "model_name": os.getenv("LLM_MODEL", "doubao-seed-1-6-flash-250828"),
    "base_url": os.getenv("LLM_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
    "temperature": 0.7,
    "max_tokens": 8192,
}

# Mem0 cloud memory (optional; leave empty to disable long-term memory)
MEM0_CONFIG = {
    "api_key": os.getenv("MEM0_API_KEY", ""),
}

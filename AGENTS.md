# wolfpack-core — Development Guide

## Stack
- Redis 7 on port 6380 (NOT default 6379)
- Python 3.14, torch 2.11+cu128
- NVIDIA free tier API (5 models)
- Ollama Cloud for local inference

## Conventions
- `os.environ.get("REDIS_PORT", 6380)` — never hardcode 6379
- Blake3 for all witness chain hashes
- Append-only JSON chains for provenance
- MPL-2.0 license on all files

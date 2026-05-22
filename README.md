# wolfpack-core

Shared primitives for the Wolf Pack multi-agent system.

## What's Here

- **agent_comms** — Redis pub/sub bus, channel definitions, message protocols
- **redis_bus** — Connection manager (port 6380), health checks, reconnection
- **model_router** — Two-axis routing: time-of-day + Ollama budget zone, NVIDIA free tier escape hatch

## Architecture

Each Wolf Pack agent (Hermes, Hrim, Alfred, CoPAW) forks from wolfpack-core.
Shared primitives live here. Agent-specific logic lives in each fork.

```
wolfpack-core (v0.1.0) ──fork──→ hermes-agent
                              ──fork──→ hrim-arsenal
                              ──fork──→ alfred-intel
                              ──fork──→ copaw-brain
```

## License

MPL-2.0 — file-level copyleft. Corpos must credit, can mix with closed, but can't strip attribution.

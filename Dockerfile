FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim@sha256:531f855bda2c73cd6ef67d56b733b357cea384185b3022bd09f05e002cd144ca AS dev

ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PYRIGHT_PYTHON_NODE_VERSION=22.21.1 \
    RUFF_CACHE_DIR=/home/developer/.cache/ruff \
    GIT_CONFIG_COUNT=1 \
    GIT_CONFIG_KEY_0=safe.directory \
    GIT_CONFIG_VALUE_0=/workspace \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends git libatomic1 \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 10001 developer \
    && useradd --uid 10001 --gid developer --create-home developer \
    && mkdir -p /workspace/.venv /home/developer/.cache/uv \
    && chown -R developer:developer /workspace /home/developer/.cache

WORKDIR /workspace
USER developer
CMD ["uv", "run", "--locked", "pytest"]
FROM runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       tmux \
       curl \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install \
      --break-system-packages \
      --no-cache-dir \
      "vllm==0.11.2" \
      "hf_transfer==0.1.9" \
      --extra-index-url https://download.pytorch.org/whl/cu128

COPY verify-runtime.py /usr/local/bin/workbitch-verify-runtime

RUN chmod 0755 /usr/local/bin/workbitch-verify-runtime \
    && python /usr/local/bin/workbitch-verify-runtime --build

WORKDIR /workspace

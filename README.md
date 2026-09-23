# Work Bitch GPU Worker Image

Purpose:

Pre-baked runtime for disposable Work Bitch RunPod GPU workers.

Canonical runtime fingerprint:

- Ubuntu 24.04
- Python 3.12.3
- CUDA 12.8
- torch 2.9.0+cu128
- torchvision 0.24.0+cu128
- torchaudio 2.9.0+cu128
- vLLM 0.11.2
- transformers 4.57.6
- tokenizers 0.22.2
- huggingface-hub 0.36.2
- hf-transfer 0.1.9
- safetensors 0.8.0
- xformers 0.0.33.post1
- flashinfer-python 0.5.2
- tmux 3.4

Model weights are NOT included in this image.

Persistent model target:

    /workspace/models/qwen3-30b-a3b-instruct-2507-fp8

Hallelujah Drive:

    volume ID: bpwk5qdkr2
    datacenter: US-TX-3
    mount: /workspace

The image contains no API keys, SSH keys, model weights, or operator secrets.

#!/usr/bin/env python3

import os
import shutil
import sys
from importlib.metadata import version, PackageNotFoundError

EXPECTED = {
    "vllm": "0.11.2",
    "torch": "2.9.0+cu128",
    "torchvision": "0.24.0+cu128",
    "torchaudio": "2.9.0+cu128",
    "transformers": "4.57.6",
    "tokenizers": "0.22.2",
    "huggingface-hub": "0.36.2",
    "hf-transfer": "0.1.9",
    "safetensors": "0.8.0",
    "xformers": "0.0.33.post1",
    "flashinfer-python": "0.5.2",
}

build_mode = "--build" in sys.argv
bad = []

print("=== WORK BITCH RUNTIME VERIFY ===")

for package, expected in EXPECTED.items():
    try:
        actual = version(package)
    except PackageNotFoundError:
        actual = "NOT INSTALLED"

    state = "OK" if actual == expected else "MISMATCH"
    print(f"{package:22} {actual:20} {state}")

    if actual != expected:
        bad.append((package, expected, actual))

print()
print("=== RUNPOD STARTUP CONTRACT ===")

checks = {
    "/start.sh executable": os.path.isfile("/start.sh") and os.access("/start.sh", os.X_OK),
    "sshd available": shutil.which("sshd") is not None,
    "nginx available": shutil.which("nginx") is not None,
    "headless wrapper executable": (
        os.path.isfile("/usr/local/bin/workbitch-pod-start")
        and os.access("/usr/local/bin/workbitch-pod-start", os.X_OK)
    ),
}

for name, ok in checks.items():
    print(f"{name:30} {'OK' if ok else 'MISSING'}")
    if not ok:
        bad.append((name, "present", "missing"))

import torch

print()
print("torch:", torch.__version__)
print("CUDA runtime:", torch.version.cuda)

if build_mode:
    print("GPU check: skipped during image build")
else:
    print("CUDA available:", torch.cuda.is_available())

    if not torch.cuda.is_available():
        bad.append(("CUDA", "available", "unavailable"))
    else:
        print("GPU:", torch.cuda.get_device_name(0))

if bad:
    print()
    print("RUNTIME VERIFICATION FAILED")

    for name, expected, actual in bad:
        print(f"{name}: expected {expected}, got {actual}")

    raise SystemExit(1)

print()
print("RUNTIME VERIFIED")

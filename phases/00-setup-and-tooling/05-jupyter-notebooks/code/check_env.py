import os

# Check if the environment variable exists
if "CUDA_VISIBLE_DEVICES" in os.environ:
    cuda_devices = os.environ["CUDA_VISIBLE_DEVICES"]
    print(f"✅ CUDA_VISIBLE_DEVICES is set to: '{cuda_devices}'")
else:
    print("❌ CUDA_VISIBLE_DEVICES is NOT set in this environment.")

# Bonus: Check if PyTorch can actually see your GPU(s)
try:
    import torch

    print(f"PyTorch available GPUs: {torch.cuda.device_count()}")
    if torch.cuda.is_available():
        print(f"Current GPU device name: {torch.cuda.get_device_name(0)}")
except ImportError:
    print("PyTorch is not installed in this environment, skipping hardware check.")

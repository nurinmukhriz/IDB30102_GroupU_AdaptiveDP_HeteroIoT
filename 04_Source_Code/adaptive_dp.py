import torch


# Step 1: Clip the model update
def clip_update(update, max_norm=1.0):
    norm = torch.norm(update)

    if norm > max_norm:
        update = update * (max_norm / norm)

    return update


# Step 2: Select the noise level based on privacy level
def select_noise_scale(privacy_level):
    if privacy_level == "high":
        return 0.5
    elif privacy_level == "low":
        return 0.1
    else:
        return 0.3


# Step 3: Add differential privacy noise
def add_dp_noise(update, noise_scale):
    noise = torch.normal(
        mean=0.0,
        std=noise_scale,
        size=update.shape
    )

    return update + noise


# Step 4: Apply adaptive differential privacy
def apply_adaptive_dp(update, privacy_level="medium"):
    clipped_update = clip_update(update)

    noise_scale = select_noise_scale(
        privacy_level
    )

    protected_update = add_dp_noise(
        clipped_update,
        noise_scale
    )

    return protected_update

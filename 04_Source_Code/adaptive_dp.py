import torch


def clip_update(update, max_norm=1.0):
    norm = torch.norm(update)

    if norm > max_norm:
        update = update * (max_norm / norm)

    return update


def add_dp_noise(update, noise_scale):
    noise = torch.normal(
        mean=0.0,
        std=noise_scale,
        size=update.shape
    )

    return update + noise


def apply_adaptive_dp(update, privacy_level="medium"):
    if privacy_level == "high":
        noise_scale = 0.5
    elif privacy_level == "low":
        noise_scale = 0.1
    else:
        noise_scale = 0.3

    clipped_update = clip_update(update)
    protected_update = add_dp_noise(
        clipped_update,
        noise_scale
    )

    return protected_update

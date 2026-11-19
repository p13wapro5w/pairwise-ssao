import math

def hemisphere_angle(index, total):
    """半球采样角。"""
    raise NotImplementedError("TODO: hemisphere_angle")

def noise_uv(x, y, size):
    """噪声去重复。"""
    raise NotImplementedError("TODO: noise_uv")

def linear_depth(z, near, far):
    """深度重建。"""
    raise NotImplementedError("TODO: linear_depth")

def ao_radius(world_radius, pixels_per_unit):
    """世界半径。"""
    raise NotImplementedError("TODO: ao_radius")

def normal_weight(dot_value, bias):
    """法线权重。"""
    raise NotImplementedError("TODO: normal_weight")

def depth_weight(delta, scale):
    """深度权重。"""
    raise NotImplementedError("TODO: depth_weight")

def upsample_scale(scale, factor):
    """上采样。"""
    raise NotImplementedError("TODO: upsample_scale")

def transparent_occluder(alpha, threshold):
    """透明剔除。"""
    raise NotImplementedError("TODO: transparent_occluder")

def distance_falloff(distance, max_distance):
    """距离衰减。"""
    raise NotImplementedError("TODO: distance_falloff")

def ao_normalize(total, count):
    """AO 归一。"""
    raise NotImplementedError("TODO: ao_normalize")

def blur_kernel(radius):
    """双边核。"""
    raise NotImplementedError("TODO: blur_kernel")

def half_res(width):
    """半分辨率。"""
    raise NotImplementedError("TODO: half_res")

def sample_count(quality, base):
    """采样数。"""
    raise NotImplementedError("TODO: sample_count")

def apply_ao(ao, indirect):
    """AO 应用。"""
    raise NotImplementedError("TODO: apply_ao")

def camera_ao_key(camera_id, frame):
    """相机 AO 隔离。"""
    raise NotImplementedError("TODO: camera_ao_key")

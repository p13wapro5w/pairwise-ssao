import pytest
from render import ssao as mod

CASES = [
    ("angle", 'm.hemisphere_angle(1, 4) == approx(1.5707963, rel=1e-5)'),
    ("noise", 'm.noise_uv(5, 7, 4) == (0.25, 0.75)'),
    ("depth0", 'm.linear_depth(0, 0.1, 100) == approx(0.1)'),
    ("depth1", 'm.linear_depth(1, 0.1, 100) == approx(100.0)'),
    ("radius", 'm.ao_radius(0.5, 2) == approx(1.0)'),
    ("normal", 'm.normal_weight(0.8, 0.2) == approx(0.6)'),
    ("dweight", 'm.depth_weight(0, 1) == approx(1.0)'),
    ("upsample", 'm.upsample_scale(2, 2) == 4'),
    ("transparent", 'm.transparent_occluder(0.2, 0.5) is False'),
    ("falloff", 'm.distance_falloff(5, 10) == approx(0.5)'),
    ("norm", 'm.ao_normalize(2, 4) == approx(0.5)'),
    ("blur", 'm.blur_kernel(2) == 5'),
    ("half", 'm.half_res(7) == 3'),
    ("samples", 'm.sample_count(2, 8) == 16'),
    ("apply", 'm.apply_ao(0.5, 2.0) == approx(1.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})

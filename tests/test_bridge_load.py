import pytest
import game.bridge_load as mod

CASES = [
    ("stress_iterate_converge", (1,)),
    ("load_contact_backtrack", (1,)),
    ("structure_version_snapshot", (1,)),
    ("edit_order_authority", (1,)),
    ("mesh_rigid_handoff", (1,)),
    ("collider_reclaim", (1,)),
    ("load_bridge", (1,)),
    ("build_beam", (1,)),
    ("solve_structure", (1,)),
    ("present_bridge", (1,)),
    ("validate_bridge", (1,)),
    ("metrics_bridge", (1,)),
    ("audit_bridge", (1,)),
    ("fallback_bridge", (1,)),
    ("determinism_bridge", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

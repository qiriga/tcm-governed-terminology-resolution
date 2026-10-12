from enum import Enum

class DecisionLevel(str, Enum):
    A = "LEVEL_A_EXACT"
    B = "LEVEL_B_VERIFIED_ALIAS"
    C = "LEVEL_C_NORMALIZED"
    D = "LEVEL_D_FUZZY_CANDIDATE"
    E = "LEVEL_E_AMBIGUOUS"
    F = "LEVEL_F_UNSUPPORTED"

AUTO_LEVELS = frozenset({DecisionLevel.A, DecisionLevel.B, DecisionLevel.C})

def may_emit_factual_binding(level: DecisionLevel, eligible_count: int) -> bool:
    return level in AUTO_LEVELS and eligible_count == 1

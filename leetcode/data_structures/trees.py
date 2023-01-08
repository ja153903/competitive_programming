from dataclasses import dataclass
from typing import Self, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[Self] = None
    right: Optional[Self] = None

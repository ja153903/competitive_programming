from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class ListNode:
    val: int
    next: Optional[Self] = None

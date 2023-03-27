"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Network(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BOND_REWARD_RUNE_FIELD_NUMBER: builtins.int
    TOTAL_BOND_UNITS_FIELD_NUMBER: builtins.int
    BURNED_BEP2_RUNE_FIELD_NUMBER: builtins.int
    BURNED_ERC20_RUNE_FIELD_NUMBER: builtins.int
    LPINCOMESPLIT_FIELD_NUMBER: builtins.int
    NODEINCOMESPLIT_FIELD_NUMBER: builtins.int
    bond_reward_rune: builtins.str
    total_bond_units: builtins.str
    burned_bep2_rune: builtins.str
    burned_erc20_rune: builtins.str
    LPIncomeSplit: builtins.int
    NodeIncomeSplit: builtins.int
    def __init__(
        self,
        *,
        bond_reward_rune: builtins.str = ...,
        total_bond_units: builtins.str = ...,
        burned_bep2_rune: builtins.str = ...,
        burned_erc20_rune: builtins.str = ...,
        LPIncomeSplit: builtins.int = ...,
        NodeIncomeSplit: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["LPIncomeSplit", b"LPIncomeSplit", "NodeIncomeSplit", b"NodeIncomeSplit", "bond_reward_rune", b"bond_reward_rune", "burned_bep2_rune", b"burned_bep2_rune", "burned_erc20_rune", b"burned_erc20_rune", "total_bond_units", b"total_bond_units"]) -> None: ...

global___Network = Network
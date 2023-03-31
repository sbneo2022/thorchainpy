from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="NetworkResponse")


@attr.s(auto_attribs=True)
class NetworkResponse:
    """
    Attributes:
        bond_reward_rune (str): total amount of RUNE awarded to node operators Example: 857134475040.
        burned_bep_2_rune (str): total of burned BEP2 RUNE Example: 674699077345087.
        burned_erc_20_rune (str): total of burned ERC20 RUNE Example: 66369401654835.
        total_bond_units (str): total bonded RUNE Example: 0.
        total_reserve (str): total reserve RUNE Example: 21999180112172346.
        vaults_migrating (bool): Returns true if there exist RetiringVaults which have not finished migrating funds to
            new ActiveVaults
    """

    bond_reward_rune: str
    burned_bep_2_rune: str
    burned_erc_20_rune: str
    total_bond_units: str
    total_reserve: str
    vaults_migrating: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bond_reward_rune = self.bond_reward_rune
        burned_bep_2_rune = self.burned_bep_2_rune
        burned_erc_20_rune = self.burned_erc_20_rune
        total_bond_units = self.total_bond_units
        total_reserve = self.total_reserve
        vaults_migrating = self.vaults_migrating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bond_reward_rune": bond_reward_rune,
                "burned_bep_2_rune": burned_bep_2_rune,
                "burned_erc_20_rune": burned_erc_20_rune,
                "total_bond_units": total_bond_units,
                "total_reserve": total_reserve,
                "vaults_migrating": vaults_migrating,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bond_reward_rune = d.pop("bond_reward_rune")

        burned_bep_2_rune = d.pop("burned_bep_2_rune")

        burned_erc_20_rune = d.pop("burned_erc_20_rune")

        total_bond_units = d.pop("total_bond_units")

        total_reserve = d.pop("total_reserve")

        vaults_migrating = d.pop("vaults_migrating")

        network_response = cls(
            bond_reward_rune=bond_reward_rune,
            burned_bep_2_rune=burned_bep_2_rune,
            burned_erc_20_rune=burned_erc_20_rune,
            total_bond_units=total_bond_units,
            total_reserve=total_reserve,
            vaults_migrating=vaults_migrating,
        )

        network_response.additional_properties = d
        return network_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

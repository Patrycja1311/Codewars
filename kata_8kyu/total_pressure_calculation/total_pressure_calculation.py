def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    gas_constant = 0.082
    return (given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * gas_constant * (temp + 273.15) / volume

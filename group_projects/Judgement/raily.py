
easy_prompt = "enter prompt here"
easy_accepted = "accepted consequences"
easy_denied = "denied consequences"

medium_prompt = "enter prompt here"
medium_denied = "denied consequence"
medium_accepted = "accepted consequence"

hard_prompt = "enter prompt here"
hard_accepted = "enter accepted consequence"
hard_denied = "enter denied consequences"

#dictionary
PRE_1 = (
    "NAME: Aileen Wuornos\n"
    "AGE: 34\n"
    "HEIGHT: 5'4\n"
    "WEIGHT: 145 pounds\n"
    "EYES: Brown\n"
    "RACE: White\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Arrested in Florida on an outstanding warrant while driving a vehicle belonging to a missing man. Investigators linked her to the shooting deaths of seven men along state highways over a one-year period, recovering victims' personal belongings pawned under her aliases. Aileen claimed she acted in self-defense during every encounter, though ballistic evidence and witness sightings showed a consistent pattern of robbery and fatal shootings.",
    "Ballistics confirmed the weapon in her possession matched all seven highway homicides. Denying release prevented further fatalities.",
    "After being released on bail, she stole another vehicle and committed another fatal highway robbery before being recaptured.",
)
prompt, denied, accepted = PRE_1

PRM_1 = (
    "NAME: Anna Sorokin\n"
    "AGE: 26\n"
    "HEIGHT: 5'5\n"
    "WEIGHT: 125 pounds\n"
    "EYES: Blue\n"
    "RACE: White\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Arrested in California while leaving an addiction treatment facility after skipping out on tens of thousands of dollars in luxury hotel bills in New York. Police found forged bank statements showing a fake 60-million-euro trust fund used to defraud banks, hotels, and private jet operators out of roughly $275,000. Anna claimed her actions were merely aggressive business negotiations and that she intended to pay everyone back once her venture launched.",
    "Investigators uncovered multiple fake passports and international wire fraud schemes. Holding her prevented her from fleeing the country.",
    "Upon release, she immediately used a new alias to defraud another boutique hotel out of $30,000 before skipping town.",
)
prompt, denied, accepted = PRM_1
PRM_2 = (
    "NAME: Dorothea Puente\n"
    "AGE: 59\n"
    "HEIGHT: 5'3\n"
    "WEIGHT: 135 pounds\n"
    "EYES: Brown\n"
    "RACE: White\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Arrested in California after social workers reported that an elderly, mentally disabled tenant had vanished from her unlicensed boarding house. Dorothea claimed the tenant had simply gone on a trip with relatives, though neighbors reported a foul odor coming from her freshly dug garden and she was caught cashing the tenant's Social Security checks.",
    "Excavation of her backyard uncovered seven bodies buried in the garden. You made the right call keeping her in custody.",
    "Released due to lack of immediate evidence, she fled to Los Angeles and attempted to befriend another elderly retiree in a bar.",
)
prompt, denied, accepted = PRM_2
PRH_1 = (
    "NAME: Susan Wright\n"
    "AGE: 26\n"
    "HEIGHT: 5'4\n"
    "WEIGHT: 120 pounds\n"
    "EYES: Blue\n"
    "RACE: White\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Arrested in Texas after her attorney alerted authorities to a body buried in the backyard of her family home. Investigators discovered her husband bound to a bed frame with neckties and stabbed 193 times with two knives, alongside evidence that she had repainted the bedroom walls and filed a false domestic abuse report the day after the killing. Susan claimed she acted in self-defense after years of severe physical and sexual abuse, though prosecutors pointed to a recently purchased $200,000 life insurance policy and the restraint of the victim as signs of premeditation.",
    "Forensic blood spatter analysis contradicted her self-defense timeline, leading to a murder conviction.",
    "Released on bond pending trial, she complied with all court appearances and posed no further threat to the public.",
)
prompt, denied, accepted = PRH_1
PRH_2 = (
    "NAME: Casey Anthony\n"
    "AGE: 22\n"
    "HEIGHT: 5'2\n"
    "WEIGHT: 115 pounds\n"
    "EYES: Blue\n"
    "RACE: White\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Arrested in Florida for child neglect, making false official statements, and obstructing an investigation after her two-year-old daughter went missing for 31 days without being reported. Police detected an odor of human decomposition in the trunk of her abandoned car and found that she had lied about her employment and a babysitter's identity. Casey claimed she had not reported the disappearance because she was conducting her own search and was afraid of her family's reaction.",
    "Searchers later found the child's remains in a wooded area near the family home with duct tape over the mouth.",
    "Released on bond, she remained under strict home confinement and public scrutiny without committing further offenses.",
)

# Dictionary storing all profiles organized by difficulty (including duplicates/extras)
profiles_dict = {
    "EASY": [PRE_1],
    "MEDIUM": [PRM_1, PRM_2],
    "HARD": [PRH_1, PRH_2],
}

prompt, denied, accepted = profiles_dict["EASY", "MEDIUM", "HARD"][0]

this was doing some weird stuff with the program not sure what was happening
"""

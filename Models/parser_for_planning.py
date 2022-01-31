'''
This module serves as planning unit and will be removed, once the package is finished. it is used to plan how the retrobiocat data model can be parsed to the BioCatHub model
'''

Retrobiocat_model = [{
    "cofactors": [
        [
            "Amine"
        ],
        [
            "Carbonyl"
        ]
    ],
    "enzyme": "TA",
    "products": [
        "CC(=O)c1ccccc1"
    ],
    "reaction": "Secondary amine deamination",
    "substrates": [
        "CC(N)c((((((1ccccc1"
    ]
},
    {
    "cofactors": [
        [
            "NAD(P)H"
        ],
        [
            "NAD(P)"
        ]
    ],
    "enzyme": "ADH",
    "products": [
        "CC(=O)c1ccccc1"
    ],
    "reaction": "Secondary alcohol oxidation",
    "substrates": [
        "CC(O)c1ccccc1"
    ]
}
]

enzymes = [
    {
        "name": "TA",
                "reactions": [
                    {
                        "name": "Secondary amine deamination",
                        "educts": [
                                {
                                    "name": "",
                                    "role": "substrate",
                                    "smiles": "CC(N)c1ccccc1"
                                },
                            {
                                    "name": "Amine",
                                    "role": "Cofactor",
                                    "smiles": ""
                                },
                            {
                                    "name": "Carbonyl",
                                    "role": "Cofactor",
                                    "smiles": ""
                                }
                        ],
                        "products": [
                            {
                                "name": "",
                                "role": "product",
                                "smiles": "CC(=O)c1ccccc1"
                            }
                        ]
                    }
                ]

    }
]

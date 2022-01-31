import pytest
import os
import tempfile
import json

from app import create_app
from Models.parser_for_planning import Retrobiocat_model as rbc_model


test_data = [{"substrates": ["CC(N)c1ccccc1"],
                  "products": ["CC(=O)c1ccccc1"],
                  "cofactors": [["Amine"], ["Carbonyl"]],
                  "enzyme": "TA",
                  "reaction": "Secondary amine deamination",
                  }]

def test_minimongo():
    app = create_app()
    with app.test_client() as client:        
        rv = client.post('/retrobiohub/minimongo/')
        assert rv.status_code == 200 

def test_retrobiohub_create():
    app = create_app()
    with app.test_client() as client:
        rv = client.post('/retrobiohub/',json=rbc_model)
        assert rv.status_code == 200 

def test_case():
    app = create_app()
    with app.test_client() as client:
        rv = client.post('/retrobiohub/',json=test_data)
        assert rv.status_code == 200

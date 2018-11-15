# coding: utf-8
import requests

correios_url = "https://viacep.com.br/ws/{cep}/json/"


def test_scrap_request():
    cep = "20271020"
    response = requests.get(correios_url.format(cep=cep))

    assert response.status_code is 200

    response.encoding="UTF-8"
    json_data = response.json()

    assert json_data['bairro'] == u'Maracanã'

"""
Teste feito em 3 etapas (AAA)
- Arrange: preparar cenário, criar objetos, config. dependências, iniciar dados
- Act: Executar ação ou método testado
- Assert: Validar se o resultado da ação corresponde ao experado
"""

from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():

    # Arrange (instância de TestClient passando o nosso arquivo para testes)
    client = TestClient(app)

    # Act (faz a chamada pelo método GET no root)
    response = client.get('/')

    # Assert (garante que a resposta seja o que queremos)
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK

"""
Teste feito em 3 etapas (AAA)
- Arrange: preparar cenário, criar objetos, config. dependências, iniciar dados
- Act: Executar ação ou método testado
- Assert: Validar se o resultado da ação corresponde ao experado
"""

from http import HTTPStatus

# Arrange (instância de TestClient passando o nosso arquivo para testes)
"""@pytest.fixture
def client():
    return TestClient(app)"""


def test_root_deve_retornar_ola_mundo(client):

    # Act (faz a chamada pelo método GET no root)
    response = client.get('/')

    # Assert (garante que a resposta seja o que queremos)
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_olamundo_retorna_html(client):

    response = client.get('olamundo')

    assert '<h1>Olá, Mundo!</h1>' in response.text

    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'teste',
            'email': 'teste@teste.com',
            'password': 'teste123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'teste@teste.com',
        'username': 'teste',
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'teste@teste.com',
                'username': 'teste',
            }
        ]
    }


def test_read_users_by_id(client):

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'teste@teste.com',
        'username': 'teste',
    }


def test_read_users_by_id_not_found(client):

    response = client.get('/users/132132132131')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!'}


def test_update_user(client):

    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'senha123',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_update_user_not_found(client):

    response = client.put(
        '/users/43024302',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'senha123',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!'}


def test_delete_user(client):

    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_delete_user_not_fount(client):

    response = client.delete('/users/123131321321')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!'}

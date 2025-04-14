import pytest
from httpx import AsyncClient

from schemas.table import Table


@pytest.mark.asyncio
async def test_empty_tables(client: AsyncClient):
    response = await client.get('/v1/tables/')
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_one_table(client: AsyncClient, test_table_one: Table):
    response = await client.get('/v1/tables/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


@pytest.mark.asyncio
async def test_create_table(client: AsyncClient):
    input_data = {
        'name': 'TableCreate',
        'seats': 1,
        'location': 'Hall'
        }
    response = await client.post('/v1/tables/', json=input_data)
    assert response.status_code == 201
    created_table = response.json()
    assert created_table['name'] == input_data['name']
    assert created_table['seats'] == input_data['seats']
    assert created_table['location'] == input_data['location']


@pytest.mark.asyncio
async def test_delete_table(client: AsyncClient, test_table_one: Table):
    response = await client.delete(f'/v1/tables/{test_table_one.id}')
    assert response.status_code == 204
    assert not response.content

from datetime import datetime, timedelta

import pytest
from httpx import AsyncClient

from schemas.reservation import Reservation
from schemas.table import Table


@pytest.mark.asyncio
async def test_empty_reservation(client: AsyncClient):
    response = await client.get('/v1/reservations/')
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_reservation(client: AsyncClient, test_reservation: Reservation):
    response = await client.get('/v1/reservations/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


@pytest.mark.asyncio
async def test_create_reservation(client: AsyncClient, test_table_one: Table):
    input_data = {
        'customer_name': 'Dwayne Johnson',
        'reservation_time': (
            datetime.now() + timedelta(minutes=2)
        ).isoformat(),
        'duration_minutes': 30,
        'table_id': test_table_one.id
        }
    response = await client.post('/v1/reservations/', json=input_data)
    assert response.status_code == 201
    created_reservation = response.json()
    assert created_reservation[
        'customer_name'] == input_data['customer_name']
    assert created_reservation[
        'reservation_time'] == input_data['reservation_time']
    assert created_reservation[
        'duration_minutes'] == input_data['duration_minutes']
    assert created_reservation[
        'table_id'] == input_data['table_id']


@pytest.mark.asyncio
async def test_create_reservation_with_invalid_table(
        client: AsyncClient,
        test_table_one: Table
):
    input_data = {
        'customer_name': 'Dwayne Johnson',
        'reservation_time': (
            datetime.now() + timedelta(minutes=2)
        ).isoformat(),
        'duration_minutes': 30,
        'table_id': 10
        }
    response = await client.post('/v1/reservations/', json=input_data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_crossed_reservation(
        client: AsyncClient,
        test_table_one: Table,
        test_reservation: Reservation
):
    input_data = {
        'customer_name': 'Dwayne Johnson',
        'reservation_time': (
            datetime.now() + timedelta(minutes=2)
        ).isoformat(),
        'duration_minutes': 30,
        'table_id': test_table_one.id
        }
    response = await client.post('/v1/reservations/', json=input_data)
    assert response.status_code == 400
    data = response.json()
    assert data['detail'][0].startswith('Cтолик занят')


@pytest.mark.asyncio
async def test_delete_reservation(
        client: AsyncClient,
        test_reservation: Reservation
):
    response = await client.delete(f'/v1/reservations/{test_reservation.id}')
    assert response.status_code == 204
    assert not response.content

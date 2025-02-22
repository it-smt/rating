from django.http import HttpRequest
from ninja import Router

from main.api.v1.schemas import SDriverShow, SMsg
from main.services.people_service import PeopleService

router = Router()


@router.get("drivers/", response={200: list[SDriverShow], 400: SMsg})
def get_drivers(request: HttpRequest, rank_name: str = "Бронза") -> list[SDriverShow]:
    """Получение всех водителей."""
    return PeopleService.get_by_rank(rank_name)

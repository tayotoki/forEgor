def vacancy_view(vacancy: dict):
    if (requirement := vacancy.get("snippet")).__class__ is dict:
        requirement = f"{requirement.get('requirement')}\n" \
                      f"{requirement.get('responsibility')}"

    return (f"Название: {vacancy.get('name')}\n"
            f"Ссылка: {vacancy.get('url')}\n"
            f"Описание: {requirement}\n"
            f"Зарплата: {vacancy.get('salary')}")
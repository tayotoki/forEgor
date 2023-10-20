import json

from .manager_abc import FileManager


class JSONManager(FileManager):
    FILE_NAME = "./vacancies.json"

    def add_vacancy(self, vacancy: dict):
        try:
            with open(self.FILE_NAME) as file:
                try:
                    vacancies = json.load(file)
                except json.decoder.JSONDecodeError:
                    vacancies = []
                vacancies.append(vacancy)

            with open(self.FILE_NAME, "w") as file:
                json.dump(vacancies, file, indent=2, ensure_ascii=False)

        except FileNotFoundError:
            with open(self.FILE_NAME, "w") as file:
                vacancies = [vacancy, ]
                json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def delete_vacancy(self, index: int) -> int | None:
        with open(self.FILE_NAME) as file:
            vacancies = json.load(file)

            try:
                vacancies[index]
            except IndexError:
                return -1
            else:
                del vacancies[index]

    def get_best_vacancy(self):
        with open(self.FILE_NAME) as file:
            vacancies = [
                vacancy for vacancy in json.load(file)
                if vacancy.get("salary", 0) is not None
            ]

            best_vacancy = max(
                vacancies,
                key=lambda vacancy: vacancy.get("salary")
            )

            return best_vacancy

    def clear(self):
        with open(self.FILE_NAME, "w"):
            pass

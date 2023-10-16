from classes.api_classes import HH, SJ
import json


def main():

    while True:
        keyword = input('Введите название должности / профессии: ')
        hh_vacancy = HH(keyword)
        sj_vacancy = SJ(keyword)
        dict_for_job = {'HH': hh_vacancy.get_vacancies(), 'SJ': sj_vacancy.get_vacancies()}

        with open('job.json', 'w', encoding='utf-8') as file:
            json.dump(dict_for_job, file, ensure_ascii=False, indent=2)

        for data in dict_for_job.items():
            for item in data:
                print(f"Должность - {item['name']}\nЗ/п - {item['salary']}\nОписание - {item['snippet']}\nСсылка - {item['url']}\n")


if __name__ == '__main__':
    main()

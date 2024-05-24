import os
from datetime import datetime


def make_commits(days: int):
    for day in range(days, 0, -1):
        dates = f'{day} days ago'
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(f'{dates}\n')

        os.system('git add data.txt')

        os.system('git commit --date="' + dates + '" -m "First commit"')

    os.system('git push')


start_date = datetime(2020, 9, 1)
end_date = datetime(2024, 5, 24)
delta = end_date - start_date

make_commits(delta.days)

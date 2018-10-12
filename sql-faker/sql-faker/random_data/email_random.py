# coding=utf-8
from random_abstract import RandomData
import random


class EmailRandom(RandomData):
    """邮箱生成器"""

    def create(self):
        prefix = random.choice(english_names) + str(random.randrange(11, 999999))
        suffix = random.choice(email_suffix)
        # 邮箱前缀 + 后缀
        return '%s@%s.com' % (prefix, suffix)


# 英文名
english_names = (
    "Jacob", "Michael", "Ethan", "Joshua", "Alexander", "Anthony", "William", "Christopher",
    "Jayden", "Andrew", "Joseph", "David", "Noad", "Aiden", "James", "Ryan", "Logan", "John",
    "Nathan", "Elijah", "Christian", "Gabriel", "Benjamin", "Jonathan", "Tyler", "Samuel",
    "Nicholas", "Gavin", "Dylan", "Jackson", "Brandon", "Caleb", "Jackson", "Brandon", "Caleb",
    "Mason", "Angel", "Isaac", "Evan", "Jack", "Kevin", "Jose", "Isaiah", "Luke", "Landon",
    "Justin", "Lucas", "Zachary", "Jordan", "Robert", "Aaron", "Brayden", "Thomas", "Cameron",
    "Hunter", "Austin", "Adrian", "Connor", "Owen", "Aidan", "Jason", "Julian", "Wyatt", "Charles",
    "Luis", "Carter", "Juan", "Chase", "Diego", "Jeremiah", "Brody", "Zavier", "Adam", "Carlos",
    "Liam", "Hayden", "Jesus", "Ian", "Tristan", "Bryan", "Sean", "Cole", "Alex", "Eric", "Brian",
    "Jaden", "Carson", "Blake", "Ayden", "Coope", "Dominic", "Brady", "Caden", "Josiah", "Kyle",
    "Colton", "Kaden", "Eli"
)

# 邮箱后缀
email_suffix = (
    "126", "163", "gmail", "qq", "188", "hotmail", "yahoo", "sina",
    "sohu", "msn", "live", "tom", "sogou"
)

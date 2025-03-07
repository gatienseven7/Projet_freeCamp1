import pandas as pd

def demographic_analysis():
    # Charger les données
    df = pd.read_csv("adult.data", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ])

    # 1. Nombre de personnes par race
    race_counts = df["race"].value_counts()

    # 2. Âge moyen des hommes
    avg_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Pourcentage de personnes avec un Baccalauréat
    bachelors_percentage = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Pourcentage de personnes ayant un diplôme avancé (Bachelors, Masters, Doctorate) et gagnant >50K
    higher_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_edu_rich = round((df[higher_edu & (df["salary"] == ">50K")].shape[0] / higher_edu.sum()) * 100, 1)

    # 5. Pourcentage de personnes sans éducation avancée gagnant >50K
    lower_edu = ~higher_edu
    lower_edu_rich = round((df[lower_edu & (df["salary"] == ">50K")].shape[0] / lower_edu.sum()) * 100, 1)

    # 6. Nombre minimum d'heures travaillées par semaine
    min_hours = df["hours-per-week"].min()

    # 7. Pourcentage de ceux qui travaillent le minimum d'heures et gagnent >50K
    min_hours_workers = df[df["hours-per-week"] == min_hours]
    min_hours_rich = round((min_hours_workers[min_hours_workers["salary"] == ">50K"].shape[0] / min_hours_workers.shape[0]) * 100, 1)

    # 8. Pays avec le pourcentage le plus élevé de personnes gagnant >50K
    country_salary = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_total = df["native-country"].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)

    # 9. Profession la plus populaire en Inde pour ceux gagnant >50K
    india_top_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    return {
        "race_counts": race_counts,
        "avg_age_men": avg_age_men,
        "bachelors_percentage": bachelors_percentage,
        "higher_edu_rich": higher_edu_rich,
        "lower_edu_rich": lower_edu_rich,
        "min_hours": min_hours,
        "min_hours_rich": min_hours_rich,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "india_top_occupation": india_top_occupation
    }

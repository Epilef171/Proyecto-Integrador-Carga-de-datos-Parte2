import pandas as pd

Dataset = [
    {"name": "Persona1", "age": 25, "is_dead": 0},
    {"name": "Persona2", "age": 30, "is_dead": 1},
    {"name": "Persona3", "age": 22, "is_dead": 0},
    # ... más datos
]

df = pd.DataFrame(Dataset)

df_alive = df[df['is_dead'] == 0]
df_dead = df[df['is_dead'] == 1]

average_age_alive = df_alive['age'].mean()
average_age_dead = df_dead['age'].mean()

print(f"Promedio de edades de personas vivas: {average_age_alive}")
print(f"Promedio de edades de personas fallecidas: {average_age_dead}")

import pandas as pd
import autopep8


def formatted_file(file: str) -> pd.DataFrame:
    """Форматирование файла
    Возвращает фрейм данных с добавлением столбцов"""
    df = pd.read_csv(file)

    df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
    df["Date1"] = df["Date"].dt.date
    df["Year"] = df["Date"].dt.year
    df["Week"] = df["Date"].dt.isocalendar().week
    return df


def clear_file(df: pd.DataFrame) -> pd.DataFrame:
    "Очистка файла возвращает базу данных без добавленного столбца"
    del df["Year"]
    del df["Week"]
    del df["Date1"]
    return df


def range_of_years(file: str) -> list:
    """Диапазон годов в наборе данных
    input_file - файл с набором данных
    возвращает список с первым и последним годом в наборе данных"""
    df = formatted_file(file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def max_week(df: pd.DataFrame) -> int:
    """Возвращает Максимальное количество недель за один год"""
    start_range = df[df["Week"] == df["Week"].max()]
    value = start_range["Week"].values[0]
    return value


def min_week(df: pd.DataFrame) -> int:
    """Возвращает Максимальное  количество недель за один год"""
    end_range = df[df["Week"] == df["Week"].min()]
    value = end_range["Week"].values[0]
    return value


def write_to_file(file: str) -> None:
    """input_file - файл с набором данных
    возвращает ничего"""
    df = formatted_file(file)
    range_of_years_list = range_of_years(file)

    for years in range(range_of_years_list[0], range_of_years_list[1] - 1, -1):
        lf = df[df["Year"] == years]

        for weeks in range(
                max_week(lf), min_week(lf) - 1, -1):
            try:
                sf = lf[lf["Week"] == weeks]
                if sf.empty:
                    break
                elif sf.shape[0] == 1:
                    data = str(sf["Date1"].iloc[0]).replace("-", "") + "_" + str(sf["Date1"].iloc[0]).replace("-", "")
                else:
                    data = str(sf["Date1"].iloc[0]).replace("-", "") + "_" + str(sf["Date1"].iloc[-1]).replace("-", "")
                clear_file(sf)

                sf.to_csv(data + ".csv", index=False)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    file = "C:/Users/User/Desktop/dataset.csv"
    write_to_file(file)





import pandas as pd


def write_to_file(input_file: str, file_for_x: str, file_for_y: str) -> None:
    """Запуск файла с набором данных
    file_for_x файл для  первого стобца
    file_for_y файл для второго столбца
    """
    df = pd.read_csv(input_file)
    df["Day"].to_csv(file_for_x, index=False)
    df["Exchange rate"].to_csv(file_for_y, index=False)


if __name__ == "__main__":
    file_dates = "X.csv"
    file_course = "Y.csv"
    file = "C:/Users/user/Desktop/dataset.csv"

    write_to_file(file, file_dates, file_course)


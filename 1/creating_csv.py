
import pandas as pd


def write_to_file(file: str, X_csv: str, Y_csv: str) -> None:
    """Запуск файла с набором данных
    file_for_x файл для  первого стобца
    file_for_y файл для второго столбца
    """
    df = pd.read_csv(file)
    df["Date"].to_csv(X_csv, index=False)
    df["Course"].to_csv(Y_csv, index=False)


if __name__ == "__main__":
    file_dates = "X.csv"
    file_course = "Y.csv"
    file = "C:/Users/user/Desktop/dataset.csv"

    write_to_file(file, file_dates, file_course)


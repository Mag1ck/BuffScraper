import os
import czytanie
import czyszczeniecen
import filtrowanie


def collect_data():
    filtrowanie.collect()


def process_data():
    czytanie.process_item()


def clear_duplicates():
    czyszczeniecen.clear()


def main():
    collect_data()
    process_data()
    clear_duplicates()


if __name__ == "__main__":
    main()

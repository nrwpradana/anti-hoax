import pandas as pd
import pathlib

DATA_DIR = pathlib.Path.cwd().joinpath("src", "data")


def get_literasi():
    literasi = pd.read_excel(
        DATA_DIR.joinpath("indeks-literasi-digital-indonesia.xlsx")
    )
    return literasi


def get_kominfo():
    kominfo = pd.read_csv(
        DATA_DIR.joinpath("data_hoax_2020_2021_kominfo.csv"), parse_dates=["date"]
    )
    return kominfo


def get_combine():
    combine = pd.read_csv(DATA_DIR.joinpath("combine.csv"))
    return combine


def get_penyebaran_hoaks20():
    data = {
        "media": [
            "facebook",
            "whatsapp",
            "youtube",
            "tv",
            "portal berita online",
            "instagram",
            "twitter",
            "radio",
            "koran/majalah",
            "line",
            "tidak ada/tidak tahu",
        ],
        "persentase": [71.9, 31.5, 14.9, 7.7, 10.7, 8.1, 1.9, 0.5, 2.5, 0.4, 2.9],
        "tahun": [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020],
    }
    df = pd.DataFrame(data)
    return df


def get_penyebaran_hoaks21():
    data = {
        "media": [
            "facebook",
            "whatsapp",
            "youtube",
            "tv",
            "portal berita online",
            "instagram",
            "twitter",
            "radio",
            "koran/majalah",
            "line",
            "tidak ada/tidak tahu",
        ],
        "persentase": [62.6, 20.5, 16.4, 16.3, 14.9, 9.7, 2.7, 1.5, 1.3, 0.7, 1.1],
        "tahun": [2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
    }
    df = pd.DataFrame(data)
    return df


def get_isi_hoaks20():
    data = {
        "topik": [
            "politik",
            "kesehatan",
            "agama",
            "lingkungan",
            "kerusuhan",
            "bencana alam",
            "tidak tahu",
            "lainnya",
        ],
        "persentase": [67.2, 46.3, 33.2, 21.9, 28.1, 12.4, 2.3, 1.4],
        "tahun": [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020],
    }
    df = pd.DataFrame(data)
    return df


def get_isi_hoaks21():
    data = {
        "topik": [
            "politik",
            "kesehatan",
            "agama",
            "lingkungan",
            "kerusuhan",
            "bencana alam",
            "tidak tahu",
            "lainnya",
        ],
        "persentase": [69.3, 39.7, 29.2, 21.4, 13.4, 10.9, 0, 0],
        "tahun": [2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
    }
    df = pd.DataFrame(data)
    return df


def get_literasi_prov20():
    df = pd.read_excel(
        DATA_DIR.joinpath("literasi_prov_2020.xlsx"), sheet_name="Sheet2"
    )
    return df


def get_literasi_prov21():
    df = pd.read_excel(DATA_DIR.joinpath("literasi_prov_2021.xlsx"))
    return df

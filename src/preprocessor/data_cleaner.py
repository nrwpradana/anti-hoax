import dateparser
import pandas as pd

from src.preprocessor import data_loader

# preprocessing literasi data
def literasi_only():
    literasi = data_loader.get_literasi()

    literasi_only = pd.DataFrame(literasi.iloc[0, [2, 0, 1]]).reset_index()

    # Fix path
    new_header = literasi_only.iloc[0]  # grab the first row for the header
    literasi_only = literasi_only[1:]  # take the data less the header row
    literasi_only.columns = new_header  # set the header row as the df header

    literasi_only.rename(
        columns={
            "nama_alias": "tahun",
            "Indeks Literasi Digital": "indeks_literasi_digital",
        },
        inplace=True,
    )

    literasi_only["indeks_literasi_digital"] = pd.to_numeric(
        literasi_only["indeks_literasi_digital"]
    )
    return literasi_only


# preprocessing hoax data
def kominfo_tahunan():
    kominfo = data_loader.get_kominfo()
    kominfo["bulan"] = kominfo.date.dt.month_name()
    kominfo_tahunan = (
        kominfo.groupby(["bulan", "tahun"])["judul"]
        .count()
        .reset_index()
        .rename(columns={"judul": "total"})
    )
    ordered_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    kominfo_tahunan["to_sort"] = kominfo_tahunan["bulan"].apply(
        lambda x: ordered_months.index(x)
    )
    kominfo_tahunan["tahun"] = kominfo_tahunan["tahun"].apply(str)
    kominfo_tahunan = kominfo_tahunan.sort_values("to_sort")
    return kominfo_tahunan


# preprocessing data for correlation
def get_corr_data(df1, df2):
    df1["indeks_literasi_digital"] = pd.to_numeric(df1["indeks_literasi_digital"])
    df1["tahun"] = df1["tahun"].apply(int)

    data = (
        df2.groupby(["tahun"])["total"]
        .sum()
        .reset_index()
        .rename(columns={"total": "total_hoax"})
    )
    data["tahun"] = data["tahun"].apply(int)

    combine = pd.merge(df1, data, how="inner", on="tahun")
    return combine


def get_literasi_prov20_clean():
    df = data_loader.get_literasi_prov20()
    df.drop(columns=["Unnamed: 0"])
    df["tahun"] = 2020
    return df


def get_literasi_prov21_clean():
    df = data_loader.get_literasi_prov21()
    df.drop(columns=["Unnamed: 0"])
    df["tahun"] = 2021
    return df


def get_penyebaran_hoaks():
    df1 = data_loader.get_penyebaran_hoaks20()
    df2 = data_loader.get_penyebaran_hoaks21()
    df = pd.concat([df1, df2])
    return df


def get_isi_hoaks():
    df1 = data_loader.get_isi_hoaks20()
    df2 = data_loader.get_isi_hoaks21()
    df = pd.concat([df1, df2])
    return df

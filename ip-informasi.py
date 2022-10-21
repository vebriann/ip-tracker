import os,sys,time,requests,json

# created Vebriann

def menu():
    print(" 1. Cek Informasi IP Sendiri")
    print(" 2. Cek Informasi IP Orang")
    print(" 3. Exit Program")
    pilih = input(" pilih: ")
    if pilih in ["1","01"]:
        try:
            cekip = requests.get("https://api.ipify.org/?format=json").json()
            return GetDataApi(cekip["ip"])
        except requests.exceptions.ConnectionError:
            print(" Terjadi Masalah Pada Jaringan!")
            exit()
    elif pilih in ["2","02"]:
        print("\n Masukan IP Target")
        print(" Example: 39.70.62.655")
        cekip = input(" IP: ")
        return GetDataApi(cekip["ip"])
    elif pilih in ["3","03"]:
        print(" Berhasil Keluar Program")
        exit()
    else:
        print(" Maaf Pilihan Anda Tidak Ada")
        exit()

def GetDataApi(api):
    try:
        response = requests.get(f"https://ipinfo.io/{api}/geo").json()
    except requests.exceptions.ConnectionError:
        print(" Terjadi Masalah Pada Jaringan!")
        exit()
    try:
        city = response["city"]
    except KeyError:
        city = "-"
    try:
        reg = response["region"]
    except KeyError:
        reg = "-"
    try:
        con = response["country"]
    except KeyError:
        con = "-"
    try:
        loc = response["loc"]
    except KeyError:
        loc = "-"
    try:
        org = response["org"]
    except KeyError:
        org = "-"
    try:
        timer = response["timezone"]
    except KeyError:
        timer = "-"
    print('\n INFORMASI IP KAMU\n')
    print(f' IP        : {str(api)}')
    print(f' CITY      : {str(city)}')
    print(f' REGION    : {str(reg)}')
    print(f' COUNTRY   : {str(con)}')
    print(f' LOCATION  : {str(loc)}')
    print(f' ORG       : {str(org)}')
    print(f' TIMEZONE  : {str(timer)}\n')


if __name__=="__main__":
    menu()
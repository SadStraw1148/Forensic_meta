import pikepdf
import exifread
from colorama import Fore, Back, Style
from os import system



system("cls")


print(Fore.RED + """
 ####### ####### ######  ####### #     #  #####  ###  #####  
 #       #     # #     # #       ##    # #     #  #  #     # 
 #       #     # #     # #       # #   # #        #  #       
 #####   #     # ######  #####   #  #  #  #####   #  #       
 #       #     # #   #   #       #   # #       #  #  #       
 #       #     # #    #  #       #    ## #     #  #  #     # 
 #       ####### #     # ####### #     #  #####  ###  #####  
""")



target = input(Fore.GREEN + "Enter target : ")
print()
print()





def get_exif(target_file):
    with open(target_file, "rb") as file:
        exif = exifread.process_file(file)
        if not exif:
            print("aucun métadonnée EXIF.")
        else:
            for tag in exif.keys():
                print(tag + " " + str(exif[tag]))

def convert_to_degres(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def get_gps_from_exif(target_file):
    with open(target_file, "rb") as file:
        exif = exifread.process_file(file)
        if not exif:
            print("aucun métadonnée EXIF.")
        else:
            latitude = exif.get("GPS GPSLatitude")
            latitude_ref = exif.get("GPS GPSLatitudeRef")
            longitude = exif.get("GPS GPSLongitude")
            longitude_ref = exif.get("GPS GPSLongitudeRef")
            if latitude and longitude and latitude_ref and longitude_ref:
                lat = convert_to_degres(latitude)
                long = convert_to_degres(longitude)
                if str(latitude_ref) != "N":
                    lat = 0 - lat
                if str(longitude_ref) != "E":
                    long = 0 - long
                print("LAT : " + str(lat) + "LONG : " + str(long))
                print("https://maps.google.com/maps?q=loc:%s,%s" % (str(lat), str(long)))


def change_target():
    target = input("Enter target : ")


def main():
    print()
    print()
    choice = input("""Choose a option with his number :
1-  Look exif metadata of pictures
2-  Look gps coordonates with exif metadata
3-  Look pdf metadata
4- Change target
>""")
    if choice == "1":
        get_exif(target)
    elif choice == "2":
        get_gps_from_exif(target)
    elif choice == "3":
        pdf = pikepdf.Pdf.open(target)
        pdf_metadata = pdf.docinfo    
        for key, value in pdf_metadata.items():
            print(f'{key} : {value}')
    elif choice == "4":
        change_target()

while True:
    main()
    
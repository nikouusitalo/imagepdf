import os

#from fpdf import FPDF
import datetime
phone_dir = os.path.expanduser("~/tehtävät/")
home_dir = os.path.expanduser("~")
filesdate = []



#IMG_20240906_103722.jpg

#pdf = FPDF()
#pdf.add_page()
#pdf.image()
def look_images():
    for image_name in os.listdir(phone_dir):
        if image_name.endswith(".jpg"):
            date_str = image_name[4:12]  # Get the date part 'YYYYMMDD'
            image_date = datetime.datetime.strptime(date_str, '%Y%m%d').date()  # Convert to date object
            current_date = datetime.date.today()
          pdef makepdf():
    return
def main():
    look_images()
if __name__ == "__main__":
 main()

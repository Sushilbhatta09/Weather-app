import tkinter as tk
import requests
from PIL import ImageTk,Image
import json
from io import BytesIO
import datetime

APPID = 'f2933de9acefed011e09f80447c343fd'


def write(data):
    with open('data.json','w') as file:
        json.dump(data,file)

def getweather(window):
    city = textfield.get()
    api_response_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + APPID
    response = requests.get(api_response_url)
    response_data = response.json()
    write(response_data)



    #take data from response
try :
    condition = response_data['weather'][0]['main']

    
     #changing background image, reading the image
    bg_image_data=Image.open('./Images/'+condition+'.jpg')
    resized_image_data = bg_image_data.resize((800,800),Image.ANTIALIAS)
    bg_image=ImageTk.PhotoImage(resized_image_data)


    temp = int(response_data['main']['temp']-273)
    temp_min = int(response_data['main']['temp_min']-273)
    temp_max = int(response_data['main']['temp_max']-273)
    pressure = response_data['main']['pressure']
    humidity = response_data['main']['humidity']
    wind = response_data['wind']['speed']
    sunrise = response_data['sys']['sunrise']
    sunrise1 = datetime.datetime.fromtimestamp(sunrise)
    sunset = response_data['sys']['sunset']
    sunset1 = datetime.datetime.fromtimestamp(sunset)

    #merge all information in single variable

    final_data = f"{condition} \n {temp} °C"
    final_info = f"Min_temp:{temp_min}°C \n Max_Temp:{temp_max}°C \n Pressure:{pressure} \n Humidity:{humidity} \n Windspeed:{wind} \n Sunrise:{sunrise1} \n Sunset:{sunset1}"
    label1.config(text=final_data)
    label2.config(text=final_info)
    label3.configure(image=bg_image) 
    #configure for image
    label3.image=(bg_image)
    label3.image=(bg_image)
   #  icons_label.configure(image=icon_image)
   # icons_label.image=(icon_image)
    #country_label.configure(image=country_image)
   # country_label.image=(country_image)
except KeyError:
    label1.config(text=response_data['message'])
    label2.config(text=response_data['cod'])

window = tk.Tk()
window.title("Weather App")
window.geometry("800x800")
bg_image_data = Image.open("./Images/bg.jpg")
resized_image_data = bg_image_data.resize((800,800),Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(resized_image_data)
label3 = tk.Label(window,image=bg_image)
label3.place(x=0,y=0)

textfield = tk.Entry(window,bg='#fafafa',justify='center',font=('poppins',35,'bold'),width='20')

textfield.pack(pady='20')
button = tk.Button(window,text='Get weather',font=('poppins',15,'bold'))
button.pack()
button.bind('<Button>',getweather)
label1 = tk.Label(window ,bg='#afafaf',font=('poppins',20,'bold'))
label1.pack()
label2 = tk.Label(window ,bg='#afafaf',font=('poppins',20,'bold'))
label2.pack()


window.mainloop()
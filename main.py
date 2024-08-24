# from speech import recognize_speech, speak
# from nlp import process_text
# from api import get_weather

# def main():
#     while True:
#         print("Bir komut bekleniyor...")
#         command = recognize_speech()
        
#         if not command:
#             continue
        
#         doc = process_text(command)
        
#         if "hava durumu" in command:
#             city = "Istanbul"  # Sabit bir şehir kullanın veya kullanıcıdan şehir bilgisi alın
#             weather = get_weather(city)
#             if weather:
#                 description, temperature = weather
#                 response = f"{city} için hava durumu: {description}, sıcaklık: {temperature}°C"
#                 print(response)
#                 speak(response)
#             else:
#                 print("Hava durumu bilgisi alınamadı.")
#                 speak("Hava durumu bilgisi alınamadı.")
        
#         # Diğer komutlar için burada eklemeler yapabilirsiniz
        
#         if "çıkış" in command:
#             print("Görüşmek üzere!")
#             speak("Görüşmek üzere!")
#             break

# if __name__ == "__main__":
#     main()


from nlp import process_text
from api import get_weather

def main():
    while True:
        command = input("Bir komut bekleniyor: ")
        
        if not command:
            continue
        
        doc = process_text(command)
        
        if "hava durumu" in command:
            timezone = input("Hangi şehir için hava durumu öğrenmek istiyorsunuz?: ")
            if timezone:    
                weather = get_weather(timezone)
                if weather:
                    description, temperature = weather
                    response = f"{timezone} için hava durumu: {description}, sıcaklık: {temperature}°C"
                    print(response)
                else:
                    print("Hava durumu bilgisi alınamadı.")
            else:
                print("Şehir adı anlaşılamadı.")
        
        # Diğer komutlar için burada eklemeler yapabilirsiniz
        
        if "çıkış" in command:
            print("Görüşmek üzere!")
            break

if __name__ == "__main__":
    main()


Bu kodu daha da düzelt, verilerin neden alınmadığını çöz!!!

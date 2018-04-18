import RPi.GPIO as GPIO           # Kütüphane tanımlama işlemleri yapılır.
import dht11
import time
import datetime
from time import sleep
i=0                        #.txt dosyalarının içine sıralı bilgi yazmak için kullanılacak i ye sıfır atanır.


GPIO.setwarnings(False)         # Pinlere gerekli komutlar verilir.
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()


Motorileri = 16                # Motor için gerekli pin giriş değerleri verilir.
Motorgeri = 18                 # Motorileri motorun sağa, motorgeri motorun sola dönüşünü sağlar.
Motordur = 22                  # Motor dur ise motorun durdurulmasını sağlar.

GPIO.setup(15,GPIO.OUT)        # Led ler için (GPIO.setup) kullanılarak gerekli pin kurulumları yapılır.
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)



GPIO.setup(Motorileri,GPIO.OUT)     #Üste tanımlanan motor pin degerleri için kurulum yaoılır.
GPIO.setup(Motorgeri,GPIO.OUT)
GPIO.setup(Motordur,GPIO.OUT)

sensoroku = dht11.DHT11(pin=8)       #Sensör oku degiskenine "dht11.DHT11" ile sensörden alınan bilgi verilir.
                                     #bu verinin alımı için 8 nolu pin tanımlanır.

open("nem.txt", "w")                #grafik kodu için kullanılacak olan nem.txt dosyasının açılma işlemi yapılır.
open("sicaklik.txt", "w")           #grafik kodu için kullanılacak olan sıcaklık.txt dosyasının açılma işlemi yapılır.
with open("nem.txt", "a") as log:   #nem.txt dosyasını log komutu ile yazma için uygun hale getirilir.
 with open("sicaklik.txt", "a") as log1: #sıcaklık.txt dosyasını log1 komutu ile yazma için uygun hale getirilir.

     while True:                     #while true ile sonsuz bir döngü açılır.
       
       deger = sensoroku.read()      #sensor oku daki data deger degiskenine atanır
       
       

       if deger.is_valid():          #if döngüsü ile uygun şartlarda yapılacak olan işlemlar yazılır.
           
          print("Son veri okuma saati: " + str(datetime.datetime.now()))   
            
          print("Sicaklik degeri: %d C" % deger.temperature)   #sensörden alınan datanın yazılması sağlanır.
            
          print("Nem degeri: %d %%" % deger.humidity)
       
         
            
          if(deger.humidity>80):          #nemin %80 den buyuk olma durumunda ekrana bilgi yazdırılır.
                
             print("Nem kurutma devrede")
                
             GPIO.output(24, GPIO.HIGH)   #nemin %80 den buyuk olma durumunda 24 nolu pin high olur diğerleri low
             GPIO.output(12, GPIO.LOW)
             GPIO.output(13, GPIO.LOW)
                
          
          
          elif(deger.humidity<70):          #nemin %70 den kucuk olma durumunda ekrana bilgi yazdırılır.
                
             print("Nem artirma devreye girdi!")
             
             GPIO.output(12, GPIO.LOW)      #nemin %80 den buyuk olma durumunda 13 nolu led high olur. diğerleri 0
             GPIO.output(13, GPIO.HIGH)  
             GPIO.output(24, GPIO.LOW)
                
          
          else:                            #else ile kalan durumlar için ekrana verilen bilgi yazdırılır.
                
             print("Nem degeri sisteme uygun!")
                
             GPIO.output(12, GPIO.HIGH)    #led durumları pin çıkışları ile ayarlanır.
             GPIO.output(13, GPIO.LOW)  
             GPIO.output(24, GPIO.LOW)
                
           
         
            
            
          if(deger.temperature>25):               #sıcaklık için nem ile aynı sekilde şart durumları yapılır.
                
             print("Sogutma sistemi devreye girdi!") #ekrana bilgi yazdırılır
                
             GPIO.output(Motorileri,GPIO.HIGH)      #motorun sola dönmesi için motorgeriye low degeri verlir... 
             GPIO.output(Motorgeri,GPIO.LOW)        #...diğerleri ise hıgh olur
             GPIO.output(Motordur,GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)              #stabil durumu belirten led low degeri alır.
            
          elif(deger.temperature<24):               # elif ile deger kontrol edilir.
                
             print("Isitma sistemi devreye girdi!")  #bilgi ekrana yazdırılır.
                
             GPIO.output(Motorileri,GPIO.LOW)  #motor ve led için pin cıkışlarına high ve low degerleri verilir.
             GPIO.output(Motorgeri,GPIO.HIGH)
             GPIO.output(Motordur,GPIO.HIGH)
             GPIO.output(15, GPIO.LOW)
            
            
          else:
               
             print("Sicaklik degeri sisteme uygun!")  #else ile kalan durumlar için bilgi ekrana yazıdırılır.
               
             GPIO.output(Motordur,GPIO.LOW)       #else durumu için pin cıkısları duzenlenir
             GPIO.output(15, GPIO.HIGH)   #motor durdurulurken led degeri high yapılır. led stabil sıcaklıgı belirtir
             
       global i            #global komutu ile iki .txt uzantılıdosyanında içine aynı yerden gelen data yazılır!
       i=i+1               # işlemi ile .txt uzantılı dosyanının içine yazılacak grafik verisi düzenli hale getirilir.
       if(int(deger.humidity)!=0):  # gelen datanın sıfırdan farklı deger olması sağlanır(grafik kararsız hale geliyor.)
           log.write("{},{}\n".format(str(i),str(deger.humidity))) #logwrite ile ilk .txt ye yazma işlemi yapılır.
       if(int(deger.temperature)!=0): # gelen datanın sıfırdan farklı deger olması sağlanır(grafik kararsız hale geliyor.)
           log1.write("{},{}\n".format(str(i),str(deger.temperature))) #log1write ile ikinci .txt ye yazma işlemi yapılır.
       time.sleep(2)     #sonsuz döngü için 2 saniye bekle(daha kısa sürelerde grafik kararsız oluyor.)
       
       
       
       

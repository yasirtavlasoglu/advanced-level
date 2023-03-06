import cv2

cap = cv2.VideoCapture(0)

takip = cv2.legacy.TrackerMOSSE_create() #cv2.TrackerMOSSE_create() yerine bunu kullandım çalıştı
takip = cv2.TrackerCSRT_create()

success, line = cap.read()

test = cv2.selectROI("tech-2",line,True) #işaretleme penceresi

takip.init(line,test)

#takip yazısı için
def drawBox(line,test):
    x,y,w,h = int(test[0]), int(test[1]), int(test[2]), int(test[3])
    cv2.rectangle(line,(x,y),((x+w),(y+h)),(0,255,255),3,3)
    cv2.putText(line,"Takip Ediliyor!",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
    zamanlama = cv2.getTickCount() #zaman
    success, line = cap.read()

    success,test = takip.update(line)
    print(test)

    if success:
        drawBox(line,test)
    else:
        cv2.putText(line,"Hedef Kayip!",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    
    #fps hesaplama
    fps = cv2.getTickFrequency()/(cv2.getCPUTickCount()-zamanlama) #fps hesaplama formülü
    cv2.putText(line,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2) #değeri ekrana yazdırmak için
    
    #pencere ismi
    cv2.imshow("tech-1",line)

    #q harfi ile pencereyi kapatmak
    if cv2.waitKey(1) & 0xff ==ord("q"): 
        break


    """
@yasirtavlasoglu
    """
    
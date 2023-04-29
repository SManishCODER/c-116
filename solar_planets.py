import cv2

img = cv2.imread("solar system.png")



cv2.putText(img,  
            "Sun",
            (90, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )

cv2.putText(img,  
            "Mercury",
            (190, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )

cv2.putText(img,  
            "Venus",
            (220, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )

cv2.putText(img,  
            "Earth",
            (280, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )




cv2.putText(img,  
            "Mars",
            (290, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )








cv2.putText(img,  
            "Jupiter",
            (130, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )


cv2.putText(img,  
            "Saturn",
            (160, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )

cv2.putText(img,  
            "Uranus",
            (190, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )

cv2.putText(img,  
            "Neptune",
            (290, 300),  
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (252,252,252)
            )


cv2.imshow("output",img)



cv2.imwrite("Solar_systemwithname.jpg",img)


cv2.waitKey(0)
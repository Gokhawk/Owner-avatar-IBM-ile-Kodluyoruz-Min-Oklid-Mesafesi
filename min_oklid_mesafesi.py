import math

# q^2 + r^2 = p^2
# p = sqrt(q^2 + r^2)
# d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# Noktaların tanımlanması
points = [(3,4),(5,6),(5,12),(7,24)]

# Öklid Mesafesi Fonksiyonu  
def euclideanDistance(point_1,point_2):
    return math.sqrt((point_2[0] - point_1[0])^2 + (point_2[1] - point_1[1])^2) # math kütüphanesinin sqrt fonksiyonu ile karekökünü alıyoruz.

# Mesafeleri kaydedebilmek için bir liste tanımlıyoruz.
distances = [] 


for a in range(len(points)): # Burda points listesinin uzunluğunu alıp bu listenin son noktasını belirleyerek ilk noktadan son noktaya kadar sırayla ilerleyeceğiz.
    for b in range(a + 1, len(points)): # Burda ise points listesindeki ikinci noktayı seçiyoruz ve gene listenin son noktasına kadar ilerleyeceğiz.
        distance = euclideanDistance(points[a], points[b]) # Döngünün seçtiği noktalar burda fonksiyonda işleme giriyor.
        distances.append(distance) # Bulduğumuz mesafe sonucunu distances listesine ekliyoruz. 


print(f"Minimum Mesafe: {min(distances)}") # Burda distances listesine kaydettiğimiz mesafe bilgilerininden min() fonksiyonu yardımıyla en küçük mesafeyi seçip yazdırıyoruz.





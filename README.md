# Görüntü Sınıflandırma Uygulaması

Bu proje, bir kamera cihazından görüntü yakalayarak ve ResNet50 modelini kullanarak nesneleri sınıflandırmak için bir örnek sunar.

## Başlangıç

Bu talimatlar, projeyi yerel bir Python ortamında çalıştırmak için gereken adımları içerir.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- TensorFlow (`tensorflow`)
- ResNet50 modeli için TensorFlow'un `tensorflow.keras.applications` modülü

Ayrıca, sınıflandırma için kullanılan etiketlere ihtiyacınız var. Bu etiketleri almak için internet bağlantısına ihtiyacınız vardır.

### Kurulum

Aşağıdaki adımları takip ederek projeyi yerel bir Python ortamında kurabilirsiniz:

1. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install opencv-python numpy tensorflow

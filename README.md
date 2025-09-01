# 🤖 Face Detection for Raspberry Pi 5

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-c51a4a)
![Camera](https://img.shields.io/badge/Camera-Module%203-blue)
![Python](https://img.shields.io/badge/Python-3.9+-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8+-orange)

A face detection system optimized for Raspberry Pi 5 with Camera Module 3, offering two implementations: OpenCV (lightweight) and MediaPipe (accurate).

![Face Detection Demo]([[https://via.placeholder.com/800x400?text=Face+Detection+Demo](https://github.com/Armoumad/Facial-Detection-on-Raspberry-Pi-5-with-Camera-Module-3/blob/main/photo%20test](https://github.com/Armoumad/Facial-Detection-on-Raspberry-Pi-5-with-Camera-Module-3/blob/main/photo%20test)))

## 📋 Prerequisites

### Hardware
- Raspberry Pi 5
- Raspberry Pi Camera Module 3
- Display to show results (optional)

### Software
- Raspberry Pi OS (Bullseye or newer)
- Python 3.9+

## 🔧 Installation
1. Clone this repository on your Raspberry Pi:
```bash
https://github.com/Armoumad/Facial-Detection-on-Raspberry-Pi-5-with-Camera-Module-3.git
cd Facial-Detection-on-Raspberry-Pi-5-with-Camera-Module-3
```

2. Mettre à jour le système
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

3.  Installer les dépendances pour OpenCV 
```bash
sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg-dev libtiff5-dev libpng-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libfontconfig1-dev libcairo2-dev
sudo apt-get install -y libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt-get install -y libgtk2.0-dev libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y python3-dev python3-pip

```

4. Installer les bibliothèques Python
```bash
pip3 install numpy
pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install mediapipe
```
If there is any problem installing mediapipe, you can use this command instead:
```bash
pip3 install --break-system-packages mediapipe
```
```
pip3 install picamera2
```


## 🚀 Usage
```bash
python3 face_detection.py
```

To exit the application, press the `q` key when the display window is active.

## ✨ Features

- **Real-time detection** of faces from video stream
- **Tracking of the number of faces** detected
- **Display of detection confidence** (with MediaPipe)
- **Visual interface** with rectangle around detected faces
- **Optimization** for Raspberry Pi 5 performance

## 🔍 Comparison of Methods

| Method | Accuracy | Performance | Use Case |
|---------|-----------|-------------|-------------|
| OpenCV Haar Cascades | Medium | Excellent | Controlled environments, limited resources |
| MediaPipe | High | Good | Variable conditions, better accuracy needed |

## 🛠️ Troubleshooting

### Common Issues

- **Error "Camera not found"**: Check that the camera is properly connected and enabled in `raspi-config`
- **Slow performance**: Reduce image resolution in the code (e.g., 320x240)
- **Inaccurate detections**: Adjust parameters like `scaleFactor` and `minNeighbors` in OpenCV or `min_detection_confidence` in MediaPipe

## 🔄 Future Updates

- [ ] Addition of facial recognition (person identification)
- [ ] Support for video recording of detections
- [ ] Web interface for remote monitoring
- [ ] Power-saving mode for battery-powered applications

## 📊 Performance

Here are typical performances on a standard Raspberry Pi 5:

| Method | FPS | CPU Usage | RAM Usage |
|---------|-----|----------------|----------------|
| OpenCV | 15-20 | 25-40% | ~100 MB |
| MediaPipe | 10-15 | 40-60% | ~200 MB |

## 🤝 Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👏 Credits

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [Picamera2](https://github.com/raspberrypi/picamera2)
- [Raspberry Pi Foundation](https://www.raspberrypi.org/)

---

Developed by [Armoumad](https://github.com/Armoumad) - 2025

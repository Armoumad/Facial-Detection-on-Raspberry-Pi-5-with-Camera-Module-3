# 🤖 Face Detection for Raspberry Pi 5

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-5-c51a4a)
![Camera](https://img.shields.io/badge/Camera-Module%203-blue)
![Python](https://img.shields.io/badge/Python-3.9+-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8+-orange)

A face detection system optimized for Raspberry Pi 5 with Camera Module 3, offering two implementations: OpenCV (lightweight) and MediaPipe (accurate).

![Face Detection Demo](https://via.placeholder.com/800x400?text=Face+Detection+Demo)

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
git clone https://github.com/Armoumad/raspberry-face-detection.git
cd raspberry-face-detection
```

2. Make the installation script executable and run it:
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

3. Make the detection scripts executable:
```bash
chmod +x face_detection_opencv.py
chmod +x face_detection_mediapipe.py
```

## 🚀 Usage

### Face detection with OpenCV (lighter)
```bash
./face_detection_opencv.py
```

### Face detection with MediaPipe (more accurate)
```bash
./face_detection_mediapipe.py
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

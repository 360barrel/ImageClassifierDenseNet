# Image Classifier Web App

A beautiful, minimalistic web interface to classify images using a deep learning model. Upload an image of an object, and the app returns the most likely classification with confidence — powered by a Flask backend and Bootstrap frontend.

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Flask-blue.svg" />
  <img src="https://img.shields.io/badge/Frontend-Bootstrap-lightgrey" />
  <img src="https://img.shields.io/badge/Model-ImageNet%20(pretrained)-green" />
  <img src="https://img.shields.io/badge/License-MIT-blue" />
</p>

---

## ✨ Demo

Here’s a preview of how the web interface looks:

<p align="center">
  <img src="ImageCUI.png" alt="App UI" width="600" />
</p>

---

## 🐾 Example Predictions

| Image              | Predicted Label       | Class ID |
|--------------------|-----------------------|----------|
| ![Tiger](TigerCatPred.png) | `tiger_cat`           | `n02123159` |
| ![Persian Cat](persiancat.png) | `Persian_cat`        | `n02123394` |

> 🧠 These predictions are generated using a pretrained ImageNet model (e.g., ResNet).

---

## 🚀 How to Run Locally

### 🔧 Requirements

- Python 3.7+
- pip
- `torch`, `torchvision`, `flask`

### 🛠️ Installation

```bash
git clone https://github.com/GeraldWambui/ImageClassifierDenseNet.git
cd ImageClassifierDenseNet
pip install -r requirements.txt

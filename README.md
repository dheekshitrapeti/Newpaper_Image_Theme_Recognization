# 📰 News Article Theme Recognition through Article Images

## 📌 Project Overview
This project focuses on developing a **newspaper image theme recognition system** capable of accurately identifying and classifying newspaper article images according to their **visual content**.  
Using **deep learning (ResNet50)** and image processing, the system extracts features (shapes, colors, textures) from newspaper images and predicts the **theme/section** they belong to, such as:
- 🏟️ Sports  
- 🌦️ Weather  
- 🏢 Business  
- 🏛️ Politics  
- 🎬 Cinema  

---

## 🚀 Problem Statement
- Classify newspaper article images based on their **visual patterns and objects**.  
- Recognize **standard features** (stadiums, suits, logos, buildings, crowds, etc.) that define different sections.  
- Improve accuracy by preprocessing and augmenting dataset images.  

---

## 📂 Dataset
- Images were collected manually from:
  - Campus library newspapers  
  - News apps (e.g., Way2News)  
  - Online news websites  
- Preprocessing included resizing, normalization, and augmentation techniques:
  - ✅ Random rotations  
  - ✅ Horizontal flips  

---

## ⚙️ Methodology
1. **Data Preprocessing**  
   - Resize images  
   - Normalize pixel values  
   - Apply transformations  

2. **Feature Extraction**  
   - Shapes (lines, curves)  
   - Colors (RGB combinations)  
   - Textures  

3. **Model Training**  
   - Used **ResNet50** for feature extraction and classification  
   - Trained on labeled images with data augmentation  

4. **Prediction**  
   - Compares extracted features with **standard features** for each news section  
   - Outputs probability scores for each category  

---

## 📊 Results
- **Model Accuracy (ResNet50):** **78.28%**  
- High accuracy in:
  - 🏟️ **Sports news** (stadiums, players, jerseys, equipment)  
  - 🌦️ **Weather news** (consistent visual patterns)  
- Lower accuracy in:
  - 🏛️ **Politics** (few common patterns across images)  
  - 🎬 **Cinema** (diverse visual content)  

---

## 🛠️ Challenges & Solutions
- **Challenge:** Lack of standard visual patterns in Indian politics section → **Low accuracy**  
- **Solution:** Applied **thresholding** (50%) for prediction confidence.  

- **Challenge:** Overlapping features across categories.  
- **Solution:** Used deeper feature extraction (ResNet50 layers).  

---

## 📌 Future Work
- Expand dataset with more labeled images per section.  
- Fine-tune ResNet50 with **transfer learning** on a larger dataset.  
- Explore **transformer-based vision models (ViT, CLIP)** for better generalization.  
- Add **multiclass classification support** with improved accuracy across all sections.  

---

## 🧑‍💻 Team
- **L. Sri Tanishq** (S200018)  
- **K. Naga Chakradar** (S200032)  
- **R. Dheekshit** (S200134)  

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use and modify with attribution.  

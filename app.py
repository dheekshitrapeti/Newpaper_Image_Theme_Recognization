import streamlit as st
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Streamlit UI
st.title("Newspaper Image Categorization")
st.write("Upload an image to classify it.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
class_names=['Business', 'Political', 'Sports', 'film', 'weather']
if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Define transformations (match training preprocessing)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # Resize to match model input size
        transforms.ToTensor(),  # Convert image to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalization
    ])

    # Preprocess the image
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Define and Load Model
    num_classes = 5  # Set correct number of classes
    model = models.resnet50()
    model.fc = torch.nn.Linear(in_features=2048, out_features=num_classes)

    # Load the state dictionary
    checkpoint = torch.load("/Users/dheekshitrapeti/Downloads/Newspaper_image_categorization/newspaper_cnn.pth", map_location=torch.device("cpu"))
    new_state_dict = {k.replace("model.", ""): v for k, v in checkpoint.items()}
    model.load_state_dict(new_state_dict, strict=False)
    
    model.eval()  # Set to evaluation mode

    # Perform inference
    with torch.no_grad():
        output = model(image_tensor)
        predicted_class = torch.argmax(output, dim=1).item()  # Get predicted class index

    # Display result
    st.write(f"### Predicted Category: **{class_names[predicted_class]}**")  

# Chicken-Disease-Classification

## Overview
This project aims to analyze chicken fecal images to identify if the chicken has coccidiosis or not. Coccidiosis is a common parasitic disease affecting chickens, and early detection is crucial for effective treatment.

## Dataset
The dataset used for this project was obtained from Kaggle and stored in an S3 bucket. It consists of a collection of chicken fecal images labeled with coccidiosis status in separate folders.

## Model Architecture
For the classification task, Transfer Learning was employed using EfficientNetB3 as the base architecture. The pre-trained EfficientNetB3 model was fine-tuned on the chicken fecal image dataset to leverage its feature extraction capabilities.

## Model Performance
The trained model achieved an impressive accuracy of 99% on the validation dataset. The results can be verified from scores.json

## Deployment
The project is deployed on the Azure Cloud platform, providing easy accessibility and scalability. The container is pulled from Azure Container Registery and the website is deployed using the Azure Web App.

## Tools and Technologies Used
### Data Version Control (DVC)
DVC was used for efficient data versioning and management.
### Continuous Integration/Continuous Deployment (CI/CD)
GitHub Actions were used to set up a CI/CD pipeline for the project. The project has four pipelines: 
- data_ingestion
- prepare_base_model
- training
- evaluation

##License
This project is licensed under the MIT License - see the LICENSE file for details.


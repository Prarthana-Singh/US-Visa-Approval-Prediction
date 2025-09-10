
---

# 🛂 US Visa Prediction (MLOps Project)

This project builds an end-to-end **Machine Learning Pipeline** for predicting US Visa approvals.
It covers everything from **data ingestion → preprocessing → model training → evaluation → deployment** using **MongoDB Atlas, AWS (S3, EC2, ECR), CI/CD with GitHub Actions, and Docker**.

---
### 🎥 Demo
![Demo](https://github.com/user-attachments/assets/129105a8-a8a8-429a-8628-7576825c3b93)

---

### 🖼 Demo Screenshots

| Screenshot 1 | Screenshot 2 | Screenshot 3 |
|--------------|--------------|--------------|
| ![Screenshot 1](https://github.com/user-attachments/assets/083ae8b5-edc9-4789-892d-1c568901dc6b) | ![Screenshot 2](https://github.com/user-attachments/assets/395568bd-bde5-4cf0-839b-182e1ff1d451) | ![Screenshot 3](https://github.com/user-attachments/assets/9fc4fe1b-ac92-40f8-9b05-4a118ea70697) |

---

## 🚀 Project Workflow

1. **Project Setup**

   * Run `template.py` to generate the project structure.
   * Setup `setup.py` to import local packages.
   * Create and activate virtual environment:

     ```bash
     conda create -n visa python=3.8 -y
     conda activate visa
     pip install -r requirements.txt
     ```
   * Verify packages:

     ```bash
     pip list
     ```

2. **MongoDB Setup**

   * Create a free **MongoDB Atlas** cluster (M0).
   * Create user credentials and whitelist IP (`0.0.0.0/0`).
   * Get connection string → replace `<username>` & `<password>`.
   * Push dataset ([Kaggle EasyVisa Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)) to MongoDB using `notebook/mongoDB_demo.ipynb`.
   * Verify data in MongoDB collections.

3. **Core Components**

   * **Logger & Exception Handling** (`logger.py`, `exception.py`)
   * **EDA & Feature Engineering** (`EDA.ipynb`, `Feature_Engg.ipynb`)
   * **Data Ingestion**
   * **Data Validation** (`config.schema.yaml`)
   * **Data Transformation**
   * **Model Training**
   * **Model Evaluation & Pusher** (with AWS S3 storage)
   * **Prediction Pipeline** (`app.py`)

4. **AWS Setup**

   * Create IAM user (`usvisaproject`) with **AdministratorAccess**.
   * Setup AWS CLI credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
   * Create S3 bucket: `usvisa-model-mlopsproj`.
   * Configure model registry in constants.
   * Add `cloud_storage` and `s3_estimator.py` for AWS interactions.

5. **CI/CD Pipeline**

   * **Dockerize the project** (`Dockerfile`, `.dockerignore`).
   * Setup **GitHub Actions** workflow (`.github/workflows/aws.yaml`).
   * Create IAM user (`usvisa-user`) for deployment automation.
   * Create private ECR repo: `usvisa`.
   * Launch EC2 instance (Ubuntu 20.04, T2.large, 30GB storage).
   * Install Docker & connect EC2 as a **self-hosted GitHub runner**.
   * Setup GitHub secrets for AWS & ECR.
   * Expose app on **port 8080**.

6. **Deployment**

   * Application runs on:

     ```
     http://<EC2-PUBLIC-IP>:8080
     ```
   * Training endpoint:

     ```
     http://<EC2-PUBLIC-IP>:8080/training
     ```

---

## 📂 Project Structure

```
usvisa/
│── constants/
│── entity/
│── components/
│── data_access/
│── cloud_storage/
│── pipeline/
│── static/
│── template/
│── notebook/
│── app.py
│── demo.py
│── setup.py
│── requirements.txt
│── Dockerfile
│── .github/workflows/aws.yaml
```

---

## ⚙️ Tech Stack

* **Languages:** Python 3.8
* **Database:** MongoDB Atlas
* **Cloud:** AWS (S3, EC2, ECR, IAM)
* **ML Frameworks:** scikit-learn, pandas, numpy
* **Deployment:** Docker, GitHub Actions (CI/CD)

---

## 📊 Model Performance

* **Best Model:** K-Nearest Neighbor (KNN)
* **Accuracy:** **96.66%** ✅

---

## 🔑 Environment Variables

Set the following environment variables:

```bash
MONGODB_URL = "mongodb+srv://<username>:<password>@cluster..."
AWS_ACCESS_KEY_ID = "your-aws-access-key"
AWS_SECRET_ACCESS_KEY = "your-aws-secret-key"
AWS_DEFAULT_REGION = "us-east-1"
ECR_REPO = "usvisa"
```

---

## 🛠️ Workflow

1. **constant**
2. **config\_entity**
3. **artifact\_entity**
4. **component**
5. **pipeline**
6. **app.py / demo.py**

---

## 📌 Note

* Use `conda activate visa` before running any script.
* Always push changes to GitHub → CI/CD pipeline will auto-deploy.
* EC2 instance runs on a paid tier (\~₹12/hr for T2.large).

---


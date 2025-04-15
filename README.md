# Crop-app

An AI-powered crop yield prediction system designed to assist farmers and agricultural researchers by forecasting crop yield based on parameters such as soil conditions, weather data, and organic fertilizers. The system uses a Random Forest Regressor for prediction and features a user-friendly Streamlit interface for real-time interaction.

## Directory Structure

```
ai-crop-yield-prediction/
│
├── data/                          # Sample datasets for soil, weather, and fertilizer
│   ├── soil_conditions.csv
│   ├── weather_data.csv
│   └── fertilizers.csv
│
├── model/                         # Trained model and training scripts
│   ├── crop_yield_model.pkl
│   └── train_model.py
│
├── notebooks/                     # Jupyter notebooks for EDA and model training
│   └── crop_yield_analysis.ipynb
│
├── app/                           # Streamlit app files
│   ├── app.py
│   └── utils.py
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── LICENSE                        # License file

```

## Project Overview
The AI Crop Yield Prediction System leverages machine learning to provide crop yield estimates based on key agricultural inputs. The aim is to help improve decision-making in agriculture by giving accurate, data-driven yield forecasts.

### Features:
- Real-time yield prediction with Streamlit interface
- Uses weather, soil, and fertilizer data
- Trained using Random Forest Regression
- Visualization and feature importance insight
- Extendable to real-time sensor input or API-based weather updates

## Installation and Setup

### Prerequisites:
- Python 3.8+
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/prathapprr/food-waste-optimization.git
   cd prathapprr-food-waste-optimization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Files Description
1. **`data/':** Contains CSV datasets used for training and testing
2. **'model/train_model.py':** Script to train the Random Forest Regressor
3. **'model/crop_yield_model.pkl':** Serialized model file
4. **'notebooks/':** Contains EDA and training notebooks
5. **'app/app.py':** Streamlit web app for user interaction
6. **'app/utils.py':** Helper functions for data preprocessing and prediction

## Usage

1. Launch the Streamlit application using the command:
   ```bash
   streamlit run app.py
   ```
2. Upload or select soil, weather, and fertilizer data.
3. Click Predict Yield to view the forecast.
4. Explore visual insights such as feature importance and prediction trend.

## Contribution

Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a feature branch (git checkout -b feature-name)
3. Commit your changes (git commit -m 'Add feature')
4. Push to the branch (git push origin feature-name)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, feel free to reach out:
- **Developer:** Preetham N
- **Email:** hemaranesh@gmail.com
- **Location:** Bengaluru, Karnataka

---

Happy coding! 😊

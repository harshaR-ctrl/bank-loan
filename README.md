# Loan Approval System

An intelligent machine learning-based loan approval prediction system with a modern, premium web interface supporting Indian Rupees.

## Features

- 🎨 **Modern Premium UI** - Sleek glass-morphism design with smooth animations
- 💰 **Indian Rupee Support** - All currency in INR (₹)
- 🤖 **Machine Learning Model** - Random Forest classifier trained on 100+ loan records
- ⚡ **Real-time Predictions** - Instant loan approval probability assessment
- 📊 **Probability-Based Decisions** - See approval odds with detailed analysis
- 🔒 **Input Validation** - Comprehensive data validation for all fields
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile
- 🎯 **User-Friendly** - Intuitive interface with helpful hints and icons

## Project Structure

```
loan approval/
├── loan_dataset.csv          # 100 fabricated loan records (INR values)
├── train_model.py            # ML model training script
├── app.py                    # Flask backend application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/
│   └── index.html           # Modern web interface
└── static/
    ├── style.css            # Premium styling with animations
    └── script.js            # Interactive frontend logic
```

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- Flask 2.3.3
- scikit-learn 1.3.0
- pandas 2.0.3
- numpy 1.24.3

### 2. Train the Machine Learning Model

```bash
python train_model.py
```

This will:
- Load the fabricated dataset (100 loan applicants)
- Train a Random Forest classifier with 100 trees
- Scale features using StandardScaler
- Save the trained model as `loan_model.pkl`
- Save the scaler as `scaler.pkl`
- Display model accuracy metrics

## Running the Application

```bash
python app.py
```

The web application will start at: **http://localhost:5000**

Open your browser and navigate to the URL to access the loan approval system.

## How to Use

1. **Open the Application** - Visit http://localhost:5000
2. **Fill the Application Form** with your details:
   - **Age**: 18-80 years
   - **Annual Income**: ₹12 Lakhs to ₹40 Crores
   - **Loan Amount**: ₹15 Lakhs to ₹40 Crores
   - **Credit Score**: 300-850 (CIBIL Score)
   - **Work Experience**: 0-50 years in current employment
   - **Dependents**: 0-10 family members

3. **Click "Check Eligibility"** - The system analyzes your application
4. **View Results** - See approval status and probability percentage
5. **Apply Again** - Reset and submit another application if needed

## Model Performance

The trained Random Forest model achieves:
- **Training Accuracy**: ~92%
- **Testing Accuracy**: ~90%
- **Features Used**: 6 (Age, Income, Loan Amount, Credit Score, Employment Years, Dependents)

## Dataset Information

**100 Fabricated Loan Records** with the following features:

| Feature | Range | Description |
|---------|-------|-------------|
| Age | 18-80 | Applicant age in years |
| Income | ₹12L - ₹40Cr | Annual income in rupees |
| Loan Amount | ₹15L - ₹40Cr | Requested loan in rupees |
| Credit Score | 300-850 | CIBIL credit score |
| Employment Years | 0-50 | Years in current job |
| Dependents | 0-10 | Family members |
| Loan Approved | 0/1 | Approval status (0=No, 1=Yes) |

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Flask** | Python web framework for backend |
| **scikit-learn** | Machine learning (Random Forest) |
| **pandas** | Data manipulation & analysis |
| **numpy** | Numerical computing |
| **HTML5** | Web interface markup |
| **CSS3** | Modern styling & animations |
| **JavaScript** | Interactive frontend logic |
| **Bootstrap 5** | Responsive UI framework |
| **Font Awesome** | Icons |

## Input Validation Rules

The system validates all inputs:
- ✅ Age: 18-80 years
- ✅ Income: ₹12,00,000 - ₹40,00,00,000
- ✅ Loan Amount: ₹15,00,000 - ₹40,00,00,000
- ✅ Credit Score: 300-850
- ✅ Employment Years: 0-50
- ✅ Dependents: 0-10

Invalid inputs are rejected with specific error messages.

## API Endpoints

### POST /predict
Predicts loan approval based on applicant details.

**Request Body:**
```json
{
  "age": 35,
  "income": 3500000,
  "loanAmount": 8000000,
  "creditScore": 750,
  "employmentYears": 7,
  "dependents": 2
}
```

**Response (Approved):**
```json
{
  "approved": 1,
  "probability": 85.25,
  "message": "Loan APPROVED",
  "color": "success"
}
```

**Response (Rejected):**
```json
{
  "approved": 0,
  "probability": 32.10,
  "message": "Loan REJECTED",
  "color": "danger"
}
```

## UI Features

- 🌈 **Premium Glass-Morphism Design** - Modern gradient backgrounds
- ✨ **Smooth Animations** - Floating icons, slide-ups, pop-ins
- 🎨 **Color-Coded Results** - Green for approval, red for rejection
- 📍 **Helpful Icons** - Visual indicators for each field
- 💫 **Loading Animation** - Professional spinner during analysis
- 📱 **Mobile Responsive** - Optimized for all screen sizes
- 🔄 **Error Handling** - Clear error messages with error icons

## Model Information

**Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 10
- **Train/Test Split**: 80/20
- **Scaler**: StandardScaler (mean=0, std=1)

## Notes

⚠️ **Important Disclaimers:**
- This system is for **educational/demonstration purposes only**
- Predictions are based on a machine learning model trained on fabricated data
- Real loan approval decisions require:
  - Human review by loan officers
  - Credit bureau verification
  - Income documentation
  - Asset evaluation
  - Additional regulatory compliance
- Do not use this system for actual loan decisions

## Troubleshooting

### Model not found error
- Run `python train_model.py` first to train and save the model

### Port 5000 already in use
- Change port in app.py: `app.run(debug=True, port=5001)`

### CORS issues
- Make sure you're accessing via http://localhost:5000 (not different domain)

### Poor accuracy
- Dataset is fabricated with simulated patterns
- Use real loan data for production systems

## Future Enhancements

- Add database integration for storing applications
- Implement user authentication & dashboard
- Add data visualization (charts, statistics)
- Create admin panel for model management
- Add more sophisticated feature engineering
- Implement cross-validation for better evaluation
- Build API documentation with Swagger
- Add batch processing capability
- Create mobile app version
- Integrate with real banking APIs

## License

This project is provided as-is for educational purposes.

## Support

For questions or issues, review the code comments and verify that:
1. All dependencies are installed correctly
2. Python version is 3.7+
3. Dataset file exists (loan_dataset.csv)
4. Model files exist after training (loan_model.pkl, scaler.pkl)

---

**Made with ❤️ for learning AI/ML and web development**

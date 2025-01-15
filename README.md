# Predictive Prescription Model for Ozempic

In this project, we will use classification machine learning techniques to categorize patients into distinct groups based on their need for Ozempic. These categories will include individuals who absolutely need Ozempic, those who might need it, and others who would benefit more from dietary and lifestyle changes. Additionally, we aim to analyze prescription patterns to determine whether Ozempic is being overprescribed, especially in younger populations, and if social media influence may be contributing to this trend. By leveraging machine learning, we hope to ensure that Ozempic is prescribed only to those who truly need it, reducing the potential for overprescription and unnecessary treatments.

## What is Ozempic[^1]?

![Ozempic Logo](https://www.novocare.com/content/dam/diabetes-patient/novocare/redesign/Logos/Ozempic_logo_LG.png)

According to Ozempic's official website: 
> Ozempic® (semaglutide) injection 0.5 mg, 1 mg, or 2 mg is an injectable prescription medicine used: along with diet and exercise to improve blood sugar (glucose) in adults with type 2 diabetes to reduce the risk of major cardiovascular events such as heart attack, stroke, or death in adults with type 2 diabetes with known heart disease
It is not known if Ozempic® can be used in people who have had pancreatitis.

> Ozempic® is not for use in people with type 1 diabetes.

> It is not known if Ozempic® is safe and effective for use in children under 18 years of age.

Ozempic is manufacured by Novo Nordisk 

## Criteria for prescribing Ozempic[^2]?

Per Keck Medicine, there are specific criteria for prescribing someone Ozempic or Wegovy.  

“For prescribing Wegovy for weight loss, a person must have a body mass index (BMI) of 30 or greater. It’s also approved for use in people with a BMI of 27 or greater, who have an accompanying overweight- or obesity-related condition, such as high blood pressure or sleep apnea,” Dr. Dominguez says. 

Ozempic is sometimes prescribed off-label for weight loss but is mostly used to treat people with diabetes, she says. 

## What is included in this project?

- Classification model to predict Ozempic qualification based on factors like BMI, blood pressure, cholesterol, smoking, alcohol use, and physical activity.
- Advanced features created, including risk score and comorbidity flag, to optimize model accuracy.
- Dataset balance improved with SMOTE and optimized RandomForest model using GridSearchCV.
- Model predicts patients who qualify for Ozempic, identifying high-risk individuals in need of the drug.
- GLP-1 Assessment Tool: Built a web app using Flask to predict Ozempic eligibility based on user inputs like BMI and age, incorporating logic to assess eligibility criteria and display results dynamically.

## What Does the GLP-1 Assetment Tool Do?

- Model Loading & Input: The Flask app loads a pre-trained machine learning model from a optimized_model.pkl file and collects health data (e.g., weight, age, blood pressure) from users.
- Data Processing & Prediction: The app calculates BMI, risk scores, and other features, then uses the model to predict eligibility for Ozempic.
- Results Display: Qualification results, including BMI and risk score, are displayed dynamically on the webpage.
- Design: The form is designed with Tailwind CSS for a responsive and user-friendly layout.

![Screenshot 2025-01-14 at 6 15 26 PM](https://github.com/user-attachments/assets/d4ed1a4b-15c2-4e17-bd5b-f0c831d2a2eb)

## Ozempic vs Wegovy[^2]?

Both are semaglutide injections, but they vary in dosage. Wegovy has a slightly higher maximum dosage.  

"Wegovy was studied specifically for weight loss, and the FDA approved the drug for weight loss in people 12 years and older. Both Ozempic and Wegovy are made by the same company, and the main difference besides dosage is their FDA clearance. Wegovy is approved specifically for weight loss. Ozempic is approved for diabetes management, but some doctors prescribe it to be used off-label (which is when a medication is used to treat a condition other than its FDA-approved criteria) for weight loss, too."
 
## Ozempic in Social Media and Culture

2024 was the year of Ozempic. Less than 10 seconds into the Golden Globes in January 2025, Nikki Glazer dubbed the show "Ozempic's Biggest Night"[^3]. A few days later, the American Name Society announced that Ozempic was chosen as the winner of the Name of the Year for 2024[^4]. 

Ozempic seems to be everywhere because according to a CNBC article[^5], Wegovy accounted for $263 million in ad spending in 2023, while Ozempic made up $208 million in ad spending. 

This high ad spending is reaching millions and as a result, Ozempic is being reframed from its intended use as an insulin-producing type 2 diabetes medication to a widely sought-after weight loss medication[^6].


<img width="598" alt="Ozempic Biggest Night" src="https://github.com/user-attachments/assets/6883e71b-9331-476e-a403-533178d0188f" />





Sources:

[^1]: https://www.ozempic.com/

[^2]:https://www.keckmedicine.org/blog/ozempic-for-weight-loss-los-angeles/

[^3]: https://www.yahoo.com/lifestyle/ozempics-biggest-night-how-weight-loss-drugs-showed-up-at-the-2025-golden-globes-055552886.html

[^4]: https://www.americannamesociety.org/ozempic-is-the-ans-name-of-the-year-for-2024/

[^5]: https://www.cnbc.com/2024/04/03/weight-loss-diabetes-drug-ad-spending-tops-1-billion.html

[^6]: https://doi.org/10.55016/ojs/muj.v2i2.79247

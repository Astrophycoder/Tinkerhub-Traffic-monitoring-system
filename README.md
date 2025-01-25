# Digital Twin Traffic Management System with Integrated Woman Safety Features

## Basic Details
### Team Name: Code Wizards

### Team Members
- Malavika P - SNGCE

### Hosted Project Link
[mention your project hosted project link here]

### Project Description
In the modern urban landscape, effective management of traffic is crucial. The challenge is to develop a digital twin model that can simulate traffic scenarios. This digital twin will provide a detailed representation of the urban infrastructure, enabling the analysis of various "what-if" scenarios. The goal is to optimize traffic flow, improve public service response times, and aid city planners in making data-driven decisions for future infrastructure development. By leveraging advanced simulation tools, predictive analytics, and interactive visualization, the project aims to create a robust, scalable, and user-friendly solution for comprehensive urban infrastructure management.

### The Problem statement
 Project Goals and Objectives
1.	Real-Time Traffic Monitoring and Simulation
o	Create a highly detailed and dynamic digital twin of the urban area that simulates data on traffic flow.
o	Use simulated data to predict the impact of traffic congestion at various points within the urban area.
o	Simulate scenarios involving public service disruptions (e.g., emergency responses, utility failures) to understand their impact on traffic and overall urban mobility.
o	Assess the resilience of the urban infrastructure under various stress scenarios, including peak traffic times and emergency situations.
o	Create intuitive dashboards and visualization tools for easy access to simulation results and optimization recommendations.
2.	Optimize Traffic Flow
o	Implement predictive analytics to foresee congestion and adjust traffic signals proactively.
o	Reduce travel time and improve overall commuting experience for citizens.
3.	Enhance Road Safety
o	Detect incidents automatically and alert emergency services promptly.
o	Minimize accidents by analysing traffic patterns and implementing safety measures.
4.	Provide Integrated Woman Safety Features
o	Incorporate a heartbeat monitoring system to ensure personal well-being.
o	Develop a multi-tier alert system (Red, Yellow, Blue) to respond to various safety scenarios.
o	Facilitate immediate assistance in case of harassment or sudden health issues.


### The Solution
We are developing a Digital Twin Traffic Management System with Integrated Safety Features to address the challenges of urban traffic management and safety. The solution leverages advanced simulation tools, predictive analytics, and interactive visualization to create a comprehensive and user-friendly platform. Here's how we are solving the problem:
1.	Real-Time Traffic Monitoring and Simulation:
o	Create a highly detailed and dynamic digital twin of the urban area to simulate data on traffic flow.
o	Use simulated data to predict the impact of traffic congestion at various points within the urban area.
o	Simulate scenarios involving public service disruptions (e.g., emergency responses, utility failures) to understand their impact on traffic and overall urban mobility.
o	Assess the resilience of the urban infrastructure under various stress scenarios, including peak traffic times and emergency situations.
o	Provide intuitive dashboards and visualization tools for easy access to simulation results and optimization recommendations.
2.	Optimize Traffic Flow:
o	Implement predictive analytics to foresee congestion and adjust traffic signals proactively.
o	Reduce travel time and improve overall commuting experience for citizens.
3.	Enhance Road Safety:
o	Detect incidents automatically and alert emergency services promptly.
o	Minimize accidents by analysing traffic patterns and implementing safety measures.
4.	Provide Integrated Safety Features:
o	Incorporate a heartbeat monitoring system to detect danger.
o	Develop a multi-tier alert system (Red, Yellow, and Blue) to respond to various safety scenarios.
o	Facilitate immediate assistance in case of harassment or sudden health issues.
5.	Data Sources:
o	Traffic Data: Collected from AI cameras (in prototype Kaggle datasets).
o	Heartbeat Data: Collected from users' smartphones (in prototype Kaggle datasets).
o	Data Ingestion:
  APIs to fetch and pre-process data.
	Connected to the Database.
o	Database:
	MySQL database to store real-time traffic data, user information, heartbeat data, and alerts.
o	Processing Engine:
	Predictive analytics using Tensor Flow to analyse traffic patterns.
o	User Interfaces:
	Web dashboard for administrators to monitor traffic conditions.
  Mobile app for users to monitor heartbeat data and receive alerts.
o	APIs:
	Google Maps API for traffic data integration.
	Custom APIs for data exchange between components.
1.	Web Dashboard for Admins (Police officers , helplines, nearby officials) :
o	Home Screen: Real-time traffic conditions map, key metrics, alerts, and search functionality.
o	Predictive Analytics Screen: Traffic pattern predictions, congestion forecasts, and incident reports.
o	Alert Management Screen: List of active alerts, alert details, and response actions.
2.	Mobile App for Safety Features:
o	Home Screen: emergency contact buttons.
o	History Screen: Historical heartbeat data and alerts history.
o	Notification: Send a notification asking “Are you in danger?” If no response, send signal.
1.	Real-Time Traffic Data Processing:
o	Data Cleaning: Remove duplicates; handle missing values, and pre-process data to ensure quality.
o	Aggregation and Analysis: Summarize data for analysis and handle large datasets efficiently.
o	Predictive Analytics: Apply machine learning models using Tensor Flow for forecasting traffic patterns and detecting incidents.
2.	Data Storage Plan:
o	Database Schema: Define MySQL database schema for storing real-time traffic data, user information, heartbeat data, and alerts.
o	Data Access Methods: Define API endpoints for data ingestion and retrieval and implement security measures and access control.


## Technical Details
### Technologies/Components Used
For Software:

Languages used:
Python: For data processing, analysis, traffic simulation analysis, and machine learning.
JavaScript: For web development and creating interactive visualizations.

Frameworks used:
Flask: For building server-side APIs and web application development.
React Native: For creating the mobile application.

Libraries used:
Pandas: For data manipulation and analysis.
TensorFlow: For predictive analytics and machine learning models.
Seaborn: For data visualization.
Matplotlib: For creating static, animated, and interactive visualizations.

Tools used:
MySQL: For storing real-time traffic data, user information, heartbeat data, and alerts.
Git: For version control and collaborative development.
Docker: For containerizing the application for easy deployment.
Google Maps API: For traffic data integration.

For Data Collection:
Heartbeat Monitoring:
Existing photoplethysmography (PPG) apps: Used by users to monitor their heartbeat. The data from these apps is continuously sent to our system for analysis.
Smartphones: Used to collect heartbeat data and send it to the app.


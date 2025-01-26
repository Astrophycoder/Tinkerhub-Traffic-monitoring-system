# Digital Twin Traffic Management System with Integrated Safety Features

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
3.	Optimize Traffic Flow
o	Implement predictive analytics to foresee congestion and adjust traffic signals proactively.
o	Reduce travel time and improve overall commuting experience for citizens.
5.	Enhance Road Safety
o	Detect incidents automatically and alert emergency services promptly.
o	Minimize accidents by analysing traffic patterns and implementing safety measures.
7.	Provide Integrated Woman Safety Features
o	Incorporate a heartbeat monitoring system to ensure personal well-being.
o	Develop a multi-tier alert system (Red, Yellow, Blue) to respond to various safety scenarios.
o	Facilitate immediate assistance in case of harassment or sudden health issues.




### The Solution

Our Digital Twin Traffic Management System addresses urban mobility challenges through an integrated approach combining infrastructure simulation and safety monitoring. The solution architecture comprises:

**1. Core Simulation Engine**  
- Implements a high-fidelity digital twin model replicating urban road networks  
- Utilizes historical and real-time traffic data (simulated via Kaggle datasets)  
- Enables "what-if" scenario analysis through:  
  - Congestion pattern simulation at critical junctions  
  - Public service disruption modeling (emergency responses, utility failures)  
  - Infrastructure stress testing under peak traffic conditions  

**2. Predictive Analytics Framework**  
- Combines Random Forest algorithms and TensorFlow models for:  
  - Short-term traffic pattern forecasting (15-60 minute predictions)  
  - Long-term congestion point identification  
  - Emergency response optimization  

**3. Resilience Assessment Module**  
- Evaluates infrastructure capacity through:  
  - Multi-variable stress testing  
  - Failure cascade simulations  
  - Recovery time estimations  

**4. Integrated Safety System**  
- Implements PPG-based anomaly detection:  
  - Continuous heartbeat monitoring via smartphone integration  
  - Two-stage emergency protocol:  
    1. Immediate user notification ("Are you in danger?")  
    2. Automated alert escalation with geolocation tracking  

**5. Visualization Interface**  
- Dual-platform user interface:  
  - **Web Dashboard**:  
    - Real-time traffic heatmaps  
    - Scenario simulation controls  
    - Emergency response coordination  
  - **Mobile Application**:  
    - Personal safety monitoring  
    - Historical data access  
    - Emergency contact integration  

**Technical Implementation**  
- Data Pipeline:  
  - Ingestion: Custom APIs + Google Maps integration  
  - Processing: Pandas/NumPy for data transformation  
  - Storage: MySQL database (CSV in prototype phase)  

- Simulation Tools:  
  - Scipy for signal processing  
  - Plotly for spatial visualization  
  - Leaflet.js for interactive mapping  

This system provides municipal authorities with actionable insights for infrastructure planning while offering citizens enhanced safety through real-time health monitoring integration.
o	Data Access Methods: Define API endpoints for data ingestion and retrieval and implement security measures and access control.


## Technical Details
### Technologies/Components Used
Software Implementation:

Programming Languages: Python (Backend), JavaScript (Visualization)

Frameworks: Flask (REST API), React Native (Mobile Interface)

Libraries:
Pandas (Data Processing)
Scipy (Signal Filtering)
Scikit-learn (Machine Learning)
Plotly (Data Visualization)

Tools:
Ngrok (Secure Tunneling)
Google Maps API (Geospatial Data)
MySQL (Data Storage)

For Data Collection:
Heartbeat Monitoring:
Existing photoplethysmography (PPG) apps: Used by users to monitor their heartbeat. The data from these apps is continuously sent to our system for analysis.
Smartphones: Used to collect heartbeat data and send it to the app.

### Project Documentation
## Screenshots
![Screenshot](docs/Screenshot (2).png)
![Screenshot](docs/Screenshot (2).png) 
![Screenshot](docs/Screenshot (3).png) 

### Diagrams
![workflow](/path-to-image/workflow_diagram.png) Workflow: High-level system architecture and data flow

What should I answer for :


This is a graded discussion: 5 points possible

due Oct 2, 2025 at 5:29pm
Required discussion 5.1: Evaluating the feasibility of an ML problem - Section A
2929 unread replies.2929 replies.
 Learning outcome addressed
Apply probabilistic reasoning to support decision-making in ML.
   Discussion directions and prompts
Introduction
In real-world applications, not every ML problem is feasible without thoughtful consideration of the data and its underlying assumptions. In this activity, you will apply probabilistic reasoning to explore candidate functions based on limited data.

Instructions
Revisit the ML problem you identified in Module 2, Required discussion 2.1. Reflect on your original problem and respond to the following to evaluate its feasibility in a probabilistic learning context:

Briefly describe the ML problem you selected, the data set and its source (real or hypothetical).
Evaluate the following three key assumptions for your data set and problem set-up:
Probabilistic setting: does your data set represent samples drawn independently from a fixed (but possibly unknown) probability distribution? Justify your answer with evidence from the data set or problem domain.
Stationarity: are the statistical properties of the data (e.g. distribution, feature relevance) expected to remain stable over time or across the application environment? Explain any concerns if trends, seasonality or domain shifts might affect stationarity.
A priori knowledge: do you have sufficient domain knowledge or context to guide model design (e.g. features, labels or evaluation metrics)? Mention any existing benchmarks, feature relevance insights or prior research.
If any of the above assumptions are not satisfied, how would you:
Revise the data set (e.g. re-sampling, feature engineering or filtering)?
Reframe the problem (e.g. redefine the target, split into sub-problems or choose a different learning goal)?
Completion requirements
Reflect on the prompts and submit your responses directly in the discussion board below.
Please keep your responses under 600 words.
Engage with peers by commenting thoughtfully on their posts.
Consider providing any advice or suggestions you might have to your peers' questions.
The average completion time for this activity is 60 minutes.

This is a required activity and counts towards the completion of the programme
____


Other teammates replied::::
There is a rubric associated with this discussion. Select the three vertical dots in the header bar of this text area and select 'Show Rubric' in the dropdown menu. This will display the completion requirements associated with this discussion.

Search entries or author
Search entries or author
 Filter replies by unread      
 ReplyReply to Required discussion 5.1: Evaluating the feasibility of an ML problem - Section A
Collapse Subdiscussion
Leonardo Diodato
Leonardo Diodato
Sep 27, 2025Local: Sep 27, 2025 at 2:44pm<br>Course: Sep 27, 2025 at 1:44pm
The ML problem I selected in module 2 was about sales forecast for new product launches and seasonal sales forecast for existing ones. The dataset for this problem would be given by the historical data about products launches and the performance of sales related to each of them.

Probabilistic setting: Given that the sales performances of the company are influenced by seasonality, the data points representing these sales could be represented by an unknown probability distribution which is affected by many factors, but mainly seasonality.

Stationarity: the historical data of sales performances for product launches should not show any stationarity, there are trends expected, given by the kind of product that's being considered, and the launch date around the year.

A priori knowledge: I do not have the dataset or prior knowledge about he sales performances, as I'm not involved with the teams managing the sales in the company, but I think that the features of this model would be given by the launch date, product type, specific product size, and all the specific metrics about each product, and the output of the model would be the sales forecast in 7 days or 30 days. All of these informations should be available internally of the company anyway, for all the past product launches, and domain knowledge could be provided by involving the sales team directly into the project.

Feature engineering could provide some additional useful information for this model.

 

 Reply Reply to Comment
Collapse Subdiscussion
Laveena Ramchandani
Laveena Ramchandani
Sep 28, 2025Local: Sep 28, 2025 at 4:43pm<br>Course: Sep 28, 2025 at 3:43pm
The problem I identified is preventing the use of outdated Swiss Franc (CHF) exchange rates in the Revenue Management System (RMS) to avoid revenue miscalculations and incorrect ticket/ancillary pricing.

Probabilistic setting
FX rates evolve as a stochastic process and feeds are often sampled at regular intervals. However, dependencies exist: rates are autocorrelated, and delays in feed updates may cluster around certain times (e.g., system outages). Transaction logs also reflect correlated behaviors (bulk updates, promotions). If we treat each timestamped rate observation as a draw from an underlying distribution conditioned on market dynamics, a probabilistic framing is feasible. To strengthen this assumption, resampling could normalize for time-of-day effects and dependencies.

Stationarity
FX markets are non-stationary: volatility regimes, macroeconomic events, or central bank interventions shift distributions. Seasonality is also relevant—ticket demand spikes during holidays or events interact with FX sensitivity. For RMS, the distribution of “valid vs stale” may change depending on system stability, provider latency, or frequency of manual overrides. Concerns: sudden volatility spikes (e.g., SNB unpegging CHF in 2015) could break assumptions. A practical mitigation would be to (a) retrain models frequently, (b) incorporate volatility/market regime features, and (c) monitor drift with alerts for RMS teams.

A priori knowledge
RMS analysts and FX traders know which sources are most reliable, how quickly feeds typically update, and what thresholds are acceptable for deviations. Benchmarks: published FX feeds from providers like Bloomberg/Reuters, known latency SLAs, and RMS logs of past stale-rate incidents. Prior work on anomaly detection in financial time series also provides methodological guidance. This knowledge helps define features (lagged differences, volatility windows), labels (flag rates older than x minutes or deviating >y% from benchmark), and evaluation metrics (precision/recall for stale flags is more important than raw accuracy, since missing a stale rate can directly harm revenue).

If assumptions are not satisfied -->

Revise the dataset:

Resample rates at consistent intervals to reduce autocorrelation bias.

Engineer volatility-adjusted features (e.g., deviation relative to rolling standard deviation).

Filter unreliable FX sources or weight them differently.

Reframe the problem:

If labels are unreliable, use unsupervised anomaly detection (isolation forests, autoencoders) instead of supervised classification.

Break into subproblems (e.g., detect missing feed updates separately from stale-rate drift).

Use probabilistic forecasting (predict distribution of valid FX rate) rather than binary stale/valid classification, to allow RMS to quantify confidence.

 Reply Reply to Comment
Collapse Subdiscussion
Benjamin Baumann
Benjamin Baumann
Sep 28, 2025Local: Sep 28, 2025 at 5:05pm<br>Course: Sep 28, 2025 at 4:05pm
Feasibility of applying probabilistic learning to planning decision support

The ML problem
The problem I looked at in Module 2 was whether ML can support faster and more accurate planning decisions. The data set would combine structured elements (application type, property details, geospatial data, appeal outcomes) with unstructured sources (PDF reports, consultation responses, officer notes). The aim is to predict likely decisions (approve/refuse) and the probability of an appeal, giving officers a decision support tool.

Probabilistic setting
Each planning application could be treated as a sample drawn from the underlying distribution of "all possible applications and outcomes." However, in practice, this assumption is only partly true. Applications vary widely by council and geography (urban vs rural), conservation areas vs new towns and officer discretion introduces variability. The data is not perfectly i.i.d., but if we sample broadly across councils and time periods, the data can approximate a fixed distribution. That would allow a probabilistic model to learn useful patterns while still recognising local nuances.

Stationarity
This is probably the biggest challenge. Policy changes, housing targets, or political priorities can shift the distribution of outcomes over time. For example, a council under pressure to meet housing demand may approve more marginal schemes, while new environmental rules could increase refusals. These domain shifts mean the statistical properties are not fully stationary. To handle this, the model would need retraining on recent data and possibly weighting recent cases more heavily. Monitoring performance across time slices would be essential to check for performance drift.

A priori knowledge
There’s strong domain knowledge to guide feature design. Planning officers already use policy references, geospatial constraints, and precedent cases to make decisions. Prior research shows correlations between certain features (e.g. conservation area status, flood risk) and refusal rates. Benchmarks exist in the form of appeal overturn rates or time-to-decision metrics. These give us a foundation to shape features and evaluation metrics (accuracy, recall on refusals, fairness across applicant types).

If assumptions aren’t met

Data revision: Broaden the training set across multiple councils, re-sample to balance approved/refused classes, and engineer features to capture evolving policies.

Problem reframing: Instead of predicting binary outcomes, we could frame the task as ranking cases by “decision confidence” or “appeal risk,” which might be more stable over time.

Alternative goals: Break the problem down such as predicting which tasks are repetitive vs subjective, or flagging cases likely to trigger appeals rather than replacing officer judgement.

In summary
The problem is feasible in a probabilistic learning context, but with some caveats. Applications are not perfectly i.i.d., policies shift, and officer subjectiveness creates noise. With careful data design, domain-informed features, and regular retraining, ML could still provide valuable decision support. The model’s usefulness will depend less on pure accuracy and more on whether it adapts to policy changes, highlights edge cases, and genuinely saves planning time without undermining trust.

 Reply Reply to Comment
Collapse Subdiscussion
Jack Dunning
Jack Dunning
Sep 28, 2025Local: Sep 28, 2025 at 7:16pm<br>Course: Sep 28, 2025 at 6:16pm
The ML problem I selected:

You can improve the accuracy of regional forecasts using local farm data - by bias correcting the forecast to the real live weather data collected on the farm. This would improve the accuracy of the forecast and help improve farm decisions, increasing yield and reducing waste.
The real data sets used would be:
Regional forecasts (e.g. ECMWF) 
Local farm weather station data
3 key assumptions:

Probabilistic setting

Each data point in this problem is a pair: the regional forecast (e.g. from ECMWF) and the actual observation from the farm’s weather station. Each pair is simply one example of how the weather actually turned out compared to what was predicted.

The independence part of the assumption is only partly true. Weather is naturally linked over time and space (today’s rainfall depends on yesterday’s, and nearby locations are correlated).

So while we could treat forecast-observation pairs as independent for modelling, in reality they have some dependencies. 

The evidence here is from domain knowledge, meteorology studies consistently show that weather has strong autocorrelation. For example, daily temperature is highly correlated with the day before, and rainfall often persists across multiple days. Or regional models like ECMWF are known to have systemic and long term biases (e.g. https://www.ecmwf.int/en/elibrary/81197-evaluation-biases-and-skill-ecmwf-summer-sub-seasonal-forecasts-northern Links to an external site.). This proves that the forecast-observation pairs are built on consistent underlying weather processes, and not therefore completely independent.

Stationarity

Not fully. Weather data has clear seasonality and long-term climate trends mean distributions can shift over years. The relationship between forecasts and observations may also change as the forecasting models are updated. Evidence includes (1) known seasonal cycles in rainfall/temperature, and (2) domain studies showing climate change alters baselines and extremes. This means the data is only locally stationary and models will need regular re-training or seasonal adjustments.

A priori knowledge

Yes. I have specific domain knowledge to guide model design. Forecast variables like rainfall, temperature, wind are the main features that matter. The local weather station observations provide labels or the correct information to train the model on. RMSE is a standard evaluation metric for forecasts. There are many previous scientific studies (e.g. https://www.sciencedirect.com/science/article/pii/S2212094721000621 Links to an external site.) that can act as existing benchmarks.


Revising assumptions / remedies

Probabilistic setting
Issue:
Data points are not fully independent (weather autocorrelation).

What to do:
Split training and test data by time, e.g. train on years 2022-2024 and test on years 2021. Then we would need to use past values of each weather variable as inputs to the model (e.g. if trying to predict temperature today, make sure the model knows the temperature yesterday). 


Stationarity

Issue:
Seasonality, climate trends, and forecast model updates make the data non-stationary.


What to do:
Include season/month as features, standardise per season, and re-train regularly to adapt to shifts. If models change (e.g. ECMWF update their model), re-calibrate bias correction with fresh data.

 Reply Reply to Comment
Collapse Subdiscussion
stephen sefa
stephen sefa
Sep 28, 2025Local: Sep 28, 2025 at 11:58pm<br>Course: Sep 28, 2025 at 10:58pm
The machine learning problem i identified is Challenges in sports. This is to use machine learning to limit the injuries of players and increase their performances. 

Probabilistic settings in sports can be seen in different ways such as uncertainty in player performances, which can be caused by fatigue or injury to the player. There is also incompleteness of information from sensors when they develop faults. 

Stationarity, in the world sports, data gathered are generally non-stationary because the environment defers or are dynamic and evolve constantly. With that said, there are other data sets that with time, becomes partially stationary example, the movement of patterns of players. This is done when you track the raw movement of players but it will only be for the short time. But in general, due to fatigue, injuries and performance of players, data gathered will evolve. 

I do not have prior knowledge. But in sports, there are so many events that occur so there are data available to the managers and coaches which helps them prepare for every game depending on their opponent. example Penalty conversion rate, Home team win, the strength and weakness of the opponents key players, et al.

if the above assumptions are not satisfied, resampling of the data will done. This could be by gathering more information where needed. Example, other data set can be used if that of the Penalty conversion rate did not produce much information.  

 Reply Reply to Comment
Collapse Subdiscussion
Raghavachary Nallani Charavarthula
Raghavachary Nallani Charavarthula
Sep 29, 2025Local: Sep 29, 2025 at 10:36am<br>Course: Sep 29, 2025 at 9:36am
Machine Learning Problem Description
Problem: Predicting climate-related risk, specifically flooding or associated damage, in urban and coastal regions.
Type: Supervised learning.

Regression: Predict continuous outcomes like flood extent (m²) or expected financial loss ($).

Classification: Categorize areas as high-risk, medium-risk, or low-risk.

Dataset:

Climate data: Temperature, precipitation, storm frequency, sea-level rise from NOAA, NASA, and IPCC.

Satellite/geospatial data: Elevation, flood zones, urban development from NASA, ESA, USGS.

Socioeconomic data: Population density, infrastructure from city governments and the World Bank.

Environmental data: Soil type, vegetation coverage from GIS databases.

Key Features: Temperature, precipitation, storm frequency, elevation, distance from coastline, urban density, soil type, vegetation coverage, population density.
Output Variable: Risk score, predicted flood extent, or expected financial loss.

ML Approach: Non-parametric models such as Random Forests or Gradient Boosting to capture nonlinear relationships among features.

2. Evaluation of Key Assumptions
A) Probabilistic Setting
Assumption: Data samples are independent and identically distributed (i.i.d.) from a fixed, but unknown, probability distribution.

Assessment: Partially satisfied.

Climate and geospatial data are collected over time and space; samples may not be fully independent (e.g., neighboring areas share similar rainfall patterns).

Temporal correlations exist (e.g., consecutive years of flooding events are related).

Evidence: Storm frequency, precipitation, and sea-level rise often show spatial and temporal autocorrelation.

B) Stationarity
Assumption: Statistical properties of the features and labels remain stable over time and space.

Assessment: Not fully satisfied.

Climate change introduces trends in temperature, sea-level rise, and storm frequency.

Urban development causes shifts in population density and impervious surfaces over time.

Soil and vegetation may change due to land-use shifts or extreme events.

Concern: Non-stationarity can degrade model performance when applied to future data.

C) A Priori Knowledge
Assumption: Sufficient domain knowledge exists to guide model design.

Assessment: Satisfied.

Features like elevation, distance from the coastline, and precipitation are well-known predictors of flooding.

Prior research, IPCC reports, and GIS studies provide benchmarks and context for risk assessment.

Established evaluation metrics (RMSE for regression, F1-score or AUC for classification) are available.

3. Mitigation Strategies for Unsatisfied Assumptions
If Probabilistic Setting is Violated
Resampling: Use spatially stratified sampling or block bootstrap to account for autocorrelation.

Feature engineering: Include spatial/temporal lag features (e.g., rainfall in neighboring regions, previous-year flood extent).

If Stationarity is Violated
Data revision: Include time as a feature, normalize trends, or use rolling windows to train on recent data.

Reframe problem: Predict short-term risk horizons (e.g., 1–5 years) instead of long-term future, or define risk relative to recent historical conditions.

Model choice: Consider online learning or temporal models (e.g., LSTM or gradient boosting with time-aware splits).

If A Priori Knowledge Were Limited
Feature selection: Use automated feature importance or dimensionality reduction to identify predictive variables.

Redefine target: Simplify the problem, e.g., binary flood/no-flood risk instead of precise financial loss.

 Reply Reply to Comment
Collapse Subdiscussion
Steven Amet
Steven Amet
Sep 29, 2025Local: Sep 29, 2025 at 12:22pm<br>Course: Sep 29, 2025 at 11:22am
Problem & Dataset Overview
My aim is to build a supervised classification model to predict SME/corporate credit deterioration (Non Performing Loan status within 6 months) using monthly macroeconomic indicators and bank-level credit data.

Macroeconomic data: unemployment_data, cpi_data, savings_ratio_data, disposable_income_data
Bank-level data: bank_NPL (target proxy)
Optional bank data: sector classification (not currently included)
Sources: Central Statistics Office (CSO), Central Bank of Ireland, internal credit systems.
1. Probabilistic Setting
Assumption: Data samples are drawn independently from a fixed probability distribution.

Evaluation:
This assumption is partially violated. The data is monthly time-series, meaning observations are temporally dependent. Economic indicators and credit deterioration evolve over time and are influenced by prior states, violating the i.i.d. assumption.

Evidence:
Autocorrelation and lag effects must be accounted for in Time-series ML models. Economic forecasting literature emphasises that macroeconomic variables often exhibit persistence and structural dependencies. [Econometri...orecasting]Links to an external site.

Mitigation:

Use lagged features and rolling statistics. 
Apply time-series cross-validation to preserve temporal structure.
2. Stationarity
Assumption: Statistical properties of the data remain stable over time.

Evaluation:
This assumption could be violated by certain characteristics, however this can be mitigated. Macroeconomic indicators and credit risk profiles are subject to non-stationarity due to:

Business cycles, however we can reduce noise.
Sector-specific shocks (e.g., COVID-19)
Evidence:
Stationarity is crucial for reliable forecasting, yet macroeconomic data often shows evolving trends and variance. Credit risk models must adapt to regime shifts and structural breaks. [Exploring...redictions]Links to an external site.

Mitigation:

Include volatility measures and regime indicators (e.g., Sahm Rule).
Use backtesting across multiple economic regimes. Data is years 2007 to 2025.
Monitor concept drift and retrain periodically.
3. A Priori Knowledge
Assumption: Sufficient domain knowledge exists to guide model design.

Evaluation:
This assumption is well satisfied.

Relevant features (macroeconomic)
A meaningful target (NPL proxy)
Evaluation metrics (ROC-AUC, PR curve)
Prior research and frameworks (e.g., Sahm Rule, EWI)
Evidence:
Early Warning Indicators (EWI) are widely used in banking to proactively manage credit risk. Research on SME credit risk prediction using financial and macroeconomic indicators supports your feature choices. [Early warn...risk - BAI] Links to an external site.[An Analysi...nterprises]Links to an external site.

If Assumptions Are Not Fully Met
Revise the Dataset
Feature Engineering: Add lagged variables, rolling averages, volatility indicators.
Filtering: Segment by sector 
Imputation: Use model-based or domain-informed imputation for missing bank data
Reframe the Problem
Survival Analysis: Model time-to-default instead of binary classification.
Multi-stage Modeling: First predict EWI score, then deterioration.
Anomaly Detection: Flag unusual patterns in bank-level metrics.
Conclusion
ML problem is feasible but requires careful handling of temporal dependencies, non-stationarity, and economic context. 

 Reply Reply to Comment
Collapse Subdiscussion
Hanyi
Hanyi
Sep 29, 2025Local: Sep 29, 2025 at 3:14pm<br>Course: Sep 29, 2025 at 2:14pm
I selected the MITSUI&CO. Commodity Prediction Challenge as my ML problem. This competition asks participants to predict returns for multiple financial time series, including commodities, futures, U.S. stocks, and foreign exchange. The dataset comes from real global financial markets, with files that include historical prices, trading volumes, and exchange rates (train.csv), as well as the prediction targets (train_labels.csv) such as log returns and spread values between instruments. The test data mirrors the training structure and is designed to simulate a real forecasting environment.

Probabilistic setting
The financial time series in this dataset can be approximated as samples drawn from a fixed but unknown probability distribution. Each series corresponds to a specific instrument or market (e.g., LME metals, JPX stocks, FX exchange rates) with its own data-generating process. Within a given period, the samples can reasonably be treated as independent and identically distributed. However, it is important to acknowledge that correlations exist between instruments, so the independence assumption is not fully satisfied.
Stationarity
Over short time horizons, the statistical properties of financial data (such as return distributions and volatility) tend to remain relatively stable, so assuming stationarity is acceptable. Nevertheless, financial markets are also influenced by seasonality, trends, and unexpected shocks. For example, commodity prices can shift due to quarterly demand cycles or geopolitical events. This means that full stationarity cannot be guaranteed and must be handled with care.
A priori knowledge
I bring some domain knowledge from my current work as a financial data analyst in FP&A, where I use regression and forecasting models to support planning. This helps me understand the relationship between features (prices, volumes) and labels (returns). Prior research has also identified that lagged variables and technical indicators are relevant predictors in financial modeling. In addition, the competition provides documentation (e.g., target_pairs.csv) that explains how the targets are derived, which further guides model design.
Addressing unmet assumptions
If the independence assumption does not hold, I could incorporate covariance features or adopt multivariate time series models that explicitly model dependencies across assets.
If stationarity is violated due to regime changes or seasonality, I could use rolling windows or retrain models regularly to adapt to new market conditions. Seasonal patterns may also be captured through feature engineering.
If domain knowledge is insufficient, I could rely on insights from financial literature and Kaggle community benchmarks, to guide experimentation.
 

 Reply Reply to Comment
Collapse Subdiscussion
Devang Shah
Devang Shah
Sep 29, 2025Local: Sep 29, 2025 at 10:20pm<br>Course: Sep 29, 2025 at 9:20pm
The ML problem I selected in module 2 was about a machine learning classification model that accurately categorizes incoming insurance claims into two streams in real-time: "Approve" for straight-through processing (STP) and "Review" for manual handling by a human adjuster.

Probabilistic setting: In the probabilistic setting, the assumption that the data set comprises independent samples drawn from a fixed (though possibly unknown) probability distribution is only partially valid. For the majority of claims, independence is a reasonable approximation, as unrelated incidents—such as a motor vehicle accident and a burst pipe occurring in different locations—do not exhibit statistical dependence. However, this assumption is violated in the context of catastrophic events, wherein a single exogenous shock, such as a hailstorm, flood, or wildfire, produces a large concentration of geographically proximate and temporally aligned claims.

If Assumptions Are Not Fully Met What to do:
Feature Engineering: Create features that capture the dependencies. For example, Feature that counts the number of claims from the same geographic area within a short time frame to flag potential storm-related claims.
Specialized Models: Use models designed for sequential or grouped data. 
Careful Validation: Standard cross-validation can be misleading with dependent data. 

Stationarity: The stationarity assumption is unlikely to hold, as claims exhibit seasonal patterns and the data distribution is subject to shifts from factors such as emerging fraud schemes, regulatory changes, and external shocks like pandemics or supply chain disruptions.
If Assumptions Are Not Fully Met What to do:
Continuous Monitoring: Implement a system to monitor the model's live performance. 
Regular Retraining: The most common strategy is to periodically retrain the model on fresh data. 
Online Learning: For rapidly changing environments, consider online learning models. 

A priori knowledge: Strong a priori knowledge exists in this problem, as domain experts—such as claim adjusters and underwriters—leverage the insurance industry’s rich data history to identify relevant features and known indicators of complex or potentially fraudulent claims.
If Assumptions Are Not Fully Met What to do: 
Exploratory Data Analysis (EDA): Use visualization and statistical techniques to deeply understand the data's structure, relationships, and patterns. 
Automated Feature Engineering: Use techniques like Principal Component Analysis (PCA) for dimensionality reduction or automated tools
Model-Based Feature Importance: Train an initial model and inspect its feature importance scores. 

 Reply Reply to Comment
Collapse Subdiscussion
Hassan Chagani
Hassan Chagani
Sep 30, 2025Local: Sep 30, 2025 at 1:48pm<br>Course: Sep 30, 2025 at 12:48pm
My machine learning project was identifying tall structures from satellite images. Identification of these buildings would be useful when developing catastrophe models, such as those for earthquakes and cyclones. A random sample would be extracted, and would be divided into training, validation and testing sets. Assuming all images are of the same resolution, the images would be divided into grid cells and human analysts would indicate whether each cell contains any tall structures (i.e. give those cells a value of 1). The training data set would be fed into a neural network to train it, where the input parameters would be the satellite images themselves split into grid cells, the time of day to account for shadows and the location to account for cultural differences in building design. The output parameters would be an array of probabilities corresponding to each grid cell. Once trained, the validation set would be exposed to the neural network to ensure there has been no under or overfitting and then to the testing set to evaluate performance.

 

Probabilistic setting

By selecting images at random, we would be drawing independent samples from a fixed distribution. Apart from areas of overlap, the images are independent from each other. Any grid cells that overlap with other images can be identified with latitude and longitude coordinates and can be merged. The underlying distribution from which samples are extracted would be urban settings with or without tall structures.

To ensure the sample images are independent and a therefore a good representation of all the images, they should be selected from many cities, and at different times of the day and year to account for daily and seasonal variations.

However, as there are fewer tall buildings than short buildings in cities, we would need to ensure that the sample contains enough grid cells with tall buildings in order to train the neural network. Care should be taken here to ensure that tall buildings are not over-represented when sampling. Although time consuming, we could consider resampling if an insufficient number of tall structures have been identified.

 

Stationarity

The statistical properties of the data are not expected to remain stable over time. For example, new buildings are always being constructed, and old ones are always being torn down. Additionally, extensions can be added to buildings, changing their footprints and potentially their heights. The model would need to be retrained after a certain period of time with updated images.

There is seasonal variation as well where trees could cover buildings from view in the warmer months, and snow could have the same effect in winter. This could be accounted for by taking the date of the image as an input parameter.

Different satellite sensors may see different colours when constructing the image, which could also affect classification. Having an additional input parameter being the sensor itself, and ensuring that a sufficiently large number of images are sampled across all sensors during the training, validation and testing phases could mitigate this.

 

A priori knowledge

Human analysts in insurance should have enough knowledge and experience to identify tall buildings from aerial photos. However, only relying on aerial photographs may not be sufficient, especially in cases where the data is ambiguous, such as where building shadows are obstructed or relatively short in length. Additional 3D data from LiDAR would be helpful. Human errors associated with misclassification should be expected.

Acquiring the satellite images themselves may require commercial licences with providers such as Maxar Links to an external site..

 Reply Reply to Comment
Collapse Subdiscussion
Sam Cui
Sam Cui
Sep 30, 2025Local: Sep 30, 2025 at 10:01pm<br>Course: Sep 30, 2025 at 9:01pm
Problem: Prediction of driver inputs when vehicle is at or near a state of loss of control (or, more generally, any undesired vehicle behavior)

Probabilistic setting: yes, even the same person given the exact same set up may react slightly differently each time as humans are imperfect. the range of behaviors seen across drivers of different experience levels is predicted to be very wide. 
Staionarity: most likely yes. the way an "average" driver responds is likely to change very slowly over time given the same environments. however, the environments/inputs themselves may change (e.g. as cars develop in a certain trend over time). 
A priori knolwedge: yes. physically based models can be used to generate more insightful features (e.g. whether a car is in over or understeer) than the raw data themselves.
Benchmarks: simple PID-like feedback-based control models can be and have been used to model driver behavior but have the limitation of lack of feedforward/predictive correction ability by definition. ML model would aim to beat this type of model
Based on the above, it may be best to focus the study to e.g. only "expert" drivers and only specific types of cars. A "desired trajectory" should also be defined for each data point, but this in and of itself is problematic due to the vague nature of, e.g., what is the optimal trajectory for avoiding an obstacle.

 Reply Reply to Comment
Collapse Subdiscussion
Sundari Devulapalle
Sundari Devulapalle
Sep 30, 2025Local: Sep 30, 2025 at 11:08pm<br>Course: Sep 30, 2025 at 10:08pm
Problem Statement

The problem I selected in the previous section was detecting suspicious financial transactions, particularly those indicative of money laundering. The dataset is hypothetical, combining payment transaction data from the bank’s internal systems, client onboarding/KYC records, account activity logs, and external sources such as sanctions lists, PEP watchlists, and material negative news. The target variable indicates whether a transaction is suspicious or not.

Probabilistic Setting
In theory, each financial transaction that a client gets involved in, can be treated as a sample drawn from a probability distribution of financial activity. In practice, this assumption may not be entirely true as transactions from the same client or fraud network are often correlated rather than independent (eg: a series of small value transactions). In addition to the correlated activity, labels based on Suspicious Activity Reports (SARs) may be incomplete. Resampling would help mitigate this risk to some extent. 

Stationarity
The data is not fully stationary. Fraud patterns always evolve as criminals get more creative, and normal client behaviour also shifts due to seasonality (e.g., holiday spending). This shift means what once was used to predict fraud could no longer be used reliably. To mitigate this, models would require regular retraining, monitoring for change in activity, and possibly time-series features to handle seasonality.

A Priori Knowledge
A priori knowledge on money laundering is rare and labeled data is not available. However, there is domain knowledge to guide model design. Regulators provide clear guidelines on suspicious activity, and prior research highlights relevant features such as transaction speed, unusual geographies, and round-number payments. As mentioned earlier, a SAR event by itself does not guarantee fraud transactions that those are the best proxy available for detection of fraud. Evaluation should focus on recall (catching true cases) while managing false positives.

Revising the Data or Problem
If assumptions are not met, I would:

Revise the dataset: aggregate features at the client or network level, engineer features like transaction frequency, and apply imputation for missing KYC data.

Reframe the problem: complement supervised learning with anomaly detection to capture new fraud patterns

Based on the above, while not all the assumptions hold good strictly, by carefully handling the sample datasets and by building probabilistic models that combine adaptive practices, one can ensure models remain practical and effective. 

 Reply Reply to Comment
Collapse Subdiscussion
Inderpal Tiwana
Inderpal Tiwana
Oct 1, 2025Local: Oct 1, 2025 at 5:12pm<br>Course: Oct 1, 2025 at 4:12pm
Problem & Overview

Capacity Planning on IT systems such as Kubernetes, the aim was to build a model which could use historical and live data to predict when a platform would need additional scale and rightsize accordingly based on those demands/outcomes

 

Probabilistic Setting

The data can be assumed to be taking independent samples when looking at a singular metric e.g. platform consumption, date, number of users and all datapoints have the ability to be treated as independent, however when looking at this as a larger picture and at scale or emergency events these metrics can be correlated and seen to be related and no longer independent, e.g. data centre failures and the subsequent recovery events which can cause sprawl and metrics/features to be seen to be correlated e.g. storage consumption on particular infrastructure and logs, node capacity decrease etc...

 

Stationarity

A broader look would indictate the properties the problem to be violated and not remain stable over time due to business focus shifts where platform consumption/usesage can shift dramatically, additionally there can be some seasonal events which both spike and reduce the useage of the platform suce as winter events which cause less developers to use, additionally sales/christmas/payday(sector dependent) can all trigger spikes in users. In some cases the noise can possibly be reduced, with possible retraining to mitigate some of this.

 

A Priori Knowledge

Domain Knowledge exists for this problem experts exist across organisations collecting data for their environment's, whilst I myself have the ability to understand these features due to my own experience working in the field. Which would all indicate the sme knowledge could be leveraged to create more meaningful features and in time develop the model further to provide more accuracy and greater predictions.

 

If Assumptions are not met

Revise the dataset, add new features, impute the data as needed, helping to reduce the noise and any outliers in the datasets, additionally reframe the problem, rather than tackling the problem as a whole, target individual problems and look at it with a micro lense, e.g. users on a platform, applications this will reduce the number of features being used and simplify the problem until the many smaller problems can be used to take a holistic view

 Reply Reply to Comment
Collapse Subdiscussion
Craig Dawson
Craig Dawson
Oct 1, 2025Local: Oct 1, 2025 at 5:41pm<br>Course: Oct 1, 2025 at 4:41pm
Briefly describe the ML problem you selected, the data set and its source (real or hypothetical).

I work on ships and a key task every day is to keep a log of timings which summarise the activities that occur on that day such as the moving of equipment on deck. This task is typically done manually but CCTV / ML could be used to automate the process. High-quality images of the relevant equipment would be required, sourced from existing footage. The key input variables are the images and also perhaps a co-ordinate system that can be referred to to determine what specific operation is being performed when the items of equipment are being moved. The source of the data is real and not hypothetical. The main target outcome variables are timings which summarise the timings of each activity. This is a classification problem as we are not trying to make any predictions but are trying to classify items and record information related to them.

Probabilistic setting: does your data set represent samples drawn independently from a fixed (but possibly unknown) probability distribution? Justify your answer with evidence from the data set or problem domain.

CCTV footage will normally not be drawn from a fixed probability distribution. The footage is typically captured continuously meaning that adjacent frames are correlated which limits the independence that each point of data (each frame) has. Also, the objects in each frame will interact and be dependant on one another as the occurrence of one event will typically result in the occurrence of another separate event.  

Stationarity: are the statistical properties of the data (e.g. distribution, feature relevance) expected to remain stable over time or across the application environment? Explain any concerns if trends, seasonality or domain shifts might affect stationarity.

The stationarity is likely to not remain constant over time. There are a large number of potential sources of non-stationarity that include lighting changes, differing camera angles, differing weather and changes in time of day / night. If the model is not trained to recognise objects in both daylight and darkness then it may falter. Therefore, it would be important to ensure that the model is trained appropriately.

A priori knowledge: do you have sufficient domain knowledge or context to guide model design (e.g. features, labels or evaluation metrics)? Mention any existing benchmarks, feature relevance insights or prior research.

By making use of a co-ordinate system which links to the ship's deck the available domain knowledge could be improved, similar to a pose estimation. The model could be set up to only detect objects in specific regions of the ship's deck during normal movements. The objects which are to be tracked can be labelled correctly and supervised learning can be used to ensure the objects are being tracked correctly. To aid in this effort labelling strategies can be used such as frame-level, clip-level and event-based. An existing benchmark system seems to be the DiVA system.

How would you revise the data set (e.g. re-sampling, feature engineering or filtering)?

To minimise temporal dependence recording CCTV footage frames at wider intervals could be a good idea as this may reduce autocorrelation. To improve the stationarity problem grayscale filters could be used to minimise the variance of daytime / night time footage and the model could be trained accordingly on grayscale imaging. 

How would you reframe the problem (e.g. redefine the target, split into sub-problems or choose a different learning goal)?

The use of sub-problems such as robust object detection and lightweight tracking would likely be beneficial.

 Reply Reply to Comment
Collapse Subdiscussion
Alex Llewelyn
Alex Llewelyn
Oct 1, 2025Local: Oct 1, 2025 at 8:31pm<br>Course: Oct 1, 2025 at 7:31pm
Summary of Problem & Dataset
Building a diagnostic model for prostate cancer using urine/semen mRNA expression + PSA + clinical attributes (age, BMI, smoking, family history). Labels: cancer status and stage. Dataset is prospective, gathered in a dedicated protocol with standardised analytics.

Probabilistic Setting
Selection bias: Men with high PSA scores are more likely to have had a biopsy and therefore have a verified cancer status. Performing a biopsy on a man without specific  cancer indicators would be unethical, meaning cancer status must be imputed for such individuals (assume no cancer), which could introduce bias.
Site: If some data are collected at different hospitals this could be with different equipment or operators and could introduce bias into the data. If cancer status is correlated with site (e.g., socio-economic factors) this could lead to errors in the model
Demographics: Age/ethnicity/co-morbidity may not match wider population, especially in the control group as healthy volunteers for trials are often not representative

Stationarity
Changes to screening and treatment practices, lifestyle factors, comorbities, immigration, and an ageing population could all cause the distribution to shift over time.

A Priori Knowledge
Several urine and blood markers for prostate cancer are well-established in scientific and clinical literature. Broader understanding of relevant molecular pathways means a curated set of plausible markers can be assembled from existing literature. Commercial tests are available that could provide feature priors and benchmarks.
The clinical objective is for the detection of clinically significant prostate cancer. Expert clinical appraisal of model results could help to refine the parameters and thresholds to ensure the output variable is clinically useful.

If Assumptions Fail
Ensure diverse demographic representation is present across different PSA levels, e.g. enforce > 20% non-white if in a UK context. Oversample under-represented groups by weighting data appropriately.
Consider non-invasive techniques such as MRI biopsies. Consult with ethical bodies to determine appropriateness of conducting prostatecomies in healthy volunteers in test set.
Use repeat collections to determine variability within individuals
Work with clinicians to develop ways of classifying clinical significance (e.g., none, low, high) instead of standard cancer stage grading, which has more noise and could be imbalanced. Alternatively, a continuous risk score could be used, allowing clinical bodies to make their own judgements on appropriate thresholds for medical decision-making.
Perform tests excluding individual sites to see if the model is substantially impacted
Population drift: Continuous monitoring of post-deployment test results and clinical outcomes will help to ensure the model remains sensitive and specific.

 Reply Reply to Comment
Collapse Subdiscussion
Prakasha Gourannanavar
Prakasha Gourannanavar
Oct 1, 2025Local: Oct 1, 2025 at 11pm<br>Course: Oct 1, 2025 at 10pm
In my earlier assignment, I chose predictive IT system monitoring. The goal is to predict IT failures before they happen in critical environments like airlines or labs, where even small issues can cause major disruptions.

The data comes from several sources:

System metrics like CPU, memory, disk usage, and network latency.

Application logs with errors, exceptions, and response times.

Historical incidents, including outages and recovery times.

Environmental factors like temperature, power fluctuations, and maintenance schedules.

User activity patterns tied to operations.

Based on my understanding, I looked at the key assumptions for using probabilistic ML:

Probabilistic setting: The data mostly represents samples from the system’s underlying state distribution. But events aren’t fully independent — CPU spikes often come with memory or network issues, and failures can cascade. Even though it’s not strictly i.i.d., sequence models like RNNs or probabilistic models can handle these dependencies.

Stationarity: System behaviour isn’t always stable. Updates, hardware changes, or seasonal workload spikes (like peak travel for airlines) can shift the data patterns. This means the model trained today might not work as well months later. To manage this, retraining on recent data, sliding windows, or drift detection would help.

 A priori knowledge: There’s strong domain knowledge. IT teams track key metrics (like CPU above 90% for long periods), and past incident logs help link features to outcomes. Plus, research in AIOps and log anomaly detection provides useful benchmarks. This makes feature selection and evaluation more manageable.

Based on the above, predictive monitoring is feasible but requires extra care. Using sequence-based models, retraining for concept drift, and starting with anomaly detection when labels are limited are good first steps. Human-in-the-loop feedback can also improve accuracy over time.

Overall, this problem is practical and could really help IT teams move from reactive fixes to proactive monitoring, preventing downtime and improving reliability.

 Reply Reply to Comment
Collapse Subdiscussion
Neetam Limbu
Neetam Limbu
Oct 2, 2025Local: Oct 2, 2025 at 8:57am<br>Course: Oct 2, 2025 at 7:57am
ML problem

Predicting whether a stock’s price will increase or decrease the next day based on historical market data.

Data Set

A hypothetical dataset containing daily stock information for 500 publicly traded companies over the past 10 years. Each record includes:

Open, high, low, close prices
Trading volume
Technical indicators (e.g., RSI, MACD, moving averages)
Market sentiment scores from news headlines
Source

The data is simulated to resemble real-world financial feeds, combining:

Historical price data from Yahoo Finance
Sentiment scores derived from a hypothetical NLP model trained on financial news
Probabilistic Setting

Assumption: Samples are drawn independently from a fixed (but possibly unknown) probability distribution.
Evaluation:
In theory, daily market data (e.g., open, close, volume) can be treated as samples from a stochastic process.
However, true independence is violated due to autocorrelation and temporal dependencies for example today’s price is influenced by yesterday’s.
The distribution may also evolve over time due to macroeconomic shifts, policy changes, or market sentiment.
Conclusion: This assumption is partially valid if we model the data as a stationary time series with weak dependencies, and care must be taken to account for autocorrelation and independent and identically distributed (non-i.i.d.) behavior.

Stationarity

Assumption: Statistical properties of the data remain stable over time.
Evaluation:
Financial markets are not strictly stationary. Trends, seasonality (e.g., earnings cycles), and regime shifts (e.g., bull vs bear markets) affect feature relevance and distributions.
Technical indicators may behave differently in volatile vs stable periods.
Concept drift is a real concern i.e., models trained on past data may degrade if market dynamics change.
Conclusion: Stationarity is weak. Models must be validated with walk-forward testing, and retraining should be considered to adapt to evolving conditions.

A Priori Knowledge

Assumption: Sufficient domain knowledge exists to guide model design.
Evaluation:
Financial modeling benefits from rich domain knowledge:
Feature engineering: Indicators like RSI, MACD, Bollinger Bands are well-established.
Labels: Binary movement (up/down) is a common framing, though more nuanced targets (e.g., volatility, returns) exist.
Benchmarks: Widely used baselines include logistic regression, ARIMA, and LSTM models.
Research: Extensive literature supports hybrid models, ensemble methods, and sentiment integration.
Conclusion: Strong a priori knowledge supports informed model design, feature selection, and evaluation.

If assumptions are not satisfied

Revise the Dataset:

If i.i.d. (independent and identically distributed) assumption is weak (e.g. autocorrelation, temporal dependence):

Use lag features: Include past values (e.g. previous day’s close, volume) to capture dependencies.
Time-aware sampling: Avoid random shuffling and use walk-forward splits or rolling windows.
De-trend or normalize: Apply differencing or log returns to reduce autocorrelation and stabilize variance.
 If stationarity is violated (e.g. regime shifts, seasonality):

Segment data by market regimes: Train separate models for bull, bear, or sideways markets.
Include regime indicators: Add features like VIX, interest rates, or macroeconomic flags.
Apply rolling retraining: Periodically update the model with recent data to adapt to drift.
If domain knowledge is limited:

Feature engineering from literature: Use well-known indicators (RSI, MACD, Bollinger Bands).
Incorporate sentiment data: Extract features from news, earnings reports, or social media.
Benchmark against naive models: Compare to moving average or momentum strategies to validate signal strength.
Reframe the Problem:

If predicting price direction is unstable:

Switch to regression: Predict log returns or volatility instead of binary up/down.
Use probabilistic outputs: Frame as likelihood of movement rather than hard classification.
If the task is too noisy:

Split into sub-problems:  
Predict volatility first, then direction.
Cluster stocks by behavior before modeling.
Focus on ranking: Predict relative performance (e.g. top 10% gainers) instead of absolute movement.
If labels are unreliable or delayed:

Use proxy targets: Like intraday momentum or volume spikes.
Frame as anomaly detection: Spot unusual patterns rather than predict exact outcomes.
 Reply Reply to Comment
Collapse Subdiscussion
Jay Hopkins
Jay Hopkins
Oct 2, 2025Local: Oct 2, 2025 at 10:24am<br>Course: Oct 2, 2025 at 9:24am
The problem that I addressed was exploration of an ML model that could predict whether an underwriter will quote a risk, and if yes, the limit of liability that they are willing to offer and the policy pricing. This was proposed using both structured and unstructred data. 

Structured: Claims history, policy tenor, requested pricing, requested limit of liability, requested deductible / excess and then the insurers existing aggregate exposures by sector, industry and geography.  

Unstructured: engineering reports and expert opinions. 

1. Probabilistic Setting: not strictly. You often observe price / limit only when the underwriters decision is yes. Non quotes risks would typically lack indication of pricing and limit. Portfolio capacity and peer behaviour (the London specialty insurance market operates on a lead and follow basis) may create dependancies across submissions. Appetite and capacity at the time of underwriting review affects the decisions, so creates a dependancy and not a fixed distribution. 

 

2. Stationarity: quite weak. There are insurance market cycles (hard and soft markets) where appetite and pricing change based on historical claims performances. Additionally, given each insurer is running their own portfolio with their own individual claims records, their appetites can change independently of one and other. Finally, there are regulatory changes that impact product demand. For example, the PRAs paper CP16/18 implemented new regulatory capital requirements, meaning banks could use insurer credit ratings to offset their portfolio borrower credit ratings if they toook out insurance to reduce their regulatory capital requirements. 

 

3. Domain knowledge: Yes. I have worked in the insurance market for over 8 years in claims, underwriting, broking and technology. There are several firms that build out ML models for the industry to aid actuarial pricing. 

If any of the above assumptions change, I would revise the dataset. I would de-bias the dataset by including all submissions (not just those that were quoted). I would also reframe the problem into a two stage model - quote likelihood (yes vs. no) and then conditional models for pricing. 

In summary, I think the opportunity for this model is high with a time-aware, two stage approach that counters selection bias and models the portfolio state of play. I will need to address model limitations through data design, evaluation and continuous recalibration. 

 

 Reply Reply to Comment
Collapse Subdiscussion
Waqas Zubairy
Waqas Zubairy
Oct 2, 2025Local: Oct 2, 2025 at 12:57pm<br>Course: Oct 2, 2025 at 11:57am
ML Problem and Data
The problem I worked in previous module was related to Wealth Management related data. its is about  predicting portfolio returns and/or classifying customers based on investment behavior in a wealth management setting. The major aim is to to give recommendations and risk-aware portfolio optimization.

Data and Sources (hypothetical but based on real systems):

Customer-level data: demographics, income, net worth, risk tolerance (CRM – Salesforce is our main CRM system which we used in our company).

Account/transaction data: historical trades, dividends, fees, portfolio composition (Avaloq portfolio management system - This is the system which company maintains for trades).

Market/product data: stock prices, interest rates, indices (News APIs).

External/economic data: These factors are very subjective in my opinion, for example inflation rates, sector performance, financial news sentiment etc

Key Assumptions

Probabilistic Setting
In my opinion, customer behaviour and market data can be treated as samples from underlying probability distributions. However, I am not sure about independence. Customer investment choices may be correlated (e.g., herd behaviour during market downturns), and market prices are not. but it can be influenced by some dependencies and shocks. Thus, while the probabilistic setting is partly satisfied, temporal and correlation effects must be modeled (e.g., time-series methods, autoregressive features).

Stationarity
This assumption is more problematic. Financial markets exhibit non-stationarity due to seasonality, economic cycles, and sudden events (e.g., interest rate changes, geopolitical crises). Likewise, customer preferences evolve (risk tolerance changes with age or life events). Feature relevance may shift—for example, during volatile periods, diversification features matter more than past returns. all of these factors  violates strict stationarity. Models would need frequent retraining and monitoring for concept drift to remain accurate.

A Priori Knowledge
We do have substantial domain knowledge to guide model design. Wealth management research provides established metrics (Sharpe ratio, risk-adjusted return), known customer segmentation schemes, and evaluation benchmarks (e.g., RMSE for return prediction, accuracy/F1 for classification). Financial regulations and investment theory also provide strong context for selecting features and targets. Prior studies in financial machine learning (e.g., portfolio optimization with ML) further support design choices. Thus, this assumption is reasonably satisfied.

Addressing Assumption Violations

Probabilistic Setting (correlations, dependencies):
Incorporate time-series models or graph-based approaches for networked dependencies. Ensure training/validation splits respect temporal order to avoid data leakage.

Stationarity (concept drift):

Retrain models periodically with recent data.

Use adaptive methods (online learning, drift detection techniques).

Reframe the problem to shorter-term forecasting windows, which reduces exposure to long-term distribution shifts.

A Priori Knowledge:
If insufficient, collaborate with domain experts (e.g., financial analysts) to validate features. Use feature importance methods (e.g., SHAP values) to ensure interpretability. Benchmark against simple financial baselines (e.g., buy-and-hold return) to validate improvements.

Conclusion
The problem of predicting portfolio returns or classifying customer investment behavior is well-supported by available data and strong domain knowledge. However, independence and stationarity assumptions are not fully satisfied due to correlations in customer actions and the non-stationary nature of financial markets. These issues can be mitigated by adopting time-series–aware models, careful validation strategies, and continuous retraining. With these adjustments, machine learning can provide practical value in wealth management decision support.

 Reply Reply to Comment
Collapse Subdiscussion
Roshan Jayakumar
Roshan Jayakumar
Oct 2, 2025Local: Oct 2, 2025 at 1:18pm<br>Course: Oct 2, 2025 at 12:18pm
The machine learning problem involves predicting urban traffic congestion levels to enable proactive traffic management and reduce congestion. The data set consists of historical traffic sensor readings collected from multiple locations in a city, including traffic volume, average vehicle speed, and time-of-day indicators. Additional contextual data such as weather conditions and public event schedules may also be included. The data source is real, gathered from city traffic sensors and public APIs for weather and events.


1. Probabilistic Setting
The data consists of samples collected over time from a complex system where independence doesn’t fully hold. Traffic readings at different times and places are linked—traffic at one sensor often depends on conditions upstream or earlier moments. So, strictly speaking, the data points aren’t independent and identically distributed (i.i.d.). However, for many machine learning models, it’s reasonable to treat them as if they come from an underlying distribution that may change over time.

Supporting this, analyses of time series usually show clear dependencies, and nearby sensors tend to have related patterns. Still, since the data is gathered continuously and covers a broad timeframe, it effectively represents the overall traffic behavior in the city during the observed period.

2. Stationarity
The statistical patterns in traffic data usually change over time. Daily routines like rush hours, weekly differences between weekdays and weekends, and seasonal factors such as holidays or weather all have a big impact on traffic. On top of that, changes to infrastructure like road repairs or new routes, along with unexpected events like accidents, can shift the traffic patterns. This lack of stability makes it harder for models to generalize, especially when the training data doesn’t match future conditions. Approaches like training on recent time windows, accounting for seasonal effects, or using adaptive learning methods can help address these challenges.

3. Priori Knowledge
We have plenty of domain knowledge to help guide the modeling process. Features like time of day, day of the week, weather conditions, and how sensors relate to each other spatially all play a role in traffic patterns. The labels, such as congestion levels or vehicle speeds, can be measured and validated using other data sources like travel time reports. Common evaluation metrics include Mean Absolute Error, Root Mean Squared Error, or accuracy when classifying congestion levels.
If Assumptions Aren’t Met

Adjusting the Data

Re-sampling: Apply methods like sliding windows or time-based cross-validation to better handle time dependencies and prevent data leakage.

Feature engineering: Add lagged variables, moving averages, or calendar-based features to explicitly capture trends and seasonal patterns.

Filtering: Remove outliers caused by sensor glitches or rare events if they’re not relevant to the prediction goals.

Reframing the Problem

Break it down: Separate the task into short-term and long-term forecasts or focus on specific regions to simplify the problem.


Conclusion
Predictive traffic management is an interesting but complex machine learning problem because of time and location-based dependencies and changing data patterns. Although the data isn’t completely independent and shows shifts over time, thoughtful data preparation and clear problem framing backed by solid domain expertise make it possible to build effective models that help reduce city traffic congestion.

 Reply Reply to Comment
Collapse Subdiscussion
Bruce Diesel
Bruce Diesel
Oct 2, 2025Local: Oct 2, 2025 at 3:32pm<br>Course: Oct 2, 2025 at 2:32pm
The ML problem I idnetified in 2.1 was the forecasting of cash demand and optimisation of replenishment strategy for ATMs.  

Probablisitic Setting: the probability distribution of the data samples is unknown, but adheres to consistent weekly, monthly and yearly cycles.  However, there are regularly outlier events that can cause significant spikes, such as public holidays, or events (e.g. a football match).  The effect of these events, though, can be predicted.

Stationarity: yes, statisticial propoeraties remain stable and have done so over many years. The challenge is the impact of external events on the data and being able to account for them in the historical data. 

A Priori Knowledge: yes, this task has been perfomed manually for many years by cash forecasting staff in banks.  Singificant heuristics have been developed by these people to improve their predictions. 

 Reply Reply to Comment
Collapse Subdiscussion
Aliaksandr Masny
Aliaksandr Masny
Oct 2, 2025Local: Oct 2, 2025 at 4:17pm<br>Course: Oct 2, 2025 at 3:17pm
1. Brief description of the machine learning task
The task is to predict the rate of cognitive decline in patients with Alzheimer's disease. This is a supervised learning task, specifically regression prediction, where the target variable is a continuous numerical value. The data to be used is expected to be real longitudinal clinical data from various sources.

2. Assessment of key assumptions
Probabilistic formulation:
This assumption is partially correct. Data for each patient can be considered independent, as the course of the disease in one person does not affect another. However, if data is collected from different data providers, the assumption of random distribution may be violated. On the other hand, differences in data collection protocols, equipment, and patient demographics between centers can lead to systematic discrepancies in the data.

Stationarity:
This point causes me the greatest concern. Diagnostic criteria, treatment standards, and visual data acquisition technologies (MRI/PET) are constantly improving. This means that a model trained on old data may perform worse with current patient data. 

This means that a model trained on old data may perform worse with current patient data. It would seem that the biological processes underlying Alzheimer's disease should be static, but practice shows that hypotheses about the root cause of the disease are constantly changing over time, with new hypotheses emerging that lead to the collection of other, new data from patients.

A priori knowledge:
This assumption is valid. There is a vast amount of prior knowledge in this field that can guide model development.

Evaluation metrics: Regression tasks have standard metrics such as MSE.

Benchmarks: There are numerous scientific publications with results from both statistical and ML models that can be used for comparison.

Significance of features: Decades of research have confirmed the importance of variables such as amyloid and tau protein levels in CSF, as well as hippocampal atrophy, as key predictors of the disease.
3. Solving problems with assumptions
Since assumptions about probability (in terms of identical distribution) and stationarity may be violated, the following steps are required:

Review the data set:
To solve the problem with data from different sources, it is necessary to carefully normalize and standardize all variables to bring them into uniformity.

Data filtering can be applied, for example, limiting the sample to patients diagnosed within a certain time period (e.g., over the last 10 years, or within the framework of a certain theory of the onset, development, and course of the disease) to reduce the impact of non-stationarity.
Feature engineering to create new features that may be less sensitive to changes in protocols.
Reformulating the task:
Instead of creating a single global model, the task can be broken down into subtasks. Then, by training separate models for each data source, we will obtain less divergent model predictions.
To cope with non-stationarity, we can reformulate the goal from creating a static model to developing a dynamic system (if possible) that will have to be constantly retrained and adapted as new patient data becomes available.
 Reply Reply to Comment
Collapse Subdiscussion
Jose Arturo Michel Rodriguez
Jose Arturo Michel Rodriguez
Oct 2, 2025Local: Oct 2, 2025 at 5:17pm<br>Course: Oct 2, 2025 at 4:17pm
The problem defined in module 2 is about predicting the performance of football players given their past performances. 

Probabilistic setting: does your data set represent samples drawn independently from a fixed (but possibly unknown) probability distribution? Justify your answer with evidence from the data set or problem domain.
Yes. The performance measured on a player-contribution scale could be drawn from a distribution of the factors that make up the performance. For example the number of minutes played, the player's position, the number of completed passes, the number of assists. All of these come from a distribution made up the values of all the players.

Stationarity: are the statistical properties of the data (e.g. distribution, feature relevance) expected to remain stable over time or across the application environment? Explain any concerns if trends, seasonality or domain shifts might affect stationarity.
Football is the most widely played game in the world. Given enough samples the parameters of the distribution are robust and stable. However the evolving play styles could cause the distribution to shift overtime, worth noting that the play style could be very different from one league to another. A model could be developed for each league and a global model to compare the differences.

The evolving play style could affect the performace of the model over time. 

A priori knowledge: do you have sufficient domain knowledge or context to guide model design (e.g. features, labels or evaluation metrics)? Mention any existing benchmarks, feature relevance insights or prior research.
Having a broader understanding of the feasability of ML. I don't feel confident that a useful model can be developed for this problem. There are too many unknowns including data sources and reliability of available data. 

 Reply Reply to Comment
Collapse Subdiscussion
Priyanka R Daswani
Priyanka R Daswani
Oct 2, 2025Local: Oct 2, 2025 at 5:28pm<br>Course: Oct 2, 2025 at 4:28pm
My original idea—shared on 10th Sept 2025 in Self Study Discussion 2.1 and further developed on 11th Sept 2025 in Required Discussion 2.1—involved forecasting the sales and success of new product initiatives/launches, which arise from innovation. However, the creative nature of such launches can pose challenges to stationarity, as they may not follow predictable patterns based on past data. Given this ML limitation, I’ve chosen to pivot toward a problem more clearly aligned with the assumptions of a probabilistic learning context for this exercise.

I’m exploring a ranking and recommendation system for consumer products on a shopping platform. The goal is to personalize search results for users based on their past activity—such as browsing behavior, purchases, and engagement history—to improve relevance and conversion.

Dataset (Hypothetical but realistic)

The dataset consists of anonymized user sessions capturing product views, clicks, ratings and purchases, along with product metadata (e.g., category, price, brand). Each user interaction is timestamped and associated with a user ID. The problem is to rank products in order of relevance for each user.

Probabilistic Setting

The data can be viewed as samples drawn from a fixed (though complex) probability distribution over user preferences and behavior. Each user’s interactions reflect the likelihood of product relevance given the user context.

Stationarity

Since the ranking is based on past behavior, and consumer interests tend to evolve gradually (especially within specific categories), stationarity can be assumed over shorter time windows. To mitigate longer-term shifts (e.g., seasonal trends or new releases), periodically retrain the model.

A Priori Knowledge

In consumer recommendation systems, there is a benefit from strong a priori knowledge:

Users tend to repeat purchase behavior (e.g., brand loyalty)
Certain product features (e.g., price, popularity, reviews, ratings) correlate with click-through and conversion
Well-established metrics can guide evaluation
Prior research from e-commerce platforms, competitions and academic literature (eg: collaborative filtering techniques) provides tested baselines and feature engineering strategies.

If assumptions are challenged:

If stationarity weakens (e.g., new product introductions or new users):
For cold-start users: Use available demographic features and start with popular or trending items.
For cold-start items: Use content-based filtering or similar item related properties. The item could also be shown to a random sample of users first to gather initial feedback.
If there is drift, use monitoring and adjust accordingly.
Edited by Priyanka R Daswani on Oct 2, 2025 at 5:35pm
 Reply Reply to Comment
Collapse Subdiscussion
Manuel Ruiz Prado
Manuel Ruiz Prado (He/Him)
Oct 3, 2025Local: Oct 3, 2025 at 5:04am<br>Course: Oct 3, 2025 at 4:04am
The problem I identified earlier was forecasting and optimizing cloud resource utilization using telemetry data from Azure Monitor, Application Insights, and Kubernetes logs. Inputs include CPU and memory usage, storage activity, network throughput, user counts, and historical cost reports. The output is recommended resource allocation (e.g., VM size or Kubernetes scaling). This is a supervised regression problem on time-series data.

Probabilistic Setting
Telemetry logs can be viewed as samples from an underlying distribution of workload behaviors. Strict independence does not hold because system metrics are autocorrelated (high CPU today often implies high CPU in the next time step). However, treating these as draws from a stochastic process is a common and workable assumption in time-series modeling.

Stationarity
Stationarity is more problematic. Workloads fluctuate due to business cycles, product launches, or pricing changes. Short-term local stationarity is plausible, but long-term drift and seasonality must be addressed. I would use detrending, seasonal adjustments, and rolling retraining to keep models current. Monitoring for drift is also essential since yesterday’s workload patterns may not predict tomorrow’s.

A Priori Knowledge
There is strong domain knowledge to guide model design. CPU and memory usage strongly correlate with scaling needs, and user activity often drives demand spikes. Cost data provides clear labels for efficient versus wasteful allocation. Prior research on cloud autoscaling offers benchmarks and evaluation metrics such as utilization efficiency and cost reduction.

If Assumptions Fail
If independence is too weak, I would resample data into coarser intervals. If non-stationarity dominates, I would add time-based features or use models designed for evolving distributions (e.g., LSTMs). If domain knowledge proves insufficient, I would reframe the problem into sub-tasks (e.g., CPU versus storage prediction).

Conclusion
While assumptions are only approximate, careful feature engineering, retraining, and domain insights make the problem feasible in a probabilistic learning context.

 Reply Reply to Comment
Collapse Subdiscussion
Zohreh Kolaei
Zohreh Kolaei
Oct 7, 2025Local: Oct 7, 2025 at 2:04pm<br>Course: Oct 7, 2025 at 1:04pm
Objective: To develop a machine learning model capable of accurately classifying dental X-ray images as either healthy (normal) or decayed

 

1. Probabilistic Setting

In this project, we assume:

X is the image (input features: pixels, textures, etc.).
Y is the label (0 or 1).
The model is learning to estimate the conditional probability:
P(y=1∣x)
for an unseen image.
Using Logistic Regression or Convolutional Neural Network, the model gives the probability of belonging to a class by using sigmoid function.

 

2. Stationarity

Stationarity means the data-generating process doesn’t change over time or across samples. In this setting:

We assume the joint distribution P(X, Y) is stationary:
The relationship between images and labels stays consistent across training and test data.
Model performance may drop in non-stationary data, like if lighting or backgrounds changes and if different x-ray machines was to be used to collect the data.
 

3. Prior Knowledge

Prior knowledge is about what we already know or assume before seeing any images.

In neural networks, we don’t define any priors (like in Bayesian models), but we can define prior knowledge in other ways:
In convolutional neural network for images we might assume local patterns
Using data augmentation, we assume that rotation or flipping doesn’t change the class.
Choosing architectures and strategies based on known properties of images.
Since this is a classification problem, we can tune the hyperparameters using the validation set and evaluate the model using accuracy, confusion matrix, F1 score, Recall and Precision on the test set which the model hasn't seen.
 Reply Reply to Comment
Collapse Subdiscussion
Justin Boynton
Justin Boynton
Oct 9, 2025Local: Oct 9, 2025 at 7:49am<br>Course: Oct 9, 2025 at 6:49am
The problem I selected was determining the likelihood of a software development project running over time based on the features of the project and the resources working on it. The data is sourced from Jira, a software development PM tool used by development teams and broadly contains software features and tasks with time estimates, start and end dates, time entries (hours worked) and delivery date, along with allocated resources to that feature/task. A typical agency might have 20-30 of these projects each year. Each feature or task is tagged with a complexity level (low, medium, high).

 

Probabilistic setting: The data does not strictly represent independent examples from a fixed probability distribution due to:

Time dependencies between tasks in the same project, so if one task overruns, it indicates issues that impact the following tasks in the project. These issues can include poor estimation and resource constraints.
There are typically dependencies between resources, as the same developers may be working on multiple projects simultaneously.
There will be clustering at the project level as they will share common characteristics.
The number of projects for a single agency may not be enough to mitigate the effect of individual projects sharing common characteristics.
Overall, the current data set doesn’t adhere to the i.i.d. principle fully, which could lead to overconfident predictions and poor generalisation.

Stationarity: Again, the data here is not really stationary. There are a number of factors that contribute to this:

Learning effects:  teams get better over time at estimation accuracy during a project.
Snowballing: early delays can and do lead to further delays. Conversely, confidence in the problem domain during the project can improve efficiency later on.
Team changes over longer time periods, e.g. developer skills improvements, new team members, resource allocation.
Seasonality: the summer quarter tends to see more holidays and, therefore, significant pressure on resourcing.
A Priori knowledge: There is evidence that we have strong domain expertise contained within the problem statement, including feature relevance through tags, estimations, and historical time to complete tasks by resource. 

We have a clear target of predicting the actual delivery date vs the planned and historic data for this. There are some existing benchmarks, including COCOMO models and industry reports on project success rates, as well as analogies with other work in the predictive project analysis space.

I am not aware of any industry standard benchmark datasets for this problem.

To address some of the mentioned issues, we could revise our data set by:

Improving sampling: use time-based train/test splits rather than random to keep the temporal ordering and keep one full project out of the dataset for testing generalisation.
We could aggregate features up to the project level, e.g. average complexity, team size and capability, total estimated hours, and use these as features.
We could improve stationarity by retraining the model every quarter, using the previous two years of data up to that point.
We could augment the data with more information to give indicators for developer skill level, for example.
We could also choose to reframe the problem, e.g trying to detect tasks/features within a project that are likely to cause an overrun.

We would also consider model types that are more suitable for non-strict i.i.d. data, such as Random Forests and Gradient Boosting.

 Reply Reply to Comment
Collapse Subdiscussion
Mariano Capezzani
Mariano Capezzani
Oct 11, 2025Local: Oct 11, 2025 at 4:49pm<br>Course: Oct 11, 2025 at 3:49pm
My problem is related to predicting whether a storm cell will reach a customer’s location and if so, estimating its arrival time, speed, and intensity. This prediction could help users of our weather apps make safer, more informed decisions when severe weather is developing nearby.

The setting is most definitely probabilistic, given we have no control over weather patterns and they respond to inherently stochastic behaviors. These are complex systems, and while certain features like direction and velocity are measurable, their evolution is subject to random influences. However, in a probabilistic sense, we can estimate likelihoods and confidence levels of impact based on past patterns.

That said, the data isn’t strictly IID (independent and identically distributed). Storm cells are spatially and temporally correlated—one radar frame or time step often influences the next, and nearby cells can behave similarly. So, to make this assumption more valid, we’d need to design our splits carefully (for example, by storm system or date) so the same event doesn’t appear across training and validation sets.

The data is partially stationary, but not entirely. There are known seasonal patterns, like thunderstorms are more frequent in summer, or certain regions experience stronger winds, and overall storm characteristics change throughout the year.  But there are also non-stationary elements. Radar coverage evolves over time, climate patterns change, and the geographical distribution of severe weather events can shift. This means the statistical properties of the data might drift, so a model trained on one period or region may underperform when applied elsewhere. To handle this, we might need to retrain models periodically, or include features that encode seasonality and region explicitly.

We do have strong domain knowledge to design the model. Our meteorologists already understand which parameters are meaningful, features like storm heading, speed, velocity relative to the target, and rotation strength. We also know what success looks like: a probabilistic forecast that provides reliable lead time. These insights can help shape our feature engineering, label definitions, and evaluation metrics.

 Reply Reply to Comment
Collapse Subdiscussion
Urvi Joshi
Urvi Joshi
Nov 13, 2025Nov 13, 2025 at 11:56am
Machine Learning for Band gap prediction | KaggleLinks to an external site.

The ML problem I have selected was based off of my own work during my undergraduate to do with the efficiency of PV cells. Here we want to design a model which can accurately predict the bandgap (which goes on to dictate efficiency) for different polymeric materials. There is however one glaring challenge, my specialty is in solid-state materials whereas this competition focuses on organic molecules. However, due to my experiences with organic chemistry in my undergraduate, I believe I will be able to translate my learning into this competition.

38615 HW5 | KaggleLinks to an external site.

On the other hand there is this one for solid state materials. However, I am unsure of the background of the data and am slightly unsure. I will further investigate (and later decide).

For the first competition:

The data set contains over one million molecules to train on and wants us to determine the homo-lumo gap for all these molecules. Accuracy will be determined based on the root mean squared error. This is a real source, with data coming from DFT calculations - hence there will be noise/error associated with this data (depending on the type of functionals being used and their applicability to modelling specific molecules).

Probabilistic Setting

While the distribution depends on a wide range of factors effecting the molecules, there are probably a handful of factors which dominate the model (so it is important to determine any outliers) and determine the local trends of those factors. So yes, while there is probably a vague fixed probability distribution - I expect it to be quite noisy hence data needs to be cleaned and carefully evaluated.

Stationarity

I think the data is unlikely to stay the same over time - it is more likely to shift according to trends between families of molecules, hence different compounds will be non-stationary. Issues such as extremely different chemical environments, or different effects within the chemical environment could effect groups of materials and break the model. I wonder if there is a method to deal with this and normalise the model (perhaps neural networks to weight them according to families of structures or trends?)

A priori knowledge

I think I have a decent base level knowledge however, I will definitely need to read up on the effects and the contributions of different structures and the mechanics behind the determination of the homo-lumo gap. But I think my existing background will be enough to get the ball rolling.

If assumptions are not met...

Then I will be breaking down the dataset and probably working on the classification or altering the model to work on a smaller subset of molecules. Potentially filter down the data to only specific structures and compositions and evaluating the effect of those on the bandgap and the factors effecting them. 

Edited by Urvi Joshi on Nov 13, 2025 at 12:07pm

<---- Module 2.1 is here --->
 
 
Required discussion 2.1: Determining the feasibility of a machine learning solution - Section A
1515 unread replies.3737 replies.
 Learning outcome addressed
Evaluate the suitability of ML solutions for real-world problems.
   Discussion directions and prompts
Introduction
In the previous discussion, you identified a real-world problem and explored how machine learning might address it. In this activity, you’ll assess whether the problem is a good fit for a machine learning solution. You will define the key components of your problem, reflect on its feasibility and consider how a model could be developed to solve it effectively.

Instructions
Refer back to the unique challenge you selected in Self-study discussion 2.1. Answer the following questions in your post:

What data would you use? 
Identify the type and source of data required to train your model.
What are your key input and output variables? 
Specify the features (input variables) and the target outcome (output variable).
What type of machine learning problem is this? 
Determine whether it is a classification or prediction, supervised or unsupervised, or parametric or non-parametric approach.
What steps would you take to solve this problem through machine learning? 
Outline the general process, referencing the ten-step machine learning pipeline.
What might cause missing data in your data set? 
Identify potential reasons for missing values, and suggest an approach you’ve learned in this module to handle them effectively.
Completion requirements
Reflect on the prompts and submit your responses directly in the discussion board below.
Please keep your responses under 500 words.
Engage with peers by commenting thoughtfully on their posts. 
Consider providing any advice or suggestions you might have to your peers’ questions.
The average completion time for this activity is 60 minutes.

This is a required activity and counts towards the completion of the programme.

There is a rubric associated with this discussion. Select the three vertical dots in the header bar of this text area and select 'Show Rubric' in the dropdown menu. This will display the completion requirements associated with this discussion.

Search entries or author
Search entries or author
 Filter replies by unread      
 ReplyReply to Required discussion 2.1: Determining the feasibility of a machine learning solution - Section A
Collapse Subdiscussion
Laveena Ramchandani
Laveena Ramchandani
Sep 8, 2025Local: Sep 8, 2025 at 3:31pm<br>Course: Sep 8, 2025 at 2:31pm
Problem Assessment: Preventing Use of Outdated Swiss Franc Exchange Rates in RMS

The data that would be useful to drive the scenario explained would be, timestamps, the source and the rates from the source, real-time exchange rate feeds, transaction history, pricing logs, how many tickets/ancillaries sold at that price till the next price change.


Key input and output variable

Input features (X): Current RMS exchange rate, timestamp, historical rate trends, volatility, FX source, prior transaction rates.
Output variable (Y): Binary indicator of “stale/valid” rate or predicted deviation from expected rate. Alternatively, a continuous prediction of expected correct rate for anomaly detection.
Machine learning Problem

Supervised or unsupervised depending on labeling:

Supervised: If historical “stale rate” flags exist, predict likelihood of a rate being outdated.
Unsupervised: Detect anomalies in FX data using clustering or isolation forests when no labels exist.
Predictive analytics : due to previous experience at Deloitte and Easyjet, we could even use this to help us visualise the difference between hard coding a exchange rate vs using the latest one and see how it impacts sales. 
It is important to understand the state of data first, but above ML approach could be used. 

Steps for the process

Define the problem: Prevent revenue miscalculations due to stale FX rates in RMS, as this will allow right pricing to happen and the main issue right now
Collect data: Historical exchange rates, RMS pricing logs, market FX trends, this is available and can be worked with traders in the team
Clean data: Handle missing timestamps, inconsistent sources, or duplicate entries, this is vital as learnt in this module and based on this we can actually drive further results
Explore data: Identify unusual spikes, missing entries, or abnormal trends, try to understand if anomalies are actually a deviated result or not?
Split data: Training, validation, and test sets (if supervised).
Select & Train the model: Fit on historical FX data, tune any parameters, and validate against known anomalies.
Evaluate model: Use metrics like precision, recall, and F1-score for flagged stale rates.
Deploy and monitor: Integrate ML alerts into RMS workflow; continuously retrain as new FX data arrives, as I come from a testing background it would be safe to deploy this into a developer/QA environment before we go live to prevent any live defects leading to customer delays/wrong ticket or ancillary pricing
Potential causes of missing/outdated data could be

Delays in FX feed updates, network interruptions, or manual overrides in RMS
Rare market events not captured in historical data (currently big football matches, big concerts are being captured...)
Approach to handle missing data:

Indicator-based imputation: Flag missing or delayed FX feeds as potentially stale.
Interpolation: Estimate missing rates based on recent historical trends.
 Reply Reply to Comment
Collapse Subdiscussion
Laveena Ramchandani
Laveena Ramchandani
Sep 8, 2025Local: Sep 8, 2025 at 3:41pm<br>Course: Sep 8, 2025 at 2:41pm
Problem Assessment: Preventing Use of Outdated Swiss Franc Exchange Rates in RMS

The data that would be useful to drive the scenario explained would be, timestamps, the source and the rates from the source, real-time exchange rate feeds, transaction history, pricing logs, how many tickets/ancillaries sold at that price till the next price change.


Key input and output variable

Input features (X): Current RMS exchange rate, timestamp, historical rate trends, volatility, FX source, prior transaction rates.
Output variable (Y): Binary indicator of “stale/valid” rate or predicted deviation from expected rate. Alternatively, a continuous prediction of expected correct rate for anomaly detection.
Machine learning Problem

Supervised or unsupervised depending on labeling:

Supervised: If historical “stale rate” flags exist, predict likelihood of a rate being outdated.
Unsupervised: Detect anomalies in FX data using clustering or isolation forests when no labels exist.
It is important to understand the state of data first, but above ML approach could be used. 

Steps for the process

Define the problem: Prevent revenue miscalculations due to stale FX rates in RMS, as this will allow right pricing to happen and the main issue right now
Collect data: Historical exchange rates, RMS pricing logs, market FX trends, this is available and can be worked with traders in the team
Clean data: Handle missing timestamps, inconsistent sources, or duplicate entries, this is vital as learnt in this module and based on this we can actually drive further results
Explore data: Identify unusual spikes, missing entries, or abnormal trends, try to understand if anomalies are actually a deviated result or not?
Split data: Training, validation, and test sets (if supervised).
Select & Train the model: Fit on historical FX data, tune any parameters, and validate against known anomalies.
Evaluate model: Use metrics like precision, recall, and F1-score for flagged stale rates.
Deploy and monitor: Integrate ML alerts into RMS workflow; continuously retrain as new FX data arrives, as I come from a testing background it would be safe to deploy this into a developer/QA environment before we go live to prevent any live defects leading to customer delays/wrong ticket or ancillary pricing
Potential causes of missing or outdated data:

Delays in FX feed updates, network interruptions, or manual overrides in RMS.
Rare market events not captured in historical data.
Approach to handle missing data:

Indicator-based imputation: Flag missing or delayed FX feeds as potentially stale.
Interpolation: Estimate missing rates based on recent historical trends.
Real-time alerts: Ensure critical gaps trigger workflow notifications.
Conclusion:
Machine learning can add a predictive and preventive layer to RMS, identifying potentially stale exchange rates before they impact pricing or revenue calculations. Success depends on integrating historical and real-time FX data, selecting appropriate anomaly detection or predictive models, and ensuring the system can adapt to changing market patterns.

 Reply Reply to Comment (1 like)
Collapse Subdiscussion
Priyanka R Daswani
Priyanka R Daswani
Sep 14, 2025Local: Sep 14, 2025 at 5:31pm<br>Course: Sep 14, 2025 at 4:31pm
You’ve covered the full cycle really well, including the QA testing. On the data side — do you think capturing that level of granularity in real-time (like pricing logs and volume) would be feasible during peak load times?

Edited by Priyanka R Daswani on Sep 14, 2025 at 5:31pm
 Reply Reply to Comment
Collapse Subdiscussion
Raghavachary Nallani Charavarthula
Raghavachary Nallani Charavarthula
Sep 8, 2025Local: Sep 8, 2025 at 4:14pm<br>Course: Sep 8, 2025 at 3:14pm
Data:
To train the model, we would use climate data (temperature, precipitation, sea-level rise, storm frequency) from NOAA, NASA, and IPCC datasets. satellite and geospatial data (elevation, flood zones, urban development) from NASA, ESA, and USGS.
socioeconomic data (population density, infrastructure) from city governments and the World Bank and environmental data (soil type, vegetation coverage) from GIS databases.
Key variables:
Input features would include temperature, precipitation, storm frequency, elevation, distance from coastline, urban density, soil type, vegetation coverage, and population density. The output variable would be a risk score for flooding or climate-related damage, which could also be expressed as predicted flood extent or expected financial loss.
Type of ML problem:
This is a supervised learning problem. If predicting continuous outcomes like flood extent, it’s a regression problem; if classifying areas into “high-risk,” “medium-risk,” or “low-risk,” it’s a classification problem. Non-parametric methods such as Random Forests or Gradient Boosting are well-suited due to nonlinear interactions in the data.
Steps to solve the problem: Following a standard ML workflow/pipeline:
                                                              1) define the problem, 
                                                              2) collect data, 
                                                              3) clean and pre-process data, 
                                                              4) engineer features, 
                                                              5) split data into training, validation, and test sets, 
                                                              6) select models, 
                                                              7) train models, 
                                                              8) evaluate performance, 
                                                              9) tune hyperparameters, and 
                                                              10) deploy and monitor predictions.
Handling missing data:
Missing values may arise from gaps in sensors, incomplete historical records, or inconsistent socioeconomic data. Approaches include imputation (mean/median/mode), advanced ML-based imputation (like KNN or regression), or removing records with minimal missing values.
 Reply Reply to Comment
Collapse Subdiscussion
Steven Amet
Steven Amet
Sep 11, 2025Local: Sep 11, 2025 at 3:11pm<br>Course: Sep 11, 2025 at 2:11pm
Climate data is an important and timely topic. From my experience in the employment sector, I’ve seen how it has become a key consideration due to the potential financial losses linked to climate change factors such as flooding, wind damage, and overheating. For example, a major challenge for banks in mortgage lending is assessing whether a property will be at risk of flooding in the future. A key challenge is receiving the latest data available to ascertain what areas are of potential risk on an ongoing basis.

 Reply Reply to Comment
Collapse Subdiscussion
Devang Shah
Devang Shah
Sep 8, 2025Local: Sep 8, 2025 at 8:54pm<br>Course: Sep 8, 2025 at 7:54pm
Problem Definition

Objective: To create a machine learning classification model that accurately categorizes incoming insurance claims into two streams in real-time: "Approve" for straight-through processing (STP) and "Review" for manual handling by a human adjuster.

What data would you use?

To train the model, the following data sources are used:

Structured Data:

Claimant and claim history records from the past 5–7 years
Policy details such as policyholder tenure, policy type, and coverage level
No-claims discount information and payment history
Incident-related data including type of loss, date and time, and incident descriptions
Unstructured Data:

Images (e.g., photos of damages)
Documents and reports
Third-Party Data:

Vehicle information databases (e.g., DVLA)
Geolocation and mapping data (e.g., Google Maps API)
Public datasets such as crime statistics
 

What are your key input and output variables?

Input Features (X):

Policy attributes
Claimant details and claim history
Incident information
Third-party data sources
Output Variable (Y):

Claim_Outcome

Approve → Straight-through processing
Review → Manual assessment by a human adjuster
 

What type of machine learning problem is this?

This is a supervised classification problem, and it is best solved using a non-parametric approach.

 

What steps would you take to solve this problem through machine learning?

Define the problem
Data Collection
Data Cleaning & Preprocessing
Feature Engineering
Data Splitting (training, validation, test sets)
Model Selection
Model Training
Performance Evaluation
Hyperparameter Tuning
Deployment & Monitoring
 

What might cause missing data in your data set?

Potential Reasons for Missing Values: Human Error, System or Integration Failures, Information is Not Applicable and Privacy Concerns or Non-disclosure.  Approaches include imputation to handle them effectively

 Reply Reply to Comment
Collapse Subdiscussion
Benjamin Baumann
Benjamin Baumann
Sep 9, 2025Local: Sep 9, 2025 at 9:20pm<br>Course: Sep 9, 2025 at 8:20pm
Can ML support faster and more accurate planning decisions?

What data would you use?
The main data comes from planning applications, decision notices and appeal outcomes. Some of this is structured in systems and open APIs, but a lot still sits in unstructured data such as PDFs or case notes. We’d also want property and geospatial data, things like building type, conservation areas, or flood zones. Audit trail data of the case officer’s actions could then help show which tasks are efficient and which are repetitive or need improving.

Inputs and outputs
Inputs could be the application type, property details, policy references, officer reports, consultation responses, and site context. The output might be a predicted decision (approve/refuse) with clear reasoning and a probability of the application being appealed.

Type of problem
This probably falls under a supervised classification problem as we’re learning from past labelled data (decisions) to predict future ones. For appeal likelihood it’s more of a prediction problem. The patterns are unlikely to be linear, so something like gradient boosting or random forests would make sense.

Steps to approach it

Define the problem – consistency and speed in decisions.

Gather data across councils / scrape public sources.

Clean and standardise formats, extract text from PDFs.

Explore which features correlate with outcomes.

Engineer features (e.g. policy text, geospatial context).

Train/validation/test split.

Start with simple models, then move to more complex ones.

Evaluate accuracy and fairness.

Deploy and integrate with planning tools as decision support, not automation.

Missing data
Blank fields, poor scanning, differences in how councils collect data, missing appeal links. Numeric gaps can be filled with averages or flagged as unknown, while missing text just needs to be carried through as “not available”. 

In summary
It’s a good fit for machine learning as there are lots of historic data, clear outcomes to learn from, and potential to save time and improve consistency. The hard bit probably isn’t the modelling, it’s getting the data clean, joined up, and reliable. 
Once a model is in place, we’d want to measure its value. That could mean tracking how much faster decisions are being made, how often predictions line up with final outcomes, and whether flagged cases end up in appeal.

 Reply Reply to Comment
Collapse Subdiscussion
Steven Amet
Steven Amet
Sep 11, 2025Local: Sep 11, 2025 at 3:16pm<br>Course: Sep 11, 2025 at 2:16pm
 I think this is a great idea. One question I have is, how would the model ensure transparency in its predictions? For example, could there be a risk of bias toward certain locations—such as higher approval rates in more affluent areas and lower approval in areas with lower socio-economic status?

 Reply Reply to Comment
Collapse Subdiscussion
stephen sefa
stephen sefa
Sep 9, 2025Local: Sep 9, 2025 at 9:45pm<br>Course: Sep 9, 2025 at 8:45pm
Challenges in Sports and the Role of Machine Learning (ML)

The data  i will use to prevent injuries and increase performance will be wearable device eg GPS and accelerometers, training logs which could be the kind of training being done or the duration of the training, Medical records of an athlete and match data which includes minutes played and performance stats.

key input and output variables
Input Variables (X)

Age of athlete, position, training load, injury history, minutes played, sprint count of athlete, medical records and performance stats

Output Variable (Y)

Binary Indicator- Injury (True/false)

type of machine learning problem
Classification (predicting injury: True/False)
Supervised learning (labeled data)
steps to solve the problem
Define the problem – Predict injury risk from player and training data

Collect data – From wearable sensors, match logs, and medical records

Explore the data – Identify trends and data quality

Preprocess data – Clean data

Engineer features – Get the workload ratios

Select model – Models like Logistic Regression can be explored

Train the model 

Evaluate the model 

Tune hyperparameters 

Deploy & monitor – Gradual integration into the system and monitor it time and time.

Possible causes of missing data:

Sensor failure like GPS not recording
Player not wearing device eg injury to player or players day off
Manual entry errors or inconsistent tracking
Handling approach:

Imputation methods such as mean/median imputation or regression-based imputation can be used. Indicators can also be added to flag missing information or data when a player has a day off or is injured. Data deletion must be avoided unless data is in small amount.

 Reply Reply to Comment
Collapse Subdiscussion
Alex Llewelyn
Alex Llewelyn
Sep 10, 2025Local: Sep 10, 2025 at 9:38pm<br>Course: Sep 10, 2025 at 8:38pm
What would be the implication of the binary classifier? If 'Injury' is True, does this mean the algorithm is classifying the athlete as currently injured or at risk of injury? Would if perhaps be helpful if the algorithm were able to predict injury risk based on the current training load and other parameters and provide a warning to athletes when the risk is increased? Maybe some sort of inference could be used to provide feedback to players, indicating how they could reduce their injury risk?

 Reply Reply to Comment
Collapse Subdiscussion
Inderpal Tiwana
Inderpal Tiwana
Sep 10, 2025Local: Sep 10, 2025 at 11:28am<br>Course: Sep 10, 2025 at 10:28am
What data would you use? 
A combination of both structured and unstructured data, covering capacity, dates/timestamps, platform usage statistics, workload types (migratable vs non migratable), chat logs for time to resolve capacity issues, covering key metrics discussed etc…
What are your key input and output variables?
Input - Current platform capacity, timestamp, frequency of capacity increase/decrease, historical platform data, active users, active applications
Output - prediction/forecasting of capacity with a binary if required to increase now 
What type of machine learning problem is this? 
Supervised, due to historical data to give predictions in real time, but could be parametric based on the implementation
What steps would you take to solve this problem through machine learning? 
1. Define problem
2. Gather data, api’s, monitoring tools, logs, metics
3. standardise /clean data for processing, coming from lots of sources so will need to be standardised
4. Split data, for training validation and test.
6. Model selection and training, best suited to the problem, addressing what will give the best results
7. Evaluate and tune
8. Deployment and continuous monitoring
Outline the general process, referencing the ten-step machine learning pipeline.
What might cause missing data in your data set? 
Identify potential reasons for missing values, and suggest an approach you’ve learned in this module to handle them effectively.
Downtime for platform, metrics issues are common, application errors not posting logs, storage capacity, upgrades etc… using imputation such as mean will be useful as it can provide historical data as reference and will be best placed to provide accurate data substitutes
 Reply Reply to Comment
Collapse Subdiscussion
Jack Dunning
Jack Dunning
Sep 10, 2025Local: Sep 10, 2025 at 4:14pm<br>Course: Sep 10, 2025 at 3:14pm
What specific issue are you trying to solve?
Improving field-level weather and soil forecasts to help farmers make better decisions on planting, irrigation, and spraying.

Who is affected by this problem?
Farmers, agronomists, and the wider food supply chain that depends on stable yields.

What impact does it have?
Inaccurate forecasts cause wasted inputs, lower yields, and financial losses, reducing farm profitability and food security.

Why do you think machine learning is well suited to addressing this problem?
It can ingest large, heterogeneous datasets (weather models, satellite imagery, soil/crop data), identify complex patterns, and generate predictive insights at field scale.

What data would you use?
Weather forecasts (Met Office ensembles), satellite imagery (Sentinel-2), historical soil and crop datasets, and farm management records (planting, irrigation, yields).

What are your key input and output variables?
Inputs: temperature, rainfall, humidity, soil type, irrigation events.
Outputs: soil moisture levels, crop stress indicators, yield outcomes.

What type of machine learning problem is this?
A supervised regression problem (predicting continuous values like soil moisture or yield). Non-parametric methods are likely best due to non-linear relationships between inputs and outputs.

What steps would you take to solve this problem through machine learning?

Define the problem: Provide field-level forecasts that reduce climate-driven yield risk and improve farm decisions.

Collect data: Gather Met Office forecasts, Sentinel-2 satellite imagery, soil and crop records, and historical yield/weather data.

Clean data: Handle missing sensor readings, gaps in satellite imagery, and inconsistencies across farm records.

Explore data: Analyse seasonal trends, correlations between soil moisture and yield, and identify anomalies such as drought years.

Split data: Partition into training, validation, and test sets to ensure robust supervised learning.

Select & train model: Apply regression and time-series ML models to predict soil moisture and crop stress at field scale.

Evaluate model: Use metrics like RMSE and R² to assess forecast accuracy and decision-making impact.

Deploy model: Integrate forecasts into farmer-facing decision-support tools with clear actionable outputs.

Monitor model: Continuously retrain as new weather and field data arrive to maintain accuracy.

Test in practice: Validate outputs with live farmer case studies before scaling across wider regions.

What might cause missing data in your dataset?
Cloud cover in satellite imagery, faulty sensors, or incomplete farm records. Approaches include imputation using statistical methods (mean/median), or interpolation from nearby time points.

 Reply Reply to Comment
Collapse Subdiscussion
Craig Dawson
Craig Dawson
Sep 10, 2025Local: Sep 10, 2025 at 4:18pm<br>Course: Sep 10, 2025 at 3:18pm
I work on ships and a key task every day is to keep a log of timings which summarise the activities that occur on that day such as the moving of equipment on deck. This task is typically done manually but CCTV / ML could be used to automate the process. 

What data would you use?

High-quality images of the relevant equipment would be required, sourced from existing footage. For new equipment that has never been present in the already available footage, new recordings / pictures can be made. 

What are your key input and output variables? 

The key input variables are the images and also perhaps a co-ordinate system that can be referred to to determine what specific operation is being performed when the items of equipment are being moved. The main target outcome variables are timings which summarise the timings of each activity. 

What type of machine learning problem is this?

This is a classification problem as we are not trying to make any predictions but are trying to classify items and record information related to them. Supervised learning would make more sense, especially when the model is being trained to ensure it is identifying objects correctly and in the correct way. Also, we are interested in known patterns and the output timings returned will always be reviewed by humans before being deemed correct. Non-parametric is preferred as it is typically better placed to adapt to complex visuals. 

What steps would you take to solve this problem through machine learning? 

1) Define the purpose: To obtain accurate timings that are generated in an automated manner.

2) Obtain the data set: Existing and new still images sourced.

3) Clean the data: Make sure the images are high-quality and only show the item of interest.

4) Dimension reduction: Streamline even further the succinctness of the images.

5) Task at hand: Identify when certain items are moved onboard a ship and recording the associated timings.

6) Partition the data: Train the model to identify the objects, fine tune the image identification during the training and validate that the training has been successful.

7) Choose ML techniques & 8) Use ML techniques: Dimensional reduction, classification and computer vision are strong candidate techniques.

9) Interpret the results: Check the model is correctly identifying objects.

10) Deploy ML techniques: Install the ML CCTV systems on ships. Retrain for different projects as required.

What might cause missing data in your data set?

Missing input data could be caused by malfunctioning cameras however the objects we are tracking are typically quite large so hopefully they could still be identified. If timings are missing in the output data then median, mean and/or interpolation replacement data would be sufficient.

 Reply Reply to Comment
Collapse Subdiscussion
Hanyi
Hanyi
Sep 10, 2025Local: Sep 10, 2025 at 4:32pm<br>Course: Sep 10, 2025 at 3:32pm
What data would you use?
To predict customer churn, I would use both internal and external datasets. Internally, this includes sales data, customer demographics, purchase history, order frequency, complaint logs, and engagement records such as email or platform usage. Externally, I would also look at broader market and industry trend data, which could provide context on seasonal shifts or wider customer behaviour patterns.

What are your key input and output variables?
Key inputs: purchase frequency, recency of last order, total spend, number of complaints, time to resolve complaints, loyalty programme membership, and market trend indicators.
Output: a binary churn flag (1 = at risk of leaving, 0 = likely to stay), and potentially a probability score of churn risk.

What type of machine learning problem is this?
This is a supervised classification problem, since we have historical labelled data (customers who stayed vs those who churned). 

What steps would you take to solve this problem?

Define the problem (predict churn to target retention campaigns).

Gather data from sales systems, CRM platforms, support logs, and external market sources.

Clean and preprocess: handle missing values, standardise formats, encode categorical variables.

Explore data: analyse customer segments, behaviour patterns, and churn rates.

Split into training, validation, and test sets.

Select models and train them.

Tune hyperparameters and evaluate performance using MSEand R^2

Deploy the chosen model to score customers in near real time.

Integrate outputs with marketing systems to trigger retention emails or offers for at-risk customers.

Continuously monitor and retrain the model to account for changing customer behaviour and market trends.

What might cause missing data in your dataset?
Possible causes include incomplete customer records, missing demographic details, unlogged complaint tickets, or customers with very few transactions. To handle this, I would apply imputation techniques (median/mean substitution or model-based imputation), or if the database is large enough i will just drop the missing records.

 Reply Reply to Comment
Collapse Subdiscussion
Alex Llewelyn
Alex Llewelyn
Sep 10, 2025Local: Sep 10, 2025 at 9:24pm<br>Course: Sep 10, 2025 at 8:24pm
Type of data
Data from a specifically designed clinical trial would allow control of confounding variables, the collection of all desired parameters, and greater confidence in the accuracy of labelling. The dataset would include mRNA sequencing data for a large panel of genes extracted from urine and semen, as well as PSA scores and relevant clinical details. Genes to be tested would be curated using peer-reviewed data implicating them in PCa, e.g,  oncogenes, tumour-suppressor genes, immune-response markers.

Input Variables

Continuous numeric values: mRNA expression intensity of selected genes, PSA score, age, BMI

Categorical variables: smoking status, family history

Output Variables

Categorical output from a binary indicator of cancer status, with separate cancer stage classification model or a single model outputting 'No Cancer, Stage I, II, III, IV'. 

Type of Problem

Classification, supervised learning. Due to complex relationships, a non-parametric modelling approach (e.g., decision-tree ensembles) may be  appropriate. Allows for feature-importance to be discernible to confirm biological relevance. Parametric approaches that cope with highly complex data (e.g., neural networks) also possible, but may not be practical to obtain sufficient sample size.

Steps

Define the problem: improving diagnostic accuracy for PCa. Success could be higher AUC than PSA alone. False negatives for advanced cancer are more impactful and should be penalised heavily, even at the cost of an increased false positive rate.
Data acquisition: plan, obtain ethical approval for and carry out a dedicated clinical trial to gather the required data, determining an appropriate number of patients for the parameter space in advance. Ensure the dataset is diverse and demographically representative.
Data cleaning and pre-processing: normalise gene expression values (e.g., z-scores per gene). Resolve any missing values (see below). Apply class weighting or stratified sampling if the data are unbalanced.
Exploratory analysis: employ dimensionality reduction, e.g., principal components analysis, to see if gene expression profiles cluster. This can guide feature selection and reduce parameter space.
Split data: randomise dataset and split into training, validation, and test datasets
Select model: try a few different models to find the most effective. Logistic regression could be used as a simple baseline to compare with random forest, support vector machine or neural network approaches.
Train model: maximise AUC as the primary output, with an increased penalty for misdiagnosis of Stage III/IV cancer.
Model evaluation: evaluate on test set; if probabilities are generated, adjust thresholds to achieve desired sensitivity/specificity balance.
Hyperparameter tuning: maximise performance without overfitting. Revisit feature selection if it is suspected some features reduce generalisation
Deploy and monitor: monitor performance over time, collect outcomes of patients in the trial, and continually assess real-world accuracy.
Missing Data

Laboratory technical issues (e.g., insufficient sequencing data for a particular gene, low quality samples), clerical errors, patients dropping out, opting out of certain tests, or declining to provide information could all lead to missing data. K-nearest neighbours or multiple imputation could be used to predict missing mRNA data, while mean/median/mode imputation could be used for data such as age, BMI or smoking status.

 Reply Reply to Comment
Collapse Subdiscussion
Aliaksandr Masny
Aliaksandr Masny
Sep 11, 2025Local: Sep 11, 2025 at 1pm<br>Course: Sep 11, 2025 at 12pm
Is it possible to run a pilot study using the existing data from biobanks, before running a trial? I mean that one could try to validate the curated gene list and check the feasibility.

Regarding the use of data from several human fluids, what might be the potential issues during the model training in this approach?

And back to the choosing of purpose, how one can balance between the interpretability and the model's performance?

 Reply Reply to Comment
Collapse Subdiscussion
Priyanka R Daswani
Priyanka R Daswani
Sep 11, 2025Local: Sep 11, 2025 at 8:06am<br>Course: Sep 11, 2025 at 7:06am
Disclaimer:

The original content shared and submitted here was my independent intellectual property and strategic thinking, dated 10th & 11th September 2025. This content has been removed and is not available for reproduction, distribution, or reference without prior permission.

Edited by Priyanka R Daswani on Oct 21, 2025 at 9:42am
 Reply Reply to Comment
Collapse Subdiscussion
Mariano Capezzani
Mariano Capezzani
Sep 11, 2025Local: Sep 11, 2025 at 8:15am<br>Course: Sep 11, 2025 at 7:15am
Problem

At The Weather Company, we provide customers with weather insights to they stay safe and weather-aware. At any given point there are a number of storm cells developing around our customers, and we would like to build a model that predicts if a given cell will reach them with a certain intensity. Leaving tropical storms and large tornados aside, lower intensity cells, like rotation, severe hail or tornado vortexes can still pose a threat to life and property, or may at least affect peoples intentions, so the earlier we can predict these will cross their path, with certain degree of confidence, the higher the quality of our service.

The hypothesis is that via a Machine Learning technique we may use historical data about the evolution of these storm cells, knowing their path, speed and intensity, to create a predictive model.

Our challenge is that we currently have limited storage of historic data, in the order of many terabytes per day. We’re looking into this.

The key question remains, whether any ML algorithm would still be able to provide a confident prediction, given the intrinsically stochastic nature of weather systems, but we think they may offer a path to better probabilistic guidance and improved early warnings for our customers.

 

Analysis

We have limited historic data on storm cell paths that is readily available, but we can access backups, and we can certainly start persisting with structure as of now. We have access to vasts amount of data captured from radar, satellite imagery, and ground sensors.

Inputs:

location- and time-specific weather conditions such as include precipitation in dbZ, reflectivity velocity and other parameters directly from radar, temperature, wind, pressure, etc.
geocode, type, direction, speed and intensity of storm cells, as well as more technical information such as rotation metrics, echo top, meso height, hot storm index, etc.
the customer's location
Output:

given the customer's location and a set of active storm cells, the probability of a storm cell reaching them, and the time, speed and intensity at arrival
Type: 

This is a supervised learning problem, using labeled historical storm cells and their path and impact as training data. 
Classification: storm reaches or not
Prediction (regression): we are inferring continuous variables such as ETA, speed and intensity
Steps: 

1. Define GOAL: predict storm cell reaching customers, with impact with intensity.

2. Collect data: storm cell data, path, speed and intensity based on radar, satellite, and ground reports.

3.    Inspect and clean: remove duplicate cells, or those that have too short a timespan to be significant.

4.   Dimension Reduction: extract predictors such as relative velocity toward location, storm heading, rotation strength, and storm size

5.    Determine ML task: this looks like a supervised classification/regression problem, of predicting impact probability and severity.

6.    Split data into training, validation, and test sets, by storm type and season or region.

7.    Choose ML technique: logistic regression?

8.    Use the tecnique: ?

9.    Interpret: validate results with aid of science team and meteorological experts.

10.    Deploy: integrate into Storm Radar app for beta testing, evaluate results and customer feedback

 

We might not have all required data, for example storm cell real path at various timestamps. Also, some of these storm cells merge with each other and dissipate in a rather unpredictable way.

 

 

 

 Reply Reply to Comment
Collapse Subdiscussion
Mariano Capezzani
Mariano Capezzani
Sep 11, 2025Local: Sep 11, 2025 at 8:19am<br>Course: Sep 11, 2025 at 7:19am
I'm unable to edit, so completing step 8:

8. Apply the model to historic storm cells (what we can gather) and compare predicted output with real output. There should be at least some correlation between the expected path, ETA and intensity on arrival to a test location, between both observed and predicted values.

 Reply Reply to Comment
Collapse Subdiscussion
Leonardo Diodato
Leonardo Diodato
Sep 11, 2025Local: Sep 11, 2025 at 10:27am<br>Course: Sep 11, 2025 at 9:27am
Sales forecast for new product launches and seasonal sales forecasts for existing ones.

I currently work in a company that produces products of which sales are affected by seasonality. It would be great to apply machine learning to help the management make better informed decisions about launch dates and planning better the launch of the new products.

 

What data would you use?

I would use historical data about products launches and the performance of sales related to each of them. The data source for these is internal to the company, and the type of the data is mostly categorical

 

What are your key input and output variables?

Key input variables are product type, details and specifics of the same, launch date, marketing strategies used.

Output variable is the number of sales of each product following its launch on the market in various time frames (sales in the first week, first month, first trimester)

 

What type of machine learning problem is this?

I believe this is a prediction problem, supervised (as recent historical data are available) and I would use a parametric approach

 

What steps would you take to solve this problem through machine learning?

As the purpose of the ML project has been defined already, the next steps are data collection, exploration and preparation: collect and analyze the available data to eventually operate a dimension reduction and feature engineering. Once the data are ready the ML task has to be determined, a guess for the moment is as stated above, a prediction problem, supervised. The next step would be data partitioning (train, validation and test datasets creation) and picking the best ML technique for this case. After that has been chosen, it will be used and its performance evaluated. If it is deemed satisfactory, eventually it will be deployed and used.

 

What might cause missing data in your data set?

Missing data in my case could be related to older historical product launches sales performances (outcome variables) and marketing strategies (input variable) used not being recorded at the time. Details and specifics of the products are still available for any product (other input variables). To handle this missing data I would drop the rows with unavailable data.

 Reply Reply to Comment
Collapse Subdiscussion
Aliaksandr Masny
Aliaksandr Masny
Sep 11, 2025Local: Sep 11, 2025 at 11:58am<br>Course: Sep 11, 2025 at 10:58am
Predicting the cognitive decline in Alzheimer's Disease
Assessment:

The relationships between biological, clinical, and imaging data are highly sophisticated. Thus, unlike statistical analysis, this task is suited for a ML model that can identify subtle patterns in high-dimensional data.

What data would you use? 

Neuropsychological test scores data is required: it is the yearly score from tests like mini-mental state examination (MMSE) to quantify cognitive function over time.
Brain imaging data such as Magnetic Resonance Imaging (MRI),  Computer Tomography (CT), or Positron Emission Tomography (PET) scans.
Fluid biomarkers data, like blood and the cerebrospinal fluid (CSF) biomarkers.
General clinical data - age, years of education, genetic risk factors.
 

What are your key input and output variables? 

Key output variable is the rate of cognitive decline.
Key input variables are:

MMSE score
CSF amyloid-beta and tau levels
Hippocampal volume
Blood biomarker levels
Age of a patient
Years of education
 

What type of machine learning problem is this? 

This is a forecasting supervised learning problem, specifically the regression task.

The model will learn from the longitudinal features data and predict the known outcomes, actual measured cognitive decline, which is a continuous numerical value. Both parametric and non-parametric models could be used, depending on the purpose.

 

What steps would you take to solve this problem through machine learning? 

Define the problem: develop a model that accurately predicts the rate of cognitive decline in patients diagnosed with early-stage Alzheimer's disease.
Collect data: ask for the access to the clinical longitudinal data from different data providers.
Clean data: normalize data points from different datasets, imputing missing data, removing outliers.
Explore data: analyze the cleaned dataset to understand relationships and patterns, remove possible intrinsic dependencies.
Split data into training, validation, and test sets.
Select & Train the model: choose a suitable regression algorithm, like Linear or Polynomial Regression, train it.
Evaluate model by checking the performance on the test set. Mean Squared Error (MSE) or other metrics will be helpful for the evaluation.
Deploy and monitor might be tricky for clinical data. Deployment inside the research institute might happen by providing our model for the community in a scientific publication. If we are working in a clinics, we could provide a recommendation tool for the doctors. Monitoring model's prediction could be then compared against actual patient data, and improve it. If it could successfully predict the outcome, we can use our model for the identification of new drugs in trials.
 

What might cause missing data in your data set?

Patient dropout, that might happen due to personal reasons or health issues.
Skipping procedures, due to refusal of a painful procedures, like CSF collection.
Variety of measurement procedures, that may not be consistent across different datasets.
Technical accessibility of procedures and equipment for some patients.
Collection data entry errors.
To handle it, stochastic regression or MICE techniques must be used as reliable methods, known for their preservation of variability and reduction of bias.

Edited by Aliaksandr Masny on Sep 11, 2025 at 12:21pm
 Reply Reply to Comment
Collapse Subdiscussion
Waqas Zubairy
Waqas Zubairy
Sep 11, 2025Local: Sep 11, 2025 at 12:24pm<br>Course: Sep 11, 2025 at 11:24am
Introduction

In the past, I was working with wealth management company, the major goal of the company is to maximize the wealth of customers by investing into stocks and other financial instruments. I was mainly involved in designing the ETL process to bring the data from their CRM and stock transactions systems into Centralised location (ADLS) for reporting purpose (Power BI), Because of the number of pipelines I built I had a good understanding of data.

 

What Data Would You Use?
We need different kinds of data which can in use as predictor to build a effective machine learning model

Customer-level data: demographics (age, income, net worth), investment goals, risk tolerance, and investment horizon.
Account and transaction data: historical trades, portfolio composition, cash flows, dividends, and fees.
Market and product data: stock prices, indices, bonds, mutual funds, ETFs, alternative investment returns, interest rates.
External data sources: economic indicators, inflation rates, sector performance, news sentiment, geopolitical events.
Source of data:

We were using Salesfroce (CRM) system and Avaloq (portfolio management systems)
Data feed from Market data vendors for stock prices, we mainly use API interface from Bloomberg
Publicly available economic datasets and financial news feeds which could impact stock prices and other regulatory related issues.
Key Input and Output Variables
Input features (X):

Customer demographics: age, income, risk profile.
Portfolio features: asset allocation, current holdings, historical returns, diversification metrics.
Market indicators: stock/bond prices, sector performance, volatility index (VIX), interest rates.
Transaction history: frequency of trades, past product performance.
Target variable (Y):

The predictor could be that how much return we can get from particular investments and how much return we could generate from investments (ChatGPT wordings for Y variable: portfolio return, wealth growth over a period, or risk-adjusted return.
We can also divide customers based on investments, frequency of investments, type of stocks they are interested in, which is more like a classification problem.
Type of Machine Learning Problem
Regression (Prediction):
For the values like returns on investment, regression testing is more suited
Classification:
For model related to classification of customers, the classification model is more applicable
Steps to Solve This Problem Using Machine Learning
Following the ten-step ML pipeline: (Ref: some help from ChatGPT in this section)

Define the problem: As a Scientist, I need to Predict portfolio return or calssify customers based on investments.
Collect data: Gather internal customer and portfolio data, market data, economic indicators.
Explore and understand data: Explore data using some tools like SQL or PowerBI, the main idea is to understand the data, how much data is distorted and what percentage of data is on good shape, also to understand which data is not available for machine learning processing.
Preprocess data: As discussed in current module we need to handle missing values using different methods like interpolation, normalize continuous variables, create categorical variables where needed
Feature engineering: Create features like historical volatility, Sharpe ratio, or moving averages.
Split data: there should be three sets of data including training, validation, and test sets.
Select model: we need to select model based on requirement of Y which is out outcome variable it could be Regression models (Linear Regression, Random Forest, XGBoost) or classification models (Logistic Regression, Random Forest, Neural Networks).
Train model: Fit the model using training data.
Evaluate model: Use metrics like RMSE for regression, or accuracy/F1-score for classification.
Deploy and monitor: Integrate model into decision support system, and periodically retrain with new data.
Causes of Missing Data in Wealth Management
Potential reasons:

Customers not disclosing certain demographic info (income, risk tolerance).
Incomplete transaction histories due to system errors or integration issues.
Market data gaps or delayed updates.
Mismatched identifiers across multiple data sources.
Handling missing data:

Deletion: Only if missingness is small and random.
Imputation:
Mean/median imputation for numerical features (e.g., account balances).
Mode imputation or most frequent value for categorical features.
Advanced techniques: k-NN imputation, regression-based imputation, or iterative imputation.
Interpolation: For time-series data (e.g., stock prices or portfolio values).
How Machine Learning Can Resolve Existing Issues
Portfolio optimization: ML models can predict potential returns and risks, helping advisors suggest personalized product mixes based on customer classification
Risk management: As studied in one of the case study we can use this to detect patterns that indicate potential losses or high-risk behaviors.
Customer segmentation: Identify clusters of customers with similar investment behavior for targeted strategies.
Missing data handling: ML models can impute missing customer or market data effectively, improving prediction accuracy.
Decision support: Provide real-time recommendations on rebalancing portfolios or adjusting asset allocation based on predicted outcomes.
 

 Reply Reply to Comment
Collapse Subdiscussion
Zohreh Kolaei
Zohreh Kolaei
Sep 11, 2025Local: Sep 11, 2025 at 12:50pm<br>Course: Sep 11, 2025 at 11:50am
Objective: To develop a machine learning model capable of accurately classifying dental X-ray images as either healthy (normal) or decayed (cavities).

 

What data would you use? The dataset will consist of dental X-ray images. These images must be manually labeled by dental professionals to indicate whether they show signs of decay or not. Once labeled, the data can be used to train, validate, and test the machine learning model.
 

What are your key input and output variables? 
Input (Predictor): Dental X-ray images (unstructured image data).
Output (Target): Binary classification label:
0 — Healthy (no decay)
1 — Decayed (presence of cavity)
 

What type of machine learning problem is this?  This is a supervised classification problem. Since the input data consists of images, models capable of processing visual data—such as Convolutional Neural Networks (CNNs)—are most appropriate.
 

What steps would you take to solve this problem through machine learning? 
define the problem
Data collection
Data annotation
Data cleaning and image preprocessing
Splitting the data (training, validation and test sets)
Model selection
Training the model
Perfomance evaluation
Hyperparameter adjustment or tuning
Model deployment
 

What might cause missing data in your data set? 
Low-quality or corrupted X-ray images may reduce model accuracy. These issues can be addressed by:

Removing unusable images from the dataset.
Attempting to enhance image resolution
 Reply Reply to Comment
Collapse Subdiscussion
Justin Boynton
Justin Boynton
Sep 11, 2025Local: Sep 11, 2025 at 2:07pm<br>Course: Sep 11, 2025 at 1:07pm
Problem statement: Forecasting potential software development project time overrun based on the project feature set and the resources working on the project.

Input and output variables

Inputs: Feature type, Feature complexity, Time estimate, Time logged, Developer role, Developer level 
Outputs: Projected overrun time

Type of machine learning problem

Prediction problem: We are trying to forecast how a new project might overrun
Supervised learning: We have historical data with the features and the output variable - time project overran
Non-parametric approach: The relationships between our input variables are complex, and we won't have a linear fit
What steps would you take to solve this problem through machine learning? 

Define the project scope: who will be affected by the project and what impact will it have? 
Identify data: what data are we going to use? How much data do we have? What issues might there be with the data?
Data cleaning and preprocessing: How many empty fields/columns do we have in our data? What types of imputation will we use to resolve holes in the input/output data?

Dimension reduction/Feature engineering: What inputs can be removed from our dataset as not required? Do any features need augmenting/normalising for better performance?
Select ML approach: Define the correct approach to solve the problem statement. What ML approaches will we use?
Prepare data for model development: Split data into training, validation and test data sets.
Develop and train the model: Select ML techniques, code and run training, validation and testing cycles.
Analyse the results: Assess model performance, identify potential issues and data weaknesses.
Iterate until ready for deployment: Tweak the model until it performs within acceptable benchmarks defined in the project scope.
Potential causes of missing data in our dataset
Time logs not filled in by developers: impute using Linear regression
Labelling/Tagging of project features is missing: use an NLP/SBERT algorithm to impute labels based on task title and description
 Reply Reply to Comment
Collapse Subdiscussion
Steven Amet
Steven Amet
Sep 11, 2025Local: Sep 11, 2025 at 3:04pm<br>Course: Sep 11, 2025 at 2:04pm
Challenge: Early Detection of Credit Deterioration in SME & Corporate Portfolios
What issue are we solving?
Banks often detect SME and corporate loan stress too late—after arrears or defaults materialize. We need an Early Warning Indicator (EWI) to flag rising credit risk proactively, enabling timely interventions like restructuring or covenant reviews.

Impact:
Late detection increases NPL ratios, provisioning costs, and reputational risk. Early signals improve portfolio resilience and customer outcomes.

Data to Use
We will combine macroeconomic indicators and bank-level credit data:

unemployment_data – monthly unemployment rates
cpi_data – Consumer Price Index (inflation)
savings_ratio_data – household savings ratio
disposable_income_data – household disposable income
bank_NPL – non-performing loan ratios (target proxy)
Additional SME/Corporate features (if available): financial ratios, sector classification, covenant breaches.
Sources:

Central Statistics Office (CSO), Central Bank of Ireland, internal credit systems.
Key Inputs and Output
Input Features:
Macroeconomic: Unemployment, CPI, Savings Ratio, Disposable Income
Derived: EWI composite score, EWI volatility, Sahm Rule signal
Firm-level (optional): Leverage ratio, liquidity ratio, sector risk
Output Variable:
Binary classification: 1 = loan likely to deteriorate (e.g., NPL within 6 months), 0 = healthy
Type of ML Problem
Supervised Learning (labeled historical data: default vs non-default)
Classification (predict risk flag)
Non-parametric (tree-based models like XGBoost handle nonlinearities and interactions well)
Steps to Solve (10-Step ML Pipeline)
Define Objective: Predict SME/corporate credit deterioration 3–12 months ahead.
Data Collection: Gather macro and internal credit data.
Data Cleaning: Merge on Month, handle missing values (forward fill for macro, imputation for firm-level).
Feature Engineering: Normalize indicators, compute EWI, volatility, Sahm signal.
Split Data: Train/validation/test using time-series split.
Model Selection: Gradient Boosting, Random Forest, or Logistic Regression for interpretability.
Training: Optimize hyperparameters via cross-validation.
Evaluation: ROC-AUC, Precision-Recall, backtesting on historical downturns.
Deployment: Integrate into risk dashboards with monthly refresh.
Monitoring: Track drift, recalibrate thresholds, governance checks.
Missing Data Causes & Handling
Causes:
Publication lags in macro data
Missing SME financial statements
Data entry errors
Handling:
Forward fill for time-series gaps
Mean/median imputation or model-based imputation for firm-level
Flag missingness as a feature if informative
Edited by Steven Amet on Sep 11, 2025 at 3:05pm
 Reply Reply to Comment
Collapse Subdiscussion
Urvi Joshi
Urvi Joshi
Sep 11, 2025Local: Sep 11, 2025 at 3:44pm<br>Course: Sep 11, 2025 at 2:44pm
Problem: Evaluating the factors which dictate a PV material's efficiency 

The type of data required to train the model would be theoretical material analysis using density functional theory. This would be narrowed down into different classes of materials so that they can be compared.

Input variables (X):

-Structured data: final estimated efficiency, bandgap, physical properties such as stoichiometry.

-Unstructured data: band structure, stable surface, physical structure, composition

-Third party data: Previously obtained experimental efficiencies for materials and determined structures, as well as theoretical data using a database such as the materials project to compile a wide range of structures. 

Output Variable (Y):

-Prediction of a materials efficiency and its stability as well as a print of its band structure and DOS.

Type of Problem:

-This is definitely supervised learning because the ML model is learning off of existing inputs as well as output data.

-This is a prediction problem, where the data set will take existing structures or classes and predict efficiencies based on the materials properties after being trained on similar materials. The model may have to be adjusted or incorporate some unsupervised learning if it is being trained on materials which have vastly different properties.

Steps:

1. Defining the problem: 

Evaluating the efficiency of a PV material (and learning about the factor dependency between classes of materials).

2. Collecting data

From existing material databases, as well as my own DFT calculations.

3. Cleaning the data

Will need to remove non-existent materials (incorrect or unstable structures) and potentially remove any materials with no theoretical data.

4. Dimension reduction/feature engineering

Eliminate factors which don’t dictate a wide class of materials to create a more general indicator. Can also create new categories which provide further accuracy for variables which were not considered general enough previously.

5. Defining the task

May have to redefine the task (is currently in between prediction and classification)

6. Splitting data into training/validation/test sets

7. Select & Train the model with ML techniques

8. Interpreting and comparing the models

Could compare how well the new theoretical provides an indicator for practical experimentation and materials.

9. Deploy and monitor

Monitor how the model works for a wide range of novel materials as well as pre-evaluated test materials.

 

Causes for missing data:

-Unevaluated structures/stoichiometries

-A material may simply not exist stably in a specific form.

The missing data is actually another important feature to train the model to remove structures which simply cannot exist. For data which simply doesn’t exist due to missing research a form of imputation would need to be implemented – we cannot simply use mean, modes or medians – instead the system would need to flag it and run a theoretical evaluation using DFT. For data which is missing because the structure is not a valid structure, the structure can simply be removed from the data base.

 Reply Reply to Comment
Collapse Subdiscussion
Prakasha Gourannanavar
Prakasha Gourannanavar
Sep 11, 2025Local: Sep 11, 2025 at 4:26pm<br>Course: Sep 11, 2025 at 3:26pm
Possible solution for the challenge / problem: Predictive IT System Monitoring

In recent times, several IT system failures have caused significant disruptions, affecting businesses, customers, and the public, often due to single points of failure.IT systems in critical areas, like airlines and laboratories, are highly complex and interconnected. Small issues, such as a spike in CPU usage or a minor network delay, can quickly lead to major disruptions. These disruptions can cause downtime, delays, and in some cases, safety risks. Currently, most monitoring systems react after problems occur, relying on logs and manual checks. Machine learning can help by detecting unusual patterns, predicting failures, and suggesting preventive actions, allowing teams to address issues before they escalate.

Possible sources of the data.
The predictive system would use multiple types of data:

Infrastructure metrics: CPU, memory, disk usage, network latency, and transaction rates.

Application logs: Errors, exceptions, response times, and database performance.

Historical incidents: Past outages, recovery times, and root cause analyses.

Environmental factors: Power fluctuations, temperature, maintenance schedules, and workloads.

User activity metrics: Flight operations, lab tests, or other mission-critical tasks.

Key Variables

Inputs: Time-stamped metrics, log events, transaction rates, sensor readings, and past incidents.

Outputs: Predicted system health, likelihood of failure, recommended actions, or automated alerts.

Machine Learning Approach
This is a mix of supervised prediction and anomaly detection. The system maps multiple inputs to a risk score or failure probability. Models like random forests, gradient boosting, or recurrent neural networks are suitable because they can handle complex patterns and time-dependent behaviour.

Process /Steps to build the system:
The process includes defining objectives, collecting and cleaning data, feature engineering, splitting data for training and testing, selecting and training models, evaluating performance, deploying real-time dashboards, and updating the system continuously. Features like moving averages, error ratios, and correlations help detect early warning signs.

Handling Missing Data
Incomplete logs or sensor failures are common. These can be managed with interpolation, forward-filling, or predictive imputation. Interestingly, missing or irregular data can also reveal hidden risks, making anomaly detection even more valuable.

Conclusion
Using this approach, teams can move from reactive problem-solving to proactive management. Predictive alerts and recommendations help prevent failures, reduce downtime, improve reliability, and ensure safer, smoother operations in critical IT systems

Edited by Prakasha Gourannanavar on Sep 11, 2025 at 4:27pm
 Reply Reply to Comment
Collapse Subdiscussion
Bruce Diesel
Bruce Diesel
Sep 11, 2025Local: Sep 11, 2025 at 4:30pm<br>Course: Sep 11, 2025 at 3:30pm
What data would you use:

The create the model, data from our own operations would be used.  We process transactions on behalf of numerous financial institutions and have agreements in place to utilise this data to improve our service offering.
The type of data is the raw telemetry from our machines which provides us with multiple years of cash dispensing per ATM.
Once models have been validated.  They would be adapted to specific financial institutions using the data they have from their own network.
Key Input/Output Variables:

Input variables are daily cash dispensing amounts, by denomination.
Interest Rates
Cost of CIT visits
Insurance costs
Type of Machine Learning:

Forecasting (prediction, supervised, non-parametric)
Predict future cash demand
optimisation (gradient descent, re-inforcement learning)
Optimise cash supply levels based on forecasted demand, cost of CIT, cost of Interest, insurance premiums
classification (unsupervised, classification)
Find different bahaviour profiles based on machine locations, in order to speed up learning when applied to new networks
 

Defne Purpose - as specified

Obtain data - already available
Data cleaning - most of the data is already clean as it is machine generated.
Dimensional Reduction / Feature - add factors such as public holidays
ML Task - core is prediction - based on multi-year historical data split into train/validate/test
Then optimisation - gradient descent based on demand, CIT costs, insurance and interest rates
Classification - cluster ATM's based on behaviour profile and location
 

 Reply Reply to Comment
Collapse Subdiscussion
Sundari Devulapalle
Sundari Devulapalle
Sep 11, 2025Local: Sep 11, 2025 at 5:26pm<br>Course: Sep 11, 2025 at 4:26pm
Problem Statement 

In the previous section, I discussed identifying fraud in financial transactions across the organisation as essential to protecting the bank and its clients. Although the temptation is to include all the points discussed in the previous section, it is evident that the problem needs to be broken down into smaller components. I am choosing transaction monitoring or client activity monitoring for this particular assignment as it fits well into the machine learning realm of identifying subtle and sometimes hidden patterns.

What data would you use?
I would use

Payment transaction data from our payments database
Client onboarding/KYC information
Account activity logs
External sources - sanctions lists, PEP watchlists, and adverse media feeds.
Time series
 

What are your key input and output variables?

Input variables: transaction amount,  origin and destination geographies, counterparty type, channel (online, branch, mobile), client risk profile, sanctions/PEP flags. Three engineered features- origin and destination countries, historical activity amount and frequency could be added too

Output variable : binary classification of a transaction as suspicious or not suspicious.

What type of machine learning problem is this?


I am trying to model this as a  supervised classification problem if historical suspicious activity reports (SARs) can be used as labels. However, an important point needs to be made here. SARs by themselves don't prove fraud. However, this is the best approximation we have considering the lack of labeled data. I would also use unsupervised learning that can identify unusual transaction patterns. Considering The problem suits non-parametric methods like decision trees which handle complex, non-linear data without assuming a fixed functional form.

What is the workflow?

Define the problem: detect suspicious payments indicative of money laundering or terrorist financing.

Collect data: gather transactional, client, and external risk data.

Explore data: analyse class imbalance (very few suspicious vs. many normal transactions).

Dimension reduction: engineer features such as transaction velocity, frequency, round-number payments, or unusual geographies.

Select model: test supervised models or unsupervised anomaly detection.

Partition data: Into training, validation and test
Train model: fit on training data with cross-validation.

Evaluate model: focus on recall (catching true suspicious cases) while balancing false positives, using metrics like precision, recall, and F1-score.

Interpret the results: adjust hyperparameters, resample data to handle imbalance, and refine features.

Deploy model: integrate into the bank’s AML system, monitor for drift, and retrain periodically.

What might cause missing data in your dataset?
Missing values may arise from incomplete KYC during onboarding, failed transaction logging due to system outages, inconsistent data entry across platforms, or delayed external watchlist updates. To handle this, I would apply mode imputation for categorical fields (e.g., client type), interpolation for time-series transaction gaps

 Reply Reply to Comment
Collapse Subdiscussion
Jose Arturo Michel Rodriguez
Jose Arturo Michel Rodriguez
Sep 11, 2025Local: Sep 11, 2025 at 5:48pm<br>Course: Sep 11, 2025 at 4:48pm
Problem Definition: Predictive value of game-play similarities

Objective: To predict in-game performance of a football player using play-by-play similarities. 

What data would you use? 
Player data such as DoB, number of games
play-by-play data such
passes with details such as direction, speed, completed/not-completed, distance, whether it is an assist or other important type of pass
shot on goal with same level of detail
movement on the pitch including speed, direction
tackles
One important consideration is the sequence of the events which could also be an important data point.
What are your key input and output variables? 
The inputs would be the current set of plays for any given player
The output would be a categorical classification of the player. For example a young player with with similar play style to a strong forward would be classified as as strong-forward.
What type of machine learning problem is this? 
The type of data would be suitable for a non-parametric model. Such that we let the model discover the complex relationships between the play-by-play sequences amongst all players and games.
What steps would you take to solve this problem through machine learning?
define the problem: classify a football player using play-by-play data
collect data: I would need to find a feed that provides fine-grained play-by-play. This could even be audio broadcasts that are then passed through a speech-to-text transformer.
clean and pre-process data: the data textual data will need to be cleaned of any unnecessary events as to only keep key events such as passes, attacks, shots, etc. Also need to split the plays for each player-game and label the performance.
engineer features: given that the number of plays for each player in any given game is undetermined I need to synthetise plays into more bounded features possibly by aggregating and grading each group of plays.
split data into training, validation, and test sets
select models, a type of neural network which should work better to discover non-linear relationships.
train models
evaluate performance
tune hyperparameters
deploy and monitor predictions
What might cause missing data in your data set? 
Data might not exists or be of low quality or incomplete given that football is rarely narrated in written prose, and standardized play-by-play data is not readily available.
Game data can also be missing because lower leagues have little coverage in which case only basic aggregated data (goals, cards, shots, etc.) might exists. 
Because non-parametric models require a large amount of data the feasibility of the project is low.
 Reply Reply to Comment
Collapse Subdiscussion
Hassan Chagani
Hassan Chagani
Sep 11, 2025Local: Sep 11, 2025 at 5:55pm<br>Course: Sep 11, 2025 at 4:55pm
Identifying tall structures from satellite images

Satellite images divided into grid cells, where tall structures have been identified by human analysts would be used to train the neural network. Additional data could include time of day when image was taken as the shadows would change depending on the position of the Sun, and location as buildings in different parts of the world can look different.

Key input and output variables

Input variables: the satellite images split into grid cells, the time of day, the latitude and longitude.
Output variables: an array of probabilities corresponding to each grid cell.
This would be a classification problem where 1 would indicate the definite presence of a high-rise building. It involves supervised learning as the neural network is trained on images. As the neural network will have a fixed number of parameters if the image resolutions are identical, this is parametric approach.

Steps

Define problem: reduce the number of images that human analysts need to look through in order to determine the location of high-rise buildings when designing catastrophe models.
Obtain data: satellite images of a geographical area, time of day when images were acquired and location.
Explore and clean data: remove restricted images from data, divide each image into grid cells and merge any cells that overlap with other images (identify with latitude and longitude coordinates), ensure all images have the expected resolution, remove any duplicate images. Identify grid cells with cloud cover that could obstruct the photographs.
Dimension reduction: remove any extra information such as source of images, which may be irrelevant. This can always be added back in at a later iteration if using multiple image sources.
Partition data: take a sample of images to act as the training set for human analysts, and another sample to compare the model output with that of human analysts. The remaining images form the set to be tested.
Choose machine learning technique: a neural network with input nodes for each grid cell, time of day, latitude and longitude.
Use machine learning technique: train the neural network with training set of images where high-rise buildings in each grid cell have been identified by human analysts.
Evaluate performance: the validation set of images is also analysed by humans and fed into the neural network. The model can be evaluated by determining how well it performed when compared with human analysts.
Deploy model: feed in the other images. The accuracy of the model will be monitored through the human analysts looking at grid cells that have a high likelihood of containing high-rise structures. Additionally, occasional checks of low-likelihood cells can be made to ensure these are not being missed.
Missing data

Restricted areas would be removed from photographs. These can simply be removed from the data set (i.e. no high buildings). Cloud cover can obscure part of photographs. The mean probability of surrounding grid cells could be used in these cases.

 Reply Reply to Comment
Collapse Subdiscussion
Jay Hopkins
Jay Hopkins
Sep 11, 2025Local: Sep 11, 2025 at 6:05pm<br>Course: Sep 11, 2025 at 5:05pm
Problem Definition

Objective: To create a machine learning model that can identify risk parameters for an underwriter, to understand whether based on the incoming data vs. the underwriters existing exposure, the underwriter is likely to provide a quote and corresponding capacity to underwrite the risk. 

What data would you use?

To train the model, the following data sources are used:

Structured Data:

Claims history relating to the proposed insured
The requested policy term
The requested pricing range
The requested policy limit
The requested policy deductible
Existing aggregates in the proposed risks sector, industry and geography
Unstructured Data:

Supplementary risk information, such as an engineering report, or an expert opinion on the risk 
 

What are your key input and output variables?

Input Features (X):

Policy attributes
Risk attributes
Output Variables (Y1, Y2... YN):

underwriting_decision

and if underwriting_decision = yes, then;

limit_of_liability

policy_pricing

What type of machine learning problem is this?

This would be a supervised model (it would be trained in parallel with actual underwriter decisions (i.e. augmentation)). I believe that this model would be parametric, as we'd be tuning it in tandem with underwriter results (e.g. the function is already known). 

 

What steps would you take to solve this problem through machine learning?

Define the problem
Data Collection
Data Cleaning & Preprocessing
Feature Engineering
Data Splitting (training, validation, test sets)
Model Selection
Model Training
Performance Evaluation
Hyperparameter Tuning
Deployment & Monitoring
 

What might cause missing data in your data set?

Not all risk information is available at the time of the submission. The risk may require extensions, reduced pricing, increased limits etc throughout the lifecycle of the insurance policy. This can lead to underwriters being pushed to accept risks that they otherwise would not have. 

 Reply Reply to Comment
Collapse Subdiscussion
Neetam Limbu
Neetam Limbu
Sep 12, 2025Local: Sep 12, 2025 at 1:08am<br>Course: Sep 12, 2025 at 12:08am
What data would you use? 

Price, volume, timestamp in frequency such as minute, hourly, or daily.
Quote data such as bid or ask.
Trade data such as timestamp, price, size, direction, venue.
Fundamental & event data such as earnings dates, dividend info, analyst ratings.
Alternative data such as news sentiment, social media buzz.
What are your key input and output variables? 

Input Variables: E.g., current asset price, strike price (for options), time to maturity (in years or days), risk-free interest rate, implied or historical volatility, dividend yield, volume, open interest, bid, ask, spread market, news sentiment, social media score, event flags

Output Variables: E.g., predicted asset or option price, forecasted implied volatility

What type of machine learning problem is this? 

Supervised Classification with Time-Series Constraints

We are training a model to predict a label (e.g. future price movement: up, down, or flat) based on historical features.
Labels are derived from future returns or barrier-based outcomes, which we compute from known data.
Our output is typically a discrete signal:
Binary: Long (+1) vs. Short (–1)
Ternary: Long, Short, Neutral (0)
Even if we predict probabilities or expected returns, we often threshold them into discrete actions.
What steps would you take to solve this problem through machine learning? 

Define the problem
Data Collection
Data Cleaning & Preprocessing
Feature Engineering
Data Splitting (training, validation, test sets)
Model Selection
Model Training
Performance Evaluation
Hyperparameter Tuning
Deployment & Monitoring
What might cause missing data in your data set?

Forward-fill only for ex-ante features (e.g., volume, price) and never for labels or future-dependent fields.
Drop samples with missing target or critical features especially if they compromise label integrity.
Impute cautiously, using median or regime-specific values only if justified by domain knowledge.
Flag missingness as a feature. Sometimes absence itself is informative (e.g., no trades during expected volume spike).
 Reply Reply to Comment
Collapse Subdiscussion
Manuel Ruiz Prado
Manuel Ruiz Prado (He/Him)
Sep 12, 2025Local: Sep 12, 2025 at 2:08am<br>Course: Sep 12, 2025 at 1:08am
I would use cloud monitoring and telemetry data from services like Azure Monitor, Application Insights, and Kubernetes logs. This would include CPU and memory usage, storage consumption, network throughput, active users, and historical cost reports. These data sources capture the patterns needed to forecast and optimize resource utilization.

What are your key input and output variables?

Inputs (features): CPU/memory usage, workload seasonality, network traffic, storage operations, user activity, and historical cost metrics.

Output (target): Recommended resource allocation (e.g., VM size, Kubernetes node scaling, or storage tier adjustments) that optimizes performance while reducing cost.

What type of machine learning problem is this?
This is a supervised regression problem, predicting future resource demands based on past usage. It is largely non-parametric, since workload patterns are complex and don’t follow simple linear trends.

What steps would you take to solve this problem through machine learning?
Using the ten-step ML pipeline:

Define the problem (optimize cloud spend while maintaining performance).

Collect monitoring and cost data.

Explore trends and identify anomalies.

Clean and align logs, normalize metrics.

Select supervised regression models (e.g., Gradient Boosting, Random Forest, or LSTM for time-series).

Split into training/validation/test sets.

Train the model on historical usage and cost patterns.

Deploy in Azure Data Factory or Databricks for ongoing predictions.

Monitor model drift and retrain as workloads evolve.

What might cause missing data in your dataset?
Missing values could result from monitoring outages, log ingestion failures, or misconfigured telemetry. To address this, I would use interpolation for time-series gaps or imputation techniques (such as median substitution or model-based methods) to maintain data integrity before training

Edited by Manuel Ruiz Prado on Sep 12, 2025 at 2:09am
 Reply Reply to Comment
Collapse Subdiscussion
Roshan Jayakumar
Roshan Jayakumar
Sep 13, 2025Local: Sep 13, 2025 at 8:30am<br>Course: Sep 13, 2025 at 7:30am
Problem: Reducing Urban Traffic Congestion Through Predictive Traffic Management.

The data that can be used in this case would be, Traffic flow data, Gps data, Public transit schedules and usage stats, and a particular event data.
 

The key input and output Variables include;
Input Features(X):

Time of day
Day of the week
Location(GPS)
Weather Conditions
Traffic incidents
Speciel events
Output variable(Y):

Traffic congestion level (e.g., low, medium, high), or a numeric value representing average traffic speed or travel time on a route.

 

What Type of machine learning problem is this?
This is a supervised learning problem that uses labeled historical data to predict future traffic conditions. If the goal is to estimate travel time or congestion as a continuous value, it's a regression problem; if it's to classify traffic levels into categories like low, medium, or high, it's a classification problem.Given the complexity and unpredictability of traffic data, a non-parametric approach is suitable.

 

What steps would you take to solve this problem through machine learning?
Define the problem: To forecast traffic congestion to optimize route planning and traffic signal control.
Data Collection: Gather relevant data from sources such as traffic sensors, GPS systems, and weather services.
Prepare Data: Clean the datasets and combine them based on matching time and location details.
Explore Data: Use visual tools to analyze traffic trends and identify key patterns or correlations.
Engineer Features: Identify and select important variables such as time, location, vehicle speed, and weather conditions.
Train the model: Train machine learning models like Random Forest or LSTM using the processed dataset.
Evaluate model: Measure model performance using appropriate metrics like RMSE for regression or accuracy/F1-score for classification.
Deploy and asses: Implement the final model into a live system, such as a traffic control dashboard or navigation application.
 

Missing data in a traffic dataset can result from various factors. Common causes include sensor failures, such as traffic cameras or detectors going offline, and GPS signal loss, especially in tunnels or during system outages. Delays in data synchronization from third-party applications or APIs can also lead to gaps. Additionally, human errors, like incorrect or incomplete logging of roadwork or public events, may contribute to missing information.
 

To address these gaps, several imputation techniques can be used. For time-series data, forward-fill or backward-fill methods can help maintain continuity. In numerical or categorical fields, missing values can be filled using mean or mode imputation. More advanced methods involve using predictive models that estimate missing values based on patterns in other related variables within the dataset.
 Reply Reply to Comment
Collapse Subdiscussion
Dibyajyoti Pradhan
Dibyajyoti Pradhan
Sep 18, 2025Local: Sep 18, 2025 at 2:38am<br>Course: Sep 18, 2025 at 1:38am
Problem: Detecting unusual account activity in SaaS audit logs

What data would I use?
In my work on HubSpot’s Account Insights and Audit Logs, we already collect a huge variety of data points—logins, API calls, permission changes, data exports, and admin actions. Each of these can be enriched with extra context like IP address, device, or location. For example, an account that usually logs in from London suddenly logging in from multiple countries in the same day could be a red flag. Similarly, if a user who rarely touches permissions suddenly starts escalating roles or exporting large chunks of data, that behaviour stands out. I’d also use time-based features (when the activity happens compared to normal working hours) and peer comparisons (what’s unusual compared to similar accounts).

Key inputs and outputs

Inputs: login frequency and failures, geo-location shifts, new device usage, API usage patterns, data export size, permission changes, and comparisons against both the account’s historical baseline and its peer group.

Output: a risk indicator. This could be as simple as “normal” vs “suspicious,” or a graded risk score. In some cases, if we have past confirmed incidents, the model could classify the type of risk (e.g., “suspicious login,” “unusual data export”).

Type of machine learning problem
This is primarily an anomaly detection problem because unusual behaviours aren’t always labelled in advance. Models like clustering or outlier detection can highlight when activity looks different from what’s typical. In situations where we do have historical labelled incidents, it becomes a classification problem—predicting whether an event is risky or not based on those past patterns.

Steps I would take

Define the problem clearly: focus on finding meaningful anomalies without overwhelming admins with too many false alerts.

Collect and prepare data: bring together logs from different systems, align timestamps, and remove duplicates.

Engineer features: create measures like login distance between locations, ratio of failed vs successful logins, frequency of role changes, or burstiness of API calls.

Train the model: use historical activity to establish what’s “normal,” and test against examples of suspicious behaviour where available.

Deploy gradually: first send alerts in a test environment and gather feedback from admins or security teams.

Refine and improve: use feedback on which alerts were useful vs noise to fine-tune thresholds and model features.

Monitor over time: retrain the model as behaviour patterns evolve, such as during new product launches or seasonal changes.

What might cause missing data?
Audit logs are messy. Missing data could come from system outages, client-side blocking (like ad blockers), partial events not syncing between services, or even privacy policies that remove certain fields. For example, if the IP or event type is missing, it becomes hard to judge the context of an action.

To handle this, I’d use a mix of approaches: simple imputation methods (like filling gaps with the most recent or average value) for non-critical fields, flags that explicitly mark missing data (sometimes the fact that data is missing is itself a signal), and cautious suppression of alerts when the most important fields are absent.

Summary
Audit logs are high-volume, noisy, and often overlooked, but they’re a goldmine for understanding account behaviour. I think machine learning is a strong fit because it can detect subtle, complex patterns that humans or static rules would miss. The biggest challenge isn’t building the model—it’s making the outputs clear, trustworthy, and actionable so that teams actually rely on them to protect customers and accounts.

 Reply Reply to Comment
Collapse Subdiscussion
Sam Cui
Sam Cui
Sep 30, 2025Local: Sep 30, 2025 at 9:48pm<br>Course: Sep 30, 2025 at 8:48pm
Data: telemetry traces of vehicle system sensors during specific maneuvers

Inputs: vehicle yaw rate, C.o.G slip angle, speed, acceleration, steering wheel torque

Outputs: driver inputs

Type: supervised, is prediction, however may need to be preceeded by unsupervised for data preparation, see below

Steps:

Predict human driver inputs when vehicle is not following desired trajectory
Collect telemetry traces of vehicle system sensors during specific maneuvers, either under safe and controlled test environments or in simulator environment
Group events into types based on what the desired outcome is (e.g obstacle avoidance, oversteer correction, etc.)
Using expert knowledge, convert raw sensor values into vehicle states that would more likely be sensed by humans
Select ML model. complex methodologies are likely suitable due to nature of modeling human behavior
Train. Each event group may require a different model
Test, metrics such as integral of error over period of time may be used
Missing values: lack of sensor, lack of correct labeling of desired outcome

---

## My Answer for Discussion 5.1

In Module 2, I proposed building a model to detect unusual account activity in SaaS audit logs. I work on HubSpot's Account Insights and Audit Logs, so I have direct access to real data—things like logins, API calls, permission changes, and data exports. The idea is to flag suspicious behaviour (like someone logging in from multiple countries in a short span, or a user who never touches permissions suddenly escalating roles) before it becomes a security incident.

**Probabilistic Setting**

Honestly, this assumption is only partly true for my problem. On one level, each audit log event could be seen as a sample from some underlying distribution of how users behave. But in practice, events aren't really independent. A failed login is often followed by a successful one. A permission change can trigger a chain of related actions. And if an account gets compromised, you'll see a cluster of weird activity all at once—those events are definitely correlated.

That said, I think there's a way to work around this. If I aggregate events into session-level or daily summaries and treat each account as a separate unit over fixed time windows, it becomes more reasonable to apply probabilistic thinking. It's not perfect, but it's workable.

**Stationarity**

This is where things get tricky. User behaviour isn't stable over time. When HubSpot releases a new feature, usage patterns change. During busy seasons, people work differently. Even something like the shift to remote work over the past few years has changed what "normal" looks like. A spike in API calls might just mean someone adopted a new integration—not that they're doing something suspicious.

On top of that, attackers evolve too. The tactics that worked last year might not be what we see next year. So the model would definitely degrade over time if we don't keep retraining it. This is probably my biggest concern with the feasibility of this problem.

**A Priori Knowledge**

This one I feel good about. I've been working with audit logs directly, so I know which signals tend to matter. Things like geographic impossibility (logging in from London and then Tokyo an hour later), access outside normal working hours, sudden data exports, or privilege escalation by low-level users—these are well-known red flags. There's also plenty of prior research in the security space, like the MITRE ATT&CK framework, that documents common patterns of account compromise.

For evaluation, the tricky part is balancing precision and recall. Too many false alerts and the security team stops paying attention. Miss a real threat and you've failed at the core job. But at least these trade-offs are well understood in the domain.

**If Assumptions Aren't Met**

To address the independence issue, I'd focus on feature engineering—aggregating raw events into higher-level behaviour summaries and looking at changes relative to each account's own baseline rather than absolute values. Adding time-based features (day of week, hour, time since last login) would also help capture natural patterns.

For the stationarity problem, I'd set up a retraining pipeline that updates the model regularly with recent data. Using sliding windows for training rather than a fixed historical dataset would help the model stay current. I might also consider a two-stage approach: first flag anything that deviates from the baseline, then use a separate model to classify what type of anomaly it might be.

**Conclusion**

Overall, I think this problem is feasible, but it needs careful handling. The domain knowledge is solid, which gives me confidence in feature design and evaluation. The main challenge is that behaviour keeps changing—both legitimate user patterns and attack methods. With the right retraining setup and adaptive thresholds, I believe the model can provide real value in catching suspicious activity before it causes harm.
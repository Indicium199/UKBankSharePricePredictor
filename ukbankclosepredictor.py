# Import necessary libraries
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Fetch bank data
banks = ['HSBA.L', 'LLOY.L', 'BARC.L', 'NWG.L', 'STAN.L']  # List of bank ticker names
data = yf.download(banks, start='2020-01-01', end='2024-01-01')  # Get historical data

# Extract 'Close' and 'High' prices for each stock
close_prices = data['Close'].dropna()
high_prices = data['High'].dropna()

# Create a binary target variable: 1 if the price closes higher than the previous day, 0 otherwise
for stock in banks:
    close_prices[f'{stock}_target'] = (close_prices[stock] > close_prices[stock].shift(1)).astype(int)

# Drop the first row due to NaN from shifting
close_prices = close_prices.dropna()
high_prices = high_prices.loc[close_prices.index]  # Align High prices with Close prices

# Concatenate Close and High prices as features
X = pd.concat([close_prices[banks], high_prices.add_suffix('_High')], axis=1)
y = close_prices[[f'{stock}_target' for stock in banks]]

# Split the data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data using StandardScaler for better model performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the MLPClassifier model with a similar architecture
model = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=1000, random_state=42, 
                      learning_rate_init=0.001)


# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions on the test set
predictions = model.predict(X_test_scaled)

# Calculate the accuracy
test_accuracy = accuracy_score(y_test, predictions)
print(f"Test Accuracy: {test_accuracy:.4f}")

# Prepare the output table
output_data = []

# Iterate over each date in the test set
for idx, (date, features) in enumerate(X_test.iterrows()):
    for i, bank in enumerate(banks):
        # Get the previous day's close price
        previous_close = features[bank]
        
        # Predicted label: 1 means price is predicted to go up, 0 means down
        predicted_price = "Up" if predictions[idx, i] == 1 else "Down"
        
        # Append the row to the output data
        output_data.append({
            'date': date,
            'bank name': bank,
            'previous day close price': previous_close,
            'predicted price': predicted_price
        })

# Convert the output data to a DataFrame
output_df = pd.DataFrame(output_data)

# Display the first few rows of the output DataFrame
print(output_df.head())

# Optionally, save the output to a CSV file
# output_df.to_csv('predicted_prices.csv', index=False)
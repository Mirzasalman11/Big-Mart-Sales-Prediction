import joblib
import pandas as pd
import argparse

# Load your encoder and model
loaded_encoder = joblib.load('C:/salman/ML/BigMart Sales/encoder.joblib')
loaded_model = joblib.load('C:/salman/ML/BigMart Sales/model.joblib')

def preprocess_input(data):
    # Assuming 'Item_Fat_Content' needs replacement, as per your previous code
    data.replace({'Item_Fat_Content': {'low fat':'Low Fat','LF':'Low Fat', 'reg':'Regular'}}, inplace=True)

    # Use the loaded encoder to transform the categorical columns
    data_encoded = loaded_encoder.transform(data)

    return pd.DataFrame(data_encoded)

def predict_price(args):
    # Create a DataFrame from the input data
    input_data = pd.DataFrame([(args.Item_Identifier, args.Item_Weight, args.Item_Fat_Content,
                                args.Item_Visibility, args.Item_Type, args.Item_MRP,
                                args.Outlet_Identifier, args.Outlet_Establishment_Year,
                                args.Outlet_Size, args.Outlet_Location_Type, args.Outlet_Type)],
                               columns=['Item_Identifier', 'Item_Weight', 'Item_Fat_Content',
                                        'Item_Visibility', 'Item_Type', 'Item_MRP',
                                        'Outlet_Identifier', 'Outlet_Establishment_Year',
                                        'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type'])

    # Preprocess the input data
    preprocessed_input = preprocess_input(input_data)

    # Make predictions
    pred = loaded_model.predict(preprocessed_input)[0]
    return pred

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='sales prediction')
    parser.add_argument('--Item_Identifier', type=str, required=True, help='Item Identifier')
    parser.add_argument('--Item_Weight', type=float, required=True, help='Item Weight')
    parser.add_argument('--Item_Fat_Content', type=str, required=True, help='Item Fat Content')
    parser.add_argument('--Item_Visibility', type=float, required=True, help='Item Visibility')
    parser.add_argument('--Item_Type', type=str, required=True, help='Item Type')
    parser.add_argument('--Item_MRP', type=float, required=True, help='Item MRP')
    parser.add_argument('--Outlet_Identifier', type=str, required=True, help='Outlet Identifier')
    parser.add_argument('--Outlet_Establishment_Year', type=float, required=True, help='Outlet Establishment Year')
    parser.add_argument('--Outlet_Size', type=str, required=True, help='Outlet Size')
    parser.add_argument('--Outlet_Location_Type', type=str, required=True, help='Outlet Location Type')
    parser.add_argument('--Outlet_Type', type=str, required=True, help='Outlet Type')

    args = parser.parse_args()

    # Call the predict_price function with the parsed arguments
    prediction = predict_price(args)
    print(f"sales prediction is: {prediction}")

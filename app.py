import streamlit as st
import pandas as pd
import joblib
import math


model = joblib.load("weekend_getaway_ranker_model.pkl")
scaler = model["scaler"]
weights = model["weights"]

df = pd.read_csv("Top Indian Places to Visit.csv")
coords = pd.read_csv("city_coordinates.csv")

city_aliases = {
    "New Delhi": "Delhi"
}

df["City"] = df["City"].replace(city_aliases)
coords["City"] = coords["City"].replace(city_aliases)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))

st.title("🏖️ Weekend Getaway Ranker")
st.write("Find the best weekend destinations based on distance, rating, and popularity.")

source_city = st.selectbox(
    "Select your source city",
    sorted(coords["City"].unique())
)

top_n = st.slider("Number of recommendations", 5, 15, 10)

if st.button("Get Recommendations"):
    src_lat, src_lon = coords[coords["City"] == source_city][
        ["latitude", "longitude"]
    ].values[0]

    df_pred = df.copy()
    df_pred = df_pred[df_pred["City"] != source_city]
    df_pred = df_pred.merge(coords, on="City", how="left")
    
    df_pred["distance_km"] = df_pred.apply(
        lambda row: haversine(
            src_lat, src_lon,
            row["latitude"], row["longitude"]
        ),
        axis=1
    )

    X = df_pred[[
        "Google review rating",
        "Number of google review in lakhs",
        "distance_km"
    ]]

    X_scaled = scaler.transform(X)
    df_pred["final_score"] = X_scaled @ weights

    result = df_pred.sort_values(
        "final_score", ascending=False
    ).head(top_n).reset_index(drop=True)

    result.index = result.index + 1
    
    # st.dataframe(
    #     result[["City", "Name", "distance_km", "final_score"]]
    # )
    display_df = result.copy()

    display_df["Distance (km)"] = display_df["distance_km"].round(1)
    display_df["Rating"] = display_df["Google review rating"]
    display_df["Popularity (Lakhs)"] = display_df["Number of google review in lakhs"]

    display_df = display_df[[
        "City",
        "Name",
        "Distance (km)",
        "Rating",
        "Popularity (Lakhs)"
    ]]

    st.dataframe(display_df)


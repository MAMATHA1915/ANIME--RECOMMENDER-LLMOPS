import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv



st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()    

st.title("Anime Recommender System")
query = st.text_input("Enter your query (e.g., 'I want to watch a fantasy anime with magic and adventure'):")

if query:
    with st.spinner("Generating recommendation..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(response)





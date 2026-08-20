from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try:
            logger.info("Initializing the Anime Recommendation Pipeline...")

            vector_builder = VectorStoreBuilder(csv_path=" ", persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)

            logger.info("Anime Recommendation Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing Anime Recommendation Pipeline: {e}")
            raise CustomException("Error initializing Anime Recommendation Pipeline", e)

    def recommend(self, query: str):
        try:
            logger.info(f"received a query: {query}")
            recomendation = self.recommender.get_recommendation(query)
            logger.info(f"Recommendation generated successfully for query: {query}")
            return recomendation
        except Exception as e:
            logger.error(f"Error generating recommendation for query '{query}': {e}")
            raise CustomException(f"Error generating recommendation for query '{query}'", e)



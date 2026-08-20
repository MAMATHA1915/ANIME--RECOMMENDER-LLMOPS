from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)


def main():
    try:
        logger.info("Starting the build pipeline...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/processed_anime_data.csv")
        processed_csv_path = loader.load_and_process()
        logger.info(f"Data loaded and processed successfully. Processed CSV saved at: {processed_csv_path}")

        vector_builder = VectorStoreBuilder(csv_path=processed_csv_path, persist_dir="chroma_db")
        vector_builder.build_and_save_vector_store()

        logger.info("Vector store built and saved successfully.")

        logger.info("Build pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Error in build pipeline: {e}")
        raise CustomException("Error in build pipeline", e)


if __name__ == "__main__":
    main()


        
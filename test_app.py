import unittest
from unittest.mock import patch, MagicMock
from task.app import MicrowaveRAG

class TestMicrowaveRAG(unittest.TestCase):

    @patch('task.app.AzureChatOpenAI')
    @patch('task.app.AzureOpenAIEmbeddings')
    def test_rag_pipeline(self, mock_embeddings, mock_llm_client):
        # Mock the language model and embeddings
        mock_llm_instance = mock_llm_client.return_value
        mock_llm_instance.invoke.return_value.content = "Mocked response"
        
        mock_embeddings_instance = mock_embeddings.return_value

        # Mock the vector store
        mock_vectorstore = MagicMock()
        mock_vectorstore.similarity_search_with_relevance_scores.return_value = [
            (MagicMock(page_content="Test context"), 0.9)
        ]

        with patch('task.app.FAISS.load_local', return_value=mock_vectorstore):
            with patch('task.app.os.path.exists', return_value=True):
                rag = MicrowaveRAG(embeddings=mock_embeddings_instance, llm_client=mock_llm_instance)
                
                # Test the full pipeline
                context = rag.retrieve_context("test query")
                self.assertEqual(context, "Test context")
                
                augmented_prompt = rag.augment_prompt("test query", context)
                self.assertIn("Test context", augmented_prompt)
                self.assertIn("test query", augmented_prompt)
                
                answer = rag.generate_answer(augmented_prompt)
                self.assertEqual(answer, "Mocked response")

if __name__ == '__main__':
    unittest.main()

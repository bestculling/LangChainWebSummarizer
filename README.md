## Text Summarization API with LangChain and FastAPI

This repository provides a simple FastAPI application that uses LangChain to summarize web pages. It leverages the power of Google Gemini Pro and offers language selection for Thai and English summaries.

### Features

- **Web Page Summarization:**  Provides concise summaries of web page content.
- **Multilingual Support:**  Offers summaries in both Thai and English.
- **FastAPI Framework:**  Uses FastAPI for a modern and performant API experience.

### Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bestculling/LangChainWebSummarizer.git
   cd LangChainWebSummarizer
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

5. **Run the Application:**
   ```bash
   uvicorn main:app --reload 
   ```

### Usage

1. **Send a POST request to `/summarize` with the following JSON payload:**
   ```json
   {
     "url": "https://example.com/article-to-summarize",
     "language": "en" // "th" for Thai
   }
   ```
2. **The API will respond with the summary in JSON format:**
   ```json
   {
     "summary": "This is a concise summary of the web page content."
   }
   ```

### Example

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://en.wikipedia.org/wiki/Artificial_intelligence", "language": "en"}' http://localhost:8000/summarize 
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes. 
